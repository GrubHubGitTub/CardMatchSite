from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("index.html")

@app.route('/game', methods=["GET", "POST"])
def game():
    if request.method == "POST":
        input_is_url_list = str(request.form.getlist("imagecheck"))
        print(input_is_url_list)
        cards = {}
        for n in range(1, 13):
            text = request.form[f"Card{n}"]
            if text == "":
                pass
            elif str(n) in input_is_url_list:
                cards[f"url{n}"] = text
            else:
                cards[str(n)] = text
        l = list(cards.items())
        random.shuffle(l)
        shuffled_cards = dict(l)
        return render_template("game.html", cards=shuffled_cards)

if __name__ == "__main__":
    app.run(debug=True)

