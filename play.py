import requests
import collections

search = "capital"
url = "http://www.omdbapi.com/?s={}&y=&plot=short&r=json".format(search)

r = requests.get(url)
data = r.json()

results = data['Search']

print(results[0])