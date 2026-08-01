from flask import Flask, render_template, request, redirect, url_for, flash
from salary_tax import calculate_final_income

app = Flask(__name__)
app.secret_key = "dev-secret"


@app.route("/", methods=["GET"]) 
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"]) 
def calculate():
    s = request.form.get("salary", "").strip()
    try:
        salary = float(s.replace(',', ''))
    except Exception:
        flash("Enter a numeric salary.", "error")
        return redirect(url_for("index"))
    try:
        rate, tax, final = calculate_final_income(salary)
    except ValueError as e:
        flash(str(e), "error")
        return redirect(url_for("index"))
    return render_template("result.html", salary=salary, rate=rate, tax=tax, final=final)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
