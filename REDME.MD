# FINANCE

#### This project was completed as part of Harvard's CS50 course on edX. Project requierments can be found [here](https://cs50.harvard.edu/x/2022/psets/9/).
<br>

#### Description:

A web app via which you can manage portfolios of stocks. Not only will this tool allow you to check real stocks’ actual prices and portfolios’ values, it will also let you buy (okay, “buy”) and sell (okay, “sell”) stocks by querying [IEX](https://iexcloud.io/) api for stocks’ prices.
<br>

#### For this project, I implemented the following:

1. `register` - Allows a user to register for an account and log in. The username and the hashed password are submitted via Flask and stored in a SQL database.
The password is validated against several criteria including:

    * Password must contain between 8-20 characters.
    * Password must contain at least 1 number.
    * Password must contain at least 1 uppercase letter.
    * Password must contain at least 1 special character.
1. `quote` - Allows a user to look up the current price of a stock using the stock symbol.
1. `buy` - Enables a user to buy stocks. Purchased stocks are saved to the database.
1. `index` - Displays an HTML table summarizing, for the user currently logged in, which stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding. Also display the user’s current cash balance along with a grand total.
1. `sell` -  Enables a user to sell shares of a stock (that he or she owns). Sold stocks are removed from the database and their cash balance is updated.
1. `history` - Displays an HTML table summarizing the transaction history for the user.
1. `change_password` - Allows users to change their passwords folowwing the same validation criteria as in register and then hashing the new password and storing it in the SQL database.
1. `CSS, HTML & SQL` - Queries, writing HTML and styling with css and bootstrap.
