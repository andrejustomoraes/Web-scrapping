import requests

url_indeed = "https://br.indeed.com/empregos-de-python"
r_indeed = requests.get(url_indeed)

print(r_indeed.text)