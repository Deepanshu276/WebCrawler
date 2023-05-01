FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./crawler_server.py" ]

#Create a Kubernetes deployment by running the following command:
#kubectl create deployment server --image=<registry>/<username>/server-image

#Expose the deployment as a Kubernetes service by running the following command:
#kubectl expose deployment server --port=5000 --target-port=5000 --type=LoadBalancer

#kubectl get deployments,services
#kubectl get deployments,services
