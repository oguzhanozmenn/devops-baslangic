# 1. Taban olarak Python'un hafif bir sürümünü kullan
FROM python:3.9-slim

# 2. Konteyner içinde çalışma klasörünü belirle
WORKDIR /app

# 3. Önce gereksinim dosyasını kopyala
COPY requirements.txt .

# 4. Kütüphaneleri yükle
RUN pip install -r requirements.txt

# 5. Kalan proje dosyalarını kopyala
COPY . .

# 6. Uygulamanın 5000 portunu dışarıya açacağımızı belirt
EXPOSE 5000

# 7. Konteyner başladığında çalışacak komutu ver
CMD ["python", "app.py"]