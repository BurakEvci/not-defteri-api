# Temel Python imajı
FROM python:3.9-slim

# Uygulama dizini oluştur
WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyasını kopyala
COPY app.py .

# Uygulamayı çalıştır
CMD ["python", "app.py"]
