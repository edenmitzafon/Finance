from dotenv import load_dotenv
import os

# take environment variables from .env.
load_dotenv()

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


def is_typed(field):
    if not request.form.get(field):
        flash (f"Must provide {field}")
        return apology(f"Must provide {field}", 400)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/add_funds", methods=["GET", "POST"])
@login_required
def add_funds():
    if request.method == "POST":
        db.execute("""
            UPDATE users
            SET cash = cash + :added_cash
            WHERE id=:user_id
        """, added_cash = request.form.get("amount"),
        user_id = session["user_id"])
        flash("Succesfully Added Funds")
        return redirect("/")
    else:
        return render_template("add_funds.html")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rows = db.execute("""
        SELECT symbol, SUM(share_number) as number_of_shares
        FROM transactions
        WHERE user_id = :user_id
        GROUP BY symbol
        HAVING number_of_shares > 0;
    """, user_id=session["user_id"])
    holdings = []
    grand_total = 0
    for row in rows:
        stock = lookup(row["symbol"])
        holdings.append({
            "symbol": stock["symbol"],
            "name": stock["name"],
            "shares": row["number_of_shares"],
            "price": usd(stock["price"]),
            "total": usd(stock["price"] * row["number_of_shares"])
        })
        grand_total += stock["price"] * row["number_of_shares"]
    rows = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])
    cash = rows[0]["cash"]
    grand_total += cash
    return render_template("index.html", holdings=holdings, cash=usd(cash), grand_total=usd(grand_total))



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        find_errors = is_typed("symbol") or is_typed("shares")
        if find_errors:
            return find_errors
        elif not request.form.get("shares").isdigit:
            flash ("Invalid number of shares")
            return apology("Invalid number of shares", 400)
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)
        shares = int(request.form.get("shares"))
        if stock == None:
            return ("invalid symbol", 400)
        rows = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = rows[0]["cash"]
        remaining_cash = cash - (shares * stock["price"])
        if remaining_cash < 0:
            flash ("Insufficient funds")
            return apology("Insufficient funds", 400)
        db.execute("UPDATE users SET cash=:remaining_cash WHERE id=:id",
                remaining_cash=remaining_cash,
                id=session["user_id"])
        db.execute("""INSERT INTO transactions (user_id, symbol, share_number, price)
        VALUES (:user_id, :symbol, :share_number, :price)
        """, user_id = session["user_id"],
        symbol = stock["symbol"],
        share_number = shares,
        price = stock["price"]
        )
        flash ("Successful Transaction")
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("""
        SELECT symbol, share_number, price, transaction_time
        FROM transactions
        WHERE user_id = :user_id
    """, user_id=session["user_id"])
    for i in range(len(transactions)):
        transactions[i]["price"] = usd(transactions[i]["price"])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username and password was submitted
        result_checked = is_typed("username") or is_typed("password")
        if result_checked != None:
            return result_checked

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash ("Invalid username and/or password.")
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        result_check = is_typed("symbol")
        if result_check != None:
            return result_check
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)
        if stock == None:
            flash("Invalid symbol.")
            return apology("invalid symbol", 400)
        return render_template("quoted.html", stock_data={
            "name": stock["name"],
            "symbol": stock["symbol"],
            "price": usd(stock["price"])
        })
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        special_char = ['!', '#', '$', '%', '&', ')', '(', '*', '+', ',', '-', '.', '/', ':', ';', '<', '>', '=', '?', '@', '[', ']', '^', '_', '}', '{', '|', '~']
        if not username:
            flash ("You must provide a username.")
            return apology("You must provide a username.", 400)
        if not password:
            flash ("You must provide a password")
            return apology("You must provide a password", 400)
        if not confirmation:
            flash ("Confirm your password")
            return apology("Confirm your password", 400)
        if len(password) < 8 or len(password) > 20:
            flash("Password must contain between 8-20 characters.")
            return apology("Password must contain between 8-20 characters.", 400)
        if not any(char.isdigit() for char in password):
            flash ("Password must contain at least 1 number.")
            return apology("Password must contain at least 1 number.", 400)
        if not any(char.isupper() for char in password):
            flash ("Password must contain at least 1 uppercase letter.")
            return apology ("Password must contain at least 1 uppercase letter.", 400)
        if not any(char in special_char for char in password):
            flash ("Password must contain at least 1 special character.")
            return apology("Password must contain at least 1 special character.", 400)
        if password != confirmation:
            flash ("Passwords must match.")
            return apology("Passwords must match.", 400)
        else:
            password = password
        try:
            primary_key = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                    username=request.form.get("username"),
                    hash = generate_password_hash(request.form.get("password")))
        except:
            flash ("Username already exists")
            return apology("username already exists", 400)
        if primary_key == None:
            flash ("Registration error")
            return apology("registration error", 400)
        session["user_id"] = primary_key
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        find_errors = is_typed("symbol") or is_typed("shares")
        if find_errors:
            return find_errors
        elif not request.form.get("shares").isdigit:
            flash ("Invalid number of shares")
            return apology("invalid number of shares", 400)
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)
        shares = int(request.form.get("shares"))
        if stock == None:
            return ("invalid symbol", 400)
        rows = db.execute ("""
            SELECT symbol, SUM(share_number) as total_shares FROM transactions
            WHERE user_id=:user_id
            GROUP BY symbol
            HAVING total_shares > 0;
        """, user_id=session["user_id"])
        for row in rows:
            if row["symbol"] == symbol:
                if shares > row["total_shares"]:
                    flash ("Not enogth shares in stock")
                    return apology("Not enogth shares in stock", 400)

        rows = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = rows[0]["cash"]
        remaining_cash = cash + (shares * stock["price"])

        db.execute("UPDATE users SET cash=:remaining_cash WHERE id=:id",
                remaining_cash=remaining_cash,
                id=session["user_id"])
        db.execute("""INSERT INTO transactions (user_id, symbol, share_number, price)
        VALUES (:user_id, :symbol, :share_number, :price)
        """, user_id = session["user_id"],
        symbol = stock["symbol"],
        share_number = -1 * shares,
        price = stock["price"]
        )
        flash ("Successfuly Sold")
        return redirect("/")
    else:
        rows = db.execute("""
            SELECT symbol
            FROM transactions
            WHERE user_id=:user_id
            GROUP BY symbol
            HAVING SUM(share_number) > 0;
        """, user_id=session["user_id"])
        return render_template("sell.html", symbols=[ row["symbol"] for row in rows ])

@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change the user's password"""
    current_user_id = session["user_id"]

    if request.method == "POST":
        current_password = request.form.get("current-password")
        confirmation = request.form.get("confirmation")
        new_password = request.form.get("new-password")
        special_char = ['!', '#', '$', '%', '&', ')', '(', '*', '+', ',', '-', '.', '/', ':', ';', '<', '>', '=', '?', '@', '[', ']', '^', '_', '}', '{', '|', '~']

        search_user = db.execute("SELECT * FROM users WHERE id = ?", current_user_id)

        if not current_password:
            flash ("You must provide a password")
            return apology("You must provide a password", 400)
        if not confirmation:
            flash ("You must confirm your password")
            return apology("You must confirm your password", 400)
        if current_password != confirmation:
            flash ("Passwords don't match")
            return apology("Passwords don't match", 400)
        if not new_password:
            flash ("You must provide a new password")
            return apology("You must provide a new password", 400)
        if not check_password_hash(search_user[0]["hash"], request.form.get("current-password")):
            flash ("Invalid password.")
            return apology("Invalid password.", 400)
        if len(new_password) < 8 or len(new_password) > 20:
            flash("Password must contain between 8-20 characters.")
            return apology("Password must contain between 8-20 characters.", 400)
        if not any(char.isdigit() for char in new_password):
            flash ("Password must contain at least 1 number.")
            return apology("Password must contain at least 1 number.", 400)
        if not any(char.isupper() for char in new_password):
            flash ("Password must contain at least 1 uppercase letter.")
            return apology ("Password must contain at least 1 uppercase letter.", 400)
        if not any(char in special_char for char in new_password):
            flash ("Password must contain at least 1 special character.")
            return apology("Password must contain at least 1 special character.", 400)
        if current_password != confirmation:
            flash ("Passwords must match.")
            return apology("Passwords must match.", 400)
        else:
            new_password = new_password

        hash = generate_password_hash(new_password)

        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, current_user_id)

        return render_template("login.html")

    else:
        return render_template("change_password.html")

