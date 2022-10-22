<br />
<div align="center">
  <a href="https://github.com/edenmitzafon/Finance.git">
    <img src="static/icon.png" alt="Logo" width="80" height="80">
  </a>


<h2 align="center">FINANCE</h2>

  <p align="center">
    A finantial app that allows you to trade stocks
    <br />
    <a href="https://github.com/edenmitzafon/Finance.git"><strong>Explore the docs »</strong></a>
  </p>
</div>

#### **Note:** this project was completed as part of Harvard's CS50 course on edX. Project requierments can be found [here](https://cs50.harvard.edu/x/2022/psets/9/).
<br>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#about-the-project">About The Project</a>
      <ul>
        <li><a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#getting-started">Getting Started</a>
      <ul>
        <li><a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#prerequisites">Prerequisites</a></li>
        <li><a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#roadmap">Roadmap</a></li>
    <li><a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#license">License</a></li>
    <li><a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#contact">Contact</a></li>
  </ol>
</details>

## About The Project
![project-screenshot0]

A web app via which you can manage portfolios of stocks. Not only will this tool allow you to check real stocks’ actual prices and portfolios’ values, it will also let you buy (okay, “buy”) and sell (okay, “sell”) stocks by querying [IEX](https://iexcloud.io/) api for stocks’ prices.
<br>

<p align="right">(<a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#finance">back to top</a>)</p>

### Built With

[![flask][flask.com]][flask-url]  
[![html][html.com]][html-url]  
[![css][css.com]][css-url]  
[![sqlite][sqlite.com]][sqlite-url]  
[![Bootstrap][Bootstrap.com]][Bootstrap-url]  

<p align="right">(<a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#finance">back to top</a>)</p>

## Getting Started
To get a local copy up and running follow these simple steps:
### Prerequisites

```sh
pip3 install flask
```
```sh
pip3 install Werkzeug
```
```sh
pip3 install flask_session
```
```sh
pip3 install python-dotenv
```
```sh
pip3 install cs50
```
<p align="right">(<a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#finance">back to top</a>)</p>

### Installation

1. Get a free API Key at [IEX](https://iexcloud.io/)
1. Clone the repo
   ```sh
   git clone https://github.com/edenmitzafon/Finance.git
   ```
1. Install pip3 packages
   ```sh
   pip3 install
   ```
1. Enter your API key in `.env`
   ```sh
   API_KEY='value'
   ```
   where `value` is that (pasted) key, without any space immediately before or after the =.
1. Start Flask’s built-in web server (within `finance/`):
    ```
    python -m flask run
    ```
1. Stop the app by using `Ctrl+C` in the terminal

<p align="right">(<a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#finance">back to top</a>)</p>

## Roadmap
#### For this project, I implemented the following:

1. `register` - Allows a user to register for an account. The username and the hashed password are submitted via Flask and stored in a SQL database.
![project-screenshot1]
The password is validated against several criteria including:

    * Password must contain between 8-20 characters.
    * Password must contain at least 1 number.
    * Password must contain at least 1 uppercase letter.
    * Password must contain at least 1 special character.
1. `log in` - Allows a user to log into his or her account if they are registered to the site.
![project-screenshot9]
1. `quote` - Allows a user to look up the current price of a stock using the stock symbol.
![project-screenshot2]
![project-screenshot3]
1. `buy` - Enables a user to buy stocks. Purchased stocks are saved to the database.
![project-screenshot4]
1. `index` - Displays an HTML table summarizing, for the user currently logged in, which stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding. Also display the user’s current cash balance along with a grand total.
![project-screenshot0]
1. `sell` -  Enables a user to sell shares of a stock (that he or she owns). Sold stocks are removed from the database and their cash balance is updated.
![project-screenshot5]
![project-screenshot6]
1. `history` - Displays an HTML table summarizing the transaction history for the user.
![project-screenshot7]
1. `change_password` - Allows users to change their passwords folowing the same validation criteria as in register and then hashing the new password and storing it in the SQL database.
![project-screenshot8]
1. `CSS, HTML & SQL` - Queries, writing HTML and styling with CSS and bootstrap.

<p align="right">(<a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#finance">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#finance">back to top</a>)</p>


## Contact

[![linkedin][linkedin.com]][linkedin-url]  

Project Link: [https://github.com/edenmitzafon/Finance](https://github.com/edenmitzafon/Finance)

<p align="right">(<a href="https://github.com/edenmitzafon/Finance/blob/main/README.md#finance">back to top</a>)</p>


[project-screenshot0]: https://github.com/edenmitzafon/Finance/blob/main/images/project.png
[project-screenshot1]: https://github.com/edenmitzafon/Finance/blob/main/images/regisger.png
[project-screenshot2]: https://github.com/edenmitzafon/Finance/blob/main/images/quote.png
[project-screenshot3]: https://github.com/edenmitzafon/Finance/blob/main/images/quote2.png
[project-screenshot4]: https://github.com/edenmitzafon/Finance/blob/main/images/buy.png
[project-screenshot5]: https://github.com/edenmitzafon/Finance/blob/main/images/sell.png
[project-screenshot6]: https://github.com/edenmitzafon/Finance/blob/main/images/sell2.png
[project-screenshot7]: https://github.com/edenmitzafon/Finance/blob/main/images/history.png
[project-screenshot8]: https://github.com/edenmitzafon/Finance/blob/main/images/password.png
[project-screenshot9]: https://github.com/edenmitzafon/Finance/blob/main/images/login.png


[linkedin.com]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/eden-mitzafon-1a2657254/
[sqlite.com]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[sqlite-url]: https://www.sqlite.org/index.html
[css.com]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[css-url]: https://www.w3.org/Style/CSS/Overview.en.html
[html.com]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[html-url]: https://html.com/
[flask.com]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
