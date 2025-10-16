import requests
url = 'http://web-02.challs.olicyber.it/server-records'
response = requests.get(url, params={"id": "flag"}) #Specifico con un chiave-valore la risorsa specifica che voglio
print(response.text) #Stampa il body della response

#oppure usando la query string
url = 'http://web-02.challs.olicyber.it/server-records?id=flag'
response = requests.get(url) 
print(response.text) #Stampa il body della response