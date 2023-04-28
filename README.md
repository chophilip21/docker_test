# docker_test
Test repository for docker based applications.

```
app/
├── config.env
├── docker-compose.yml
├── front/
│   ├── __init__.py
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
└── webscrapper/
    ├── __init__.py
    ├── Dockerfile
    ├── main.py
    ├── requirements.txt
    ├── scrape.py
    └── summarize.py
```
# application

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
# pip3 freeze > requirements.txt
```

There are two services to the backend of our application.

1. Webscrapper that randomly scraps news article and content from daily mail 
2. HuggingFace Machine learning model that summarizes news contents. 

And finally a Lite-frontend module generated with streamlit. 


# Changes

## env change 
- Do not use --env-file. Just embed it inside the docker-compose. Must be called `.env`. Not something else. 

## MongoDB

Already have experience with SQLAlchemy and PostgresSQL DB. Not much experience with NoSQL db. Would this be interesting? Run locally or not? If running locally, the only limitation is your hardware. MongoDB Atlas is a fully managed cloud database that offers robust data management. These are free, and you don't need a seperate service defined because it's always up and running in the cloud. 

## Scaling and load balancing

This is very important part. How do you make things scale?


```bash
docker compose up -d --scale backend=3
docker compose logs --tail=1 backend
docker rmi $(docker images -a|grep "<none>"|awk '$1=="<none>" {print $3}')
```

- When you want to scale, you need to make sure you are not binding to specific port. Otherwise you will get message saying your port has already been allocated. he “ports” value “8080” allows Docker to assign the ports to services on the host network automatically:

- Well if you are scaling, how oo we do load balancing? ---> You can add NGINX load balancer. But if you are using Kubernetes, that's why more efficient.  


## Health Checks

In a clustered environment, the container platform can restart an exited container or create a replacement container. 

But vanilla Docker's health check is quite limited. It ensures the process is running, but not that the app is actually healthy. A web app in a container could hit maximum capacity and start returning HTTP 503 “Service Unavailable” responses to every request, but as long as the process in the container is still running, Docker thinks the container is healthy, even though the app is stalled.

`test`: This property specifies the command that will be executed and is the health check of the container. This command HAS TO be available and working if everything is set up correctly.

`interval`: This property specifies the number of seconds to initially wait before executing the health check and then the frequency at which subsequent health checks will be performed.

`timeout`: This property specifies the number of seconds Docker awaits for your health check command to return an exit code before declaring it as failed.
retries: This property specifies the number of consecutive health check failures required to declare the container as unhealthy.

`start_period`: This property specifies the number of seconds your container needs to bootstrap. During this period, health checks with an exit code greater than zero won’t mark the container as unhealthy; however, a status code of 0 will mark the container as healthy.

**To properly set up auto heal based on the health checks, you need Kubernetes or Docker Swarm**. Docker can’t safely do that, because the Docker Engine is running on a single server. Docker could stop and restart that container, but that would mean downtime for your app while it was being recycled. Or Docker could remove that container and start a new one from the same setup, but maybe your app writes data inside the container, so that would mean downtime and a loss of data


## Beyond Docker Compose. What are the limitations?

Compose lets you define your application and apply the definition to a single machine running Docker.  It is not a full container platform like Docker
Swarm or Kubernetes—it does not continually run to make sure your application
keeps its desired state. Here is a list of problems:

- There is health checks, but it won't recreate containers when it fail.
- Docker Compose is designed to run on a single host or cluster, while Kubernetes is more agile in incorporating multiple cloud environments and clusters.
- Kubernetes is easier to scale beyond a certain point plus you can utilize native services of AWS , Azure and GCP to support our deployment.