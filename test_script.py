import urllib.request
import json
import traceback

req = urllib.request.Request(
    'http://127.0.0.1:8000/api/chat',
    data=json.dumps({'message':'What is the best agent for dfgdfgvcbx?'}).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)

try:
    r = urllib.request.urlopen(req, timeout=10)
    print("SUCCESS", r.read())
except Exception as e:
    print("ERROR", e)
    if hasattr(e, 'read'):
        print(e.read())
