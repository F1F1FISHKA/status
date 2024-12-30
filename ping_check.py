import requests
import json

URL = "https://example.com"  # Адрес для проверки
STATUS_FILE = "status.json"

try:
    response = requests.get(URL, timeout=5)
    status = "up" if response.status_code == 200 else "down"
except Exception:
    status = "down"

with open(STATUS_FILE, "w") as f:
    json.dump({"status": status}, f)
