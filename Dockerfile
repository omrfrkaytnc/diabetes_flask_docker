# Temel Docker imajı
FROM python:3.11-slim

# Çalışma dizinini ayarla
WORKDIR /opt

# Sistem kütüphanelerini yükle
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Gereksinimleri kopyala ve yükle
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Uygulama portunu aç
EXPOSE 5000

# Flask uygulamasını başlat
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
