Python salary tax calculator

Usage

Run the program with Python 3:

```bash
python salary_tax.py
```

Enter your salary when prompted (commas are allowed). The program prints:
- your salary
- applied tax rate
- tax amount
- final income after tax

Tax rules implemented:
- salary < 30000 -> 5%
- 30000 <= salary <= 70000 -> 15%
- salary > 70000 -> 20%

Installable application

You can install this project (editable) and get a `salary-tax` command:

```bash
pip install -e .
salary-tax --salary 45000
salary-tax --gui   # open the simple Tkinter GUI
```

Run the web application

Install dependencies and run the Flask web server:

```bash
pip install -r requirements.txt
python web_app.py
# then open http://127.0.0.1:5000 in your browser
```
