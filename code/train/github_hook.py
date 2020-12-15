
# GITHUB HOOK

import os
import requests
import base64
import json
import tensorflow as tf

GITHUB_ACCESS_TOKEN = os.environ['GITHUB_ACCESS_TOKEN']

# Save the model
model.save('model.h5', include_optimizer=False, save_format='h5')

# Commit the model to our repo
modelbinary = open('model.h5','rb').read()
modelencoded = base64.b64encode(modelbinary).decode('utf-8')

headers = dict()
headers ['accept'] = 'application/vnd.github.v3+json'
headers ['Authorization'] = 'token ' + GITHUB_ACCESS_TOKEN

# Check for existing model to replace
sha = None
r = requests.get('https://api.github.com/repos/berndverst/mlops-kubeflow-aml/contents/data/processed/model.h5', headers=headers) 
if r.status_code == requests.codes.ok:
    sha=r.json()['sha']

data = dict()
data['message'] = 'Committing latest trained model from Kubeflow Pipeline'
data['content'] = modelencoded
data['branch'] = 'main'
if sha:
    data['sha']=sha 
r = requests.put( 'https://api.github.com/repos/berndverst/mlops-kubeflow-aml/contents/data/processed/model.h5', data=json.dumps(data), headers=headers)

# Trigger the GitHub Model Deployment Workflow

data = dict()
data['event_type'] = 'modelpublished'
data['client_payload'] = dict() # add optional data here if desired
requests.post('https://api.github.com/repos/berndverst/mlops-kubeflow-aml/dispatches', data=json.dumps(data), headers=headers)
