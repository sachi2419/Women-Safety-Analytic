# from flask import Flask, render_template, request, jsonify
# import telebot
# import sqlite3

# app = Flask(__name__)

# # Telegram Bot Setup
# TOKEN = "7380544518:AAGmEk7-qgNZOqksggmMg_l2TcRS_ipSx8Q"
# bot = telebot.TeleBot(TOKEN)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/analyze", methods=["POST"])
# def analyze():
#     data = request.json
#     result = {"message": "Analysis complete", "data": data}
#     return jsonify(result)

# # Start Flask
# if __name__ == "__main__":
#     app.run(debug=True)
