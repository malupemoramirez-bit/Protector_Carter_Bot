from flask import Flask, request
import requests
import os
from respuestas import responder

app = Flask(__name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")


@app.route("/", methods=["GET"])
def home():
    return "Protector Carter Bot funcionando"


@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token == VERIFY_TOKEN:
            return challenge

        return "Token incorrecto", 403

    if request.method == "POST":

        data = request.get_json()

        print(data)

        if "entry" in data:
            for entry in data["entry"]:

                for event in entry["messaging"]:

                    if "message" in event:

                        sender_id = event["sender"]["id"]

                        if "text" in event["message"]:

                            texto = event["message"]["text"]

                            mensaje, imagen = responder(texto)

                            # Enviar texto
                            send_message(sender_id, mensaje)

                            # Enviar imagen si existe
                            if imagen:
                                send_image(sender_id, imagen)

        return "EVENT_RECEIVED", 200


def send_message(recipient_id, message):

    url = f"https://graph.facebook.com/v25.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message
        }
    }

    r = requests.post(url, json=payload, headers=headers)

    print("MENSAJE:", r.status_code)
    print(r.text)


def send_image(recipient_id, image_url):

    url = f"https://graph.facebook.com/v25.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": image_url,
                    "is_reusable": True
                }
            }
        }
    }

    r = requests.post(url, json=payload, headers=headers)

    print("IMAGEN:", r.status_code)
    print(r.text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)