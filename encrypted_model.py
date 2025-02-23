from Crypto.Cipher import AES
import os

key = b'902697f03eb7fa022cb6256b9f05dd46'  # 32-byte key (AES-256)
nonce = os.urandom(12)  # ✅ ใช้ nonce 12 bytes (มาตรฐาน AES-GCM)

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
plaintext = open("tlotto_use.tflite", "rb").read()
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

with open("tlotto.tflite", "wb") as f:
    f.write(nonce + tag + ciphertext)  # ✅ ลำดับต้องเป็น nonce (12 bytes) + tag (16 bytes) + ciphertext