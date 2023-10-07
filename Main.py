from flask import Flask, render_template
import random

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/rastgele_gercek")
def rasgele():
    liste = ["rüzgar muz yiyo Emir elmayedi Rüzgar muzunu düşürdü Emir BRUH","aaaaa","sen naaptın?","Emo baba td2 Heavy+MMedic diooooo"]

    x = random.choice(liste)

    return render_template('rasgele.html',x=x)


app.run(debug=True)