from flask import Flask, render_template

app = Flask(__name__)

@app.route("/payments")
def payments_page():
    payments = [
        {"client": "Akbar Toshmatov",  "amount": 500000,  "paid": True,  "method": "Karta"},
        {"client": "Barno Yusupova",   "amount": 1200000, "paid": False, "method": "Naqd"},
        {"client": "Jasur Qodirov",    "amount": 750000,  "paid": True,  "method": "Karta"},
        {"client": "Dilnoza Xasanova", "amount": 300000,  "paid": False, "method": "Karta"},
        {"client": "Eldor Mirzayev",   "amount": 950000,  "paid": True,  "method": "Naqd"},
    ]

    total_paid = sum(p["amount"] for p in payments if p["paid"])
    total_debt = sum(p["amount"] for p in payments if not p["paid"])

    return render_template(
        "payments.html",
        payments=payments,
        total_paid=total_paid,
        total_debt=total_debt
    )

if __name__ == "__main__":
    app.run(debug=True)
