from flask import Flask, render_template, request
import smtplib
import os
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = "crimson-secret-key"

# Your Gmail address
GMAIL_ADDRESS = "lakendra.m.nichols@gmail.com"
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")


# ==========================================
# GET IMAGES FROM STATIC/IMAGES
# ==========================================

def get_images():
    images = os.listdir("static/images")

    return [
        image for image in images
        if image.lower().endswith(
            (".jpg", ".jpeg", ".png", ".gif", ".webp")
        )
    ]


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# SHOP
# ==========================================

@app.route("/shop")
def shop():
    images = get_images()

    return render_template(
        "shop.html",
        images=images
    )


# ==========================================
# GALLERY
# ==========================================

@app.route("/gallery")
def gallery():
    images = get_images()

    return render_template(
        "gallery.html",
        images=images
    )


# ==========================================
# BUY
# ==========================================

@app.route("/buy/<image>")
def buy(image):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Purchase - Crimson Shop</title>
    </head>

    <body style="background:#080000; color:#ddd; text-align:center; padding:60px;">

        <h1>CRIMSON SHOP</h1>

        <h2>Purchase Artwork</h2>

        <p>{image}</p>

        <h3>$10.00</h3>

        <p>Checkout coming soon.</p>

        <a href="/shop">BACK TO SHOP</a>

    </body>
    </html>
    """


# ==========================================
# CONTACT
# ==========================================

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        msg = EmailMessage()

        msg["Subject"] = f"Crimson Shop Contact - {name}"
        msg["From"] = GMAIL_ADDRESS
        msg["To"] = GMAIL_ADDRESS
        msg["Reply-To"] = email

        msg.set_content(
            f"Customer Name: {name}\n"
            f"Customer Email: {email}\n\n"
            f"Message:\n{message}"
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(
                GMAIL_ADDRESS,
                GMAIL_APP_PASSWORD
            )

            smtp.send_message(msg)

        return "Message sent successfully!"

    return render_template("contact.html")


# ==========================================
# RUN FLASK
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)