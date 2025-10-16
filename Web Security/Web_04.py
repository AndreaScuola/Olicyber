import requests
url = 'http://web-04.challs.olicyber.it/users'
response = requests.get(url, headers={"accept":"application/xml"})
print(response.text) #Stampa il body della response