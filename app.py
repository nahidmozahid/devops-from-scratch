from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import random
from datetime import datetime

app = Flask(__name__)

# Replace this with your actual MongoDB URI (local or Atlas)
app.config["MONGO_URI"] = "mongodb://localhost:27017/birthdaydb"

mongo = PyMongo(app)

motivational_speeches = [
    "Believe in yourself and all that you are!",
    "Your potential is endless. Make this year count!",
    "Every day is a new beginning. Embrace it!",
    "Dream big, work hard, stay focused.",
    "You are stronger than you think. Keep going!",
    "Success is not final, failure is not fatal: It’s the courage to continue that counts.",
    "Stay positive, work hard, make it happen.",
    "This year will be your best yet — just keep pushing!",
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        birthday_str = request.form.get("birthday")
        try:
            birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
        except ValueError:
            error_msg = "Please enter a valid date!"
            return render_template("index.html", error=error_msg)

        today = datetime.today()
        next_birthday = birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_left = (next_birthday - today).days
        age = next_birthday.year - birthday.year
        speech = random.choice(motivational_speeches)

        # Save user birthday and speech to DB
        mongo.db.users.insert_one({
            "birthday": birthday_str,
            "next_birthday": next_birthday.strftime("%Y-%m-%d"),
            "age": age,
            "speech": speech,
            "created_at": datetime.utcnow()
        })

        return render_template(
            "result.html",
            speech=speech,
            days_left=days_left,
            birthday=next_birthday.strftime("%B %d, %Y"),
            age=age,
        )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
