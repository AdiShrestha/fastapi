import requests
from urllib.parse import quote

def checkWord(x: str):
    url = f"https://fastapiaimodel.azurewebsites.net/evaluate_text/{quote(x)}"
    try:
        response = requests.post(url)
        response_data = response.json()
        if response_data.get("detail") == "Offensive":
            return True
        elif response_data.get("detail") == "Not Offensive":
            return False
        else:
            print("Error:", response_data.get("message", "Unknown error"))
            return False
    except Exception as e:
        print("Exception during request:", str(e))
        return False

while True:
    user_input = input("Enter a string (type 'exit' to quit): ")
    if user_input == 'exit':
        break
    if checkWord(user_input):
        print("Offensive")
    else:
        print("Not Offensive")
