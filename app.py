# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Merhaba Oguzhan! Bu benim ilk Dockerize edilmiş uygulamam ve değişikliği hadi görelim!"

if __name__ == "__main__":
    # Uygulamayı dışarıya açmak için host='0.0.0.0' kullanıyoruz
    app.run(host='0.0.0.0', port=5000)