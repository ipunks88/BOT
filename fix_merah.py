import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

# ==== CEK ARGUMEN ====
if len(sys.argv) < 2:
    print("❗ Gunakan: python fix_merah.py +6012345678	9")
    sys.exit(1)

nomor = sys.argv[1]

# ==== KONFIGURASI PENGIRIM ====
email_pengirim = "gbwaip4@gmail.com"        # Ganti dengan email kamu
password_email = "tmabnycprxjxlzyt"          # Gunakan App Password Gmail

# ==== KONFIGURASI PENERIMA ====
email_penerima = "android@support.whatsapp.com"  # Tujuan WhatsApp Support

# ==== ISI PESAN ====
isi_pesan = f"""Здравствуйте, команда WhatsApp!

У меня возникла проблема при попытке перенести мой аккаунт WhatsApp на новый телефон. Приложение показывает сообщение:
«Используйте свой другой телефон, чтобы подтвердить перенос WhatsApp на этот»

К сожалению, я не могу получить уведомление, потому что мой старый телефон потерян.

Информация о моём аккаунте:

Номер WhatsApp:  [{nomor}]

Проблема: Не получаю код подтверждения и не могу подтвердить перенос аккаунта, так как старый телефон утерян.


Прошу помочь верифицировать и восстановить доступ к моему аккаунту, чтобы я мог(ла) снова использовать WhatsApp на новом устройстве.

Заранее благодарю за помощь и внимание.

С уважением,
[Amanda]
"""

# ==== KIRIM EMAIL ====
pesan = MIMEMultipart()
pesan["From"] = "gbwaip4@gmail.com"
pesan["To"] = "android@support.whatsapp.com"
# ❌ Tidak ada pesan["Subject"] (biarkan kosong)
pesan.attach(MIMEText(isi_pesan, "plain"))

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email_pengirim, password_email)
        server.send_message(pesan)
        print(f"✅ Email untuk nomor {nomor} berhasil dikirim ke WhatsApp Support tanpa subjek!")
except Exception as e:
    print("❌ Gagal mengirim email:", e)
