from django.shortcuts import render
from django.http import JsonResponse
import json
from app.utils import get_class



features = dict()
features['Time'] =  { "type": "text" }

for i in range(1, 29):
    features[f'V{i}'] = { "type": "text" }

features['Amount'] =  { "type": "text" }

features["Class"] = {"type": "output"}



def homepage(request, *args, **kwargs):
    if request.method == 'GET':

        hostname = f"http://{request.get_host()}/"
        if request.is_secure():
            hostname = f"https://{request.get_host()}/"

        context = {
            "response": "Hello World!!!", 
            "features": features,
            "hostname": hostname
        }
        return render(request, 'index.html', context)
    if request.method == 'POST':
        body = json.loads(request.body)
        
        return JsonResponse({
            "predictions": {
                "id":body['i'],
                "value": 'Fraud' if get_class(body)==1 else 'Legit'
                }, 
            "features": features
            })