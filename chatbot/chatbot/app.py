```python
from flask import Flask, render_template, request, jsonify
from chatbot.chatbot import chatbot

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    if user_message.strip() == "":
        return jsonify({
            "reply": "Please enter a question."
        })

    bot_reply = chatbot.reply(user_message)

    return jsonify({
        "reply": bot_reply
    })


if __name__ == "__main__":
    app.run(debug=True)
```
