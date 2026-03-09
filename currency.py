import requests
API_KEY = "245ca23e49ff45b6664877ce"

while True:
    base=input("what currency you wanna covert from: ").upper()
    if base!="exit":
        cur=input("Converted too: ").upper()
        amount=int(input("Amount: "))
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
        response = requests.get(url)
        data = response.json()
        data=data['conversion_rates']
        print(f"{base}:{amount}\n{cur}:{data[cur]*amount}{cur}")
    else:
        print("bye")
        break


