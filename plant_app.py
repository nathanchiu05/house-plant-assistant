from flask import Flask, request, render_template
import os
from plant_main import evaluate_plant #grab details from plants_need_sun.py
from plant_main import is_night
from plant_main import classify_plant

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        img_file = request.files.get("image") #get image
        direction = request.form.get("direction", "Unknown") #get direction

        if not direction:
            direction = "South"

        if img_file:
            img_path = os.path.join(UPLOAD_FOLDER, img_file.filename)
            img_file.save(img_path)

            data = evaluate_plant(img_path, direction) #call function from plants_need_sun.py

            if is_night(data["time_of_day"]):
                return render_template("sleeping.html", data=data)
            else:
                return render_template("results.html", data=data) #render results page with data

        return "No file uploaded."

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=("cert.pem", "key.pem"))