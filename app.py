from flask import Flask, jsonify, render_template, request

from chatbot_engine import TextileChatbot

app = Flask(__name__)
chatbot = TextileChatbot("data/textile_knowledge.json")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}
    message = (payload.get("message") or "").strip()

    if not message:
        return jsonify({"reply": "Please ask a textile-related question."}), 400

    reply = chatbot.get_reply(message)
    return jsonify({"reply": reply})
