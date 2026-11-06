# Ubuntu Server Project

Ubuntu 26.04 üzerinde SSH anahtar erişimi, UFW güvenlik duvarı, Nginx ve Flask uygulaması kurulum projesi.

## Mimari

İstek -> Nginx:80 -> Gunicorn:8000 -> Flask

## İçerik

- `app/app.py`: Flask uygulaması ve `/health` adresi
- `app/requirements.txt`: Python paketleri
- `deploy/portfolio-app.service`: systemd servis ayarı
- `deploy/nginx.conf`: Nginx ters proxy ayarı

## Loglar

- Uygulama: `sudo journalctl -u portfolio-app -n 50`
- Nginx erişim: `sudo tail -n 50 /var/log/nginx/access.log`
- Nginx hata: `sudo tail -n 50 /var/log/nginx/error.log`

## Güvenlik

SSH anahtarıyla giriş etkin; root ve parola ile SSH girişi kapalıdır.
Özel anahtarlar, parolalar ve sanal ortam depoya eklenmez.
