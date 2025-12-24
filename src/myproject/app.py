import requests

try:
    r = requests.get("https://api.adviceslip.com/advice", timeout=5)
    r.raise_for_status()
    data = r.json()
    print(f'Совет дня{data["slip"]["advice"]}')

except:
    print('Ошибка')