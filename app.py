from flask import Flask
from redis import Redis

app = Flask(__name__)
# Buradaki "host='redis'" kısmı çok kritik!
# Normalde 'localhost' yazarız ama Docker dünyasında servis ismini kullanacağız.
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
        # Sayacı 1 arttır
        count = redis.incr('hits')
    except Exception as e:
        return "Veritabanına bağlanılamadı! Redis çalışıyor mu?"

    return f"Merhaba Oguzhan! Bu sayfayı şu ana kadar {count} kez görüntüledin."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)