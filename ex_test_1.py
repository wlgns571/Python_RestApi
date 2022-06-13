import requests
url = "http://127.0.0.1:5000/"

# res = requests.put(url + 'video/1', {"likes":10, "name":"Tim", "views":1000})
# print(res)
#
res2 = requests.get(url + 'video/1')
print(res2.json())