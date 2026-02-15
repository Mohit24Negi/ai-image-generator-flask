from flask import Flask, render_template, request, session, redirect
import requests
import base64
import os


app = Flask(__name__)
app.secret_key = "supersecretkey"

# --------------------------
# HuggingFace API Setup
# --------------------------
HF_API_KEY = os.getenv("HF_API_KEY")


API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

# --------------------------
# Image Generator
# --------------------------
def generate_image(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        return base64.b64encode(response.content).decode("utf-8")
    else:
        print("ERROR:", response.text)
        return None

# --------------------------
# Clear History
# --------------------------
@app.route("/clear", methods=["POST"])
def clear_history():
    session["history"] = []
    return redirect("/")

# --------------------------
# Main Route
# --------------------------
@app.route("/", methods=["GET", "POST"])
def index():

    if "history" not in session:
        session["history"] = []

    error = None

    if request.method == "POST":
        prompt = request.form.get("prompt")

        if prompt:
            image_data = generate_image(prompt)

            if image_data:
                session["history"].insert(0, image_data)
                session.modified = True
            else:
                error = "Image generation failed."
        else:
            error = "Please enter a description."

    return render_template("index.html",
                           history=session.get("history", []),
                           error=error)

if __name__ == "__main__":
    app.run(debug=True)
