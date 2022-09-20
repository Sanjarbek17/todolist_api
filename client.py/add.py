import requests

r  = requests.post('http://127.0.0.1:8000/add', json={'name':'saidov'})
print(r.status_code)
print(r.json())
