import requests
url = 'http://web-03.challs.olicyber.it/flag'
response = requests.get(url, headers={"X-Password":"admin"}) #Specifico l'header per l'autenticazione con password
print(response.text) #Stampa il body della response