from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

# Create folder if not exists
if not os.path.exists("queries"):
    os.makedirs("queries")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/inquiry", methods=["GET", "POST"])
def inquiry():
    if request.method == "POST":
        name = request.form["name"].strip().replace(" ", "_")
        contact = request.form["contact"].strip()
        profession = request.form["profession"]
        flat_type = request.form["flat_type"]
        budget = request.form["budget"]

        # ✅ Save filename as Name + Contact
        filename = f"{name}_{contact}.txt"

        # ⚡ If you want unique filename each time, use timestamp also:
        # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # filename = f"{name}_{contact}_{timestamp}.txt"

        # Save query in text file
        with open(os.path.join("queries", filename), "w") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Contact: {contact}\n")
            f.write(f"Profession: {profession}\n")
            f.write(f"Flat Type: {flat_type}\n")
            f.write(f"Budget: {budget}\n")
            f.write("------------\n")

        return redirect(url_for("success"))

    return render_template("inquiry.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
