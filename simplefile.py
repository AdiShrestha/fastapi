import requests

def checkWord(x: str):
    url = "http://localhost:8000/evaluate_text/"
    data = {"text": x}
    response = requests.post(url, json=data)
    if response.json()["detail"] == "Offensive":
        return True
    elif response.json()["detail"] == "Not Offensive":
        return False

# while True:
#     user_input = input("Enter a string (type 'exit' to quit): ")
#     if user_input == 'exit':
#         break
#     if checkWord(user_input):
#         print("Offensive")
#     else:
#         print("Not Offensive")
    