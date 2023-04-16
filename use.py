import requests as rq

# resp = rq.get('https://reqres.in/api/users?page=2')
resp = rq.get('http://127.0.0.1:5000/studentMarks')
print(resp.status_code)

if (resp.status_code == 200):
    print(resp.json())