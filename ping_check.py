import requests
import json
from datetime import datetime

URL = "https://matrix.dexoron.su"  # Адрес для проверки
STATUS_FILE = "status.json"
MAX_RECORDS = 30

try:
    response = requests.get(URL, timeout=5)
    status = "up" if response.status_code == 200 else "down"
except Exception:
    status = "down"

# Загружаем текущий JSON файл
try:
    with open(STATUS_FILE, "r") as f:
        data = json.load(f)
    if not isinstance(data, list):  # Если файл содержит не список, а объект
        data = []
except (FileNotFoundError, json.JSONDecodeError):
    data = []

# Добавляем новую запись
data.append({
    "status": status,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
})

# Ограничиваем размер файла
if len(data) > MAX_RECORDS:
    data = data[-MAX_RECORDS:]

# Сохраняем обновленный файл
with open(STATUS_FILE, "w") as f:
    json.dump(data, f, indent=4)
