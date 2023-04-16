import requests as rq

resp = rq.get('http://127.0.0.1:5000/studentMarks')
print(resp.status_code)
print(resp.json())