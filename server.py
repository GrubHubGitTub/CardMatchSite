from flask import Flask, render_template, request, url_for
import random
import requests

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("index.html")

@app.route('/game', methods=["GET", "POST"])
def game():
    if request.method == "POST":
        cards = request.form["createcards"].splitlines()
        card_dic = {}
        count = 1
        for card in cards[0:12]:
            if card == "":
                pass
            else:
                try:
                    r = requests.get(card)
                    if r.status_code == 200:
                        card_dic[f"url{count}"] = card
                except Exception:
                    card_dic[str(count)] = card
                count += 1
        l = list(card_dic.items())
        random.shuffle(l)
        shuffled_cards = dict(l)
        return render_template("game.html", cards=shuffled_cards)

if __name__ == "__main__":
    app.run(debug=True)

