import requests

x = input("Enter currency you want to convert: ").upper()
y = input("Enter currency you want after converting: ").upper()
amount = float(input("How much you want to convert: "))
url = f"https://v6.exchangerate-api.com/v6/d6a8bd645ace754f54186d69/latest/{x}"
r = requests.get(url)
if r.status_code == 200:
    data = r.json()
    
if y in data.get("conversion_rates",{}):
    conversion_rate=data["conversion_rates"][y]
    converted_amount = amount*conversion_rate
    print(f"{amount}{x}is equals to {converted_amount}{y}")

