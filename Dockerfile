# Python 3.11 slim tabanlı imajı kullan
FROM python:3.11-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Tüm dosyaları container içine kopyala
COPY . /app

# Port aç
EXPOSE 8080

# Sunucuyu başlat
CMD ["python", "server.py"]
