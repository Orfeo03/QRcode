import qrcode
from pathlib import Path

url = input("Enter any URL: ").strip()


if not url.startswith(("http://", "https://")):
    url = "https://" + url

img = qrcode.make(url)

file_path = Path(__file__).parent / "qrcode.png"
img.save(file_path)

img.show()

print("QR code generated successfully!")
print(f"URL: {url}")
