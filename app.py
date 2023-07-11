from flask import Flask, url_for, redirect, render_template, request
import random
app = Flask(__name__)

users = {}
public_reviews = {
    "Brandon":"This book is easily one of the best books you'll ever read. For me, a great measure of a good book is one you want to read again. I've read this book 3 times so far. Could not reccomend this book highly enough!",
    "Tom": "What a great Book!",
    "Mark": "Absolutely hated that book!",
} 

@app.route('/', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users[username] = password
        print(users)
        return redirect('login')
    return render_template("index.html", user='users')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        current_user = username
        if username in users and users[username] == password:
            print(f"current_user = {current_user}")
            return redirect('home')
    return render_template("login.html")

@app.route('/home', methods = ['GET', 'POST'])
def home():
    current_user = f'User{random.randint(0,5000)}'
    if request.method == "POST":
        review = request.form.get('review')
        public_reviews[current_user] = review
        print(public_reviews)
        return render_template("home.html", public_reviews = public_reviews)
        

    return render_template("home.html", public_reviews = public_reviews)

@app.route('/reviews')
def reviews():
    return render_template("reviews.html")

@app.route('/wish_list')
def wish_list():
    return render_template("wish_list.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)