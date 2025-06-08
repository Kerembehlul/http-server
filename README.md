# HTTP Web Server Projesi

## Proje Açıklaması
Bu proje, temel HTTP protokolünü kullanan kendi yazdığım basit bir web sunucusudur. Statik dosyalar `/static` klasöründen servis edilir, `/api/hello` endpoint'inden JSON yanıt döner.

## Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.11
- Docker (opsiyonel)

### Çalıştırma

**Docker ile:**
```bash
docker build -t http-server .
docker run -p 8080:8080 http-server
