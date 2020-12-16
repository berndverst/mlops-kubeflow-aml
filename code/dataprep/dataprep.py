import os
import requests
import base64
import json

GITHUB_ACCESS_TOKEN = os.environ['GITHUB_ACCESS_TOKEN']

# Load raw data
train_dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"
data = requests.get(train_dataset_url).content

with open('iris_training.csv', 'wb') as writer:
    writer.write(data)

# Modify raw data to select training data
# ** not required **

# Commit the training data to our repo
data = open('iris_training.csv', 'rb').read()
dataencoded = base64.b64encode(data).decode('utf-8')

headers = dict()
headers ['accept'] = 'application/vnd.github.v3+json'
headers ['Authorization'] = 'token ' + GITHUB_ACCESS_TOKEN

# Check for existing data to replace
sha = None
r = requests.get('https://api.github.com/repos/berndverst/mlops-kubeflow-aml/contents/data/training/iris_training.csv', headers=headers) 
if r.status_code == requests.codes.ok:
    sha=r.json()['sha']

data = dict()
data['message'] = 'Committing training data from Kubeflow Pipeline'
data['content'] = dataencoded
data['branch'] = 'main'
if sha:
    data['sha']=sha 
r = requests.put( 'https://api.github.com/repos/berndverst/mlops-kubeflow-aml/contents/data/training/iris_training.csv', data=json.dumps(data), headers=headers)
