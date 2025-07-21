
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = [
    {"category": "kids", "name": "Spiderman Shirt", "price": 1500, "image": "spiderman_shirt.jpg", "description": "Cool Spiderman shirt for boys, breathable cotton."},
    {"category": "kids", "name": "Pink Full Dress", "price": 3500, "image": "pink_dress.jpg", "description": "Elegant pink full dress for girls."},
    {"category": "adults", "name": "Beige Pant and Shirt", "price": 5599, "image": "beige_pant_shirt.jpg", "description": "Classic beige pant and shirt for adults."},
    {"category": "shoes", "name": "Nike Air Jordan 5", "price": 21999, "image": "nike_air_jordan_5.jpg", "description": "Nike Air Jordan 5 for a premium sporty look."},
    {"category": "perfumes", "name": "Sauvage Men Perfume", "price": 9500, "image": "sauvage_perfume.jpg", "description": "Sauvage perfume with a strong masculine scent."},
    {"category": "accessories", "name": "Black Arabic Aura Watch", "price": 4999, "image": "black_arabic_watch.jpg", "description": "Elegant Arabic dial black watch."}
]

cart = []

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/add_to_cart/<product_name>")
def add_to_cart(product_name):
    for product in products:
        if product["name"] == product_name:
            cart.append(product)
            break
    return redirect(url_for("home"))

@app.route("/cart")
def view_cart():
    total = sum(item["price"] for item in cart) + 300
    return render_template("cart.html", cart=cart, total=total)

@app.route("/checkout", methods=["POST"])
def checkout():
    name = request.form["name"]
    address = request.form["address"]
    phone = request.form["phone"]
    cart.clear()
    return render_template("thank_you.html", name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
