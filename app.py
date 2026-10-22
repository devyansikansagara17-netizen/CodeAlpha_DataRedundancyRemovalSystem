
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "codealpha-project-secret"

DATABASE = "records.db"


def initialize_database():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


initialize_database()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()

        if len(name) < 2 or "@" not in email or "." not in email:
            flash("Please enter a valid name and email.", "error")
            return redirect(url_for("index"))

        try:
            with sqlite3.connect(DATABASE) as conn:
                conn.execute(
                    "INSERT INTO records (name, email, phone) VALUES (?, ?, ?)",
                    (name, email, phone)
                )
            flash("Record saved successfully!", "success")
        except sqlite3.IntegrityError:
            flash("Duplicate email! This record already exists.", "error")

        return redirect(url_for("index"))

    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row
        records = conn.execute(
            "SELECT * FROM records ORDER BY id DESC"
        ).fetchall()

    return render_template("index.html", records=records)


if __name__ == "__main__":
    app.run(debug=False)
