# AI Kata Sweet Shop Management System

## About
This project demonstrates **Test-Driven Development (TDD)** in Python by implementing a simple Sweet Shop Management System.  
The system allows adding sweets, placing orders, and managing stock.  
It’s built with **clean, modular code**, fully covered by unit tests, and includes an interactive runner script.

---

## Features
- Add sweets with price and stock
- Place orders for one or more sweets
- Automatically updates stock after orders
- Handles errors: ordering unavailable sweets or insufficient stock
- TDD implementation: tests written first, then code
- Interactive runner script to demo the system

---

## Project Structure

sweetshop/
│── src/
│ └── sweetshop.py # main SweetShop class
│── tests/
│ └── test_sweetshop.py # unit tests using pytest
│── run_sweetshop.py # interactive demo script
│── README.md

yaml
Copy code

---

## Setup

1. Clone the repo:

```bash
git clone https://github.com/sachinz25/sweetshop-incubyte.git
cd sweetshop-incubyte
Install dependencies (pytest):

bash
Copy code
pip install pytest
How to Run
Run Tests (TDD verification):
bash
Copy code
pytest -v
Run Interactive Script:
bash
Copy code
python run_sweetshop.py
Follow the prompts to view available sweets and place orders. The total bill and remaining stock will be displayed.

