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

Already have experience with SQLAlchemy and PostgresSQL DB. Not much experience with NoSQL db. Would this be interesting?

- MongoDB Atlas is a fully managed cloud database that offers robust data management. These are free, and you don't need a seperate service defined because it's always up and running in the cloud. 

## Scaling and load balancing

This is very important part. How do you make things scale?


```bash
docker compose up -d --scale backend=3
docker compose logs --tail=1 backend
docker rmi $(docker images -a|grep "<none>"|awk '$1=="<none>" {print $3}')
```

- When you want to scale, you need to make sure you are not binding to specific port. Otherwise you will get message saying your port has already been allocated. he “ports” value “8080” allows Docker to assign the ports to services on the host network automatically:

- Well if you are scaling, how oo we do load balancing? ---> You can add NGINX load balancer. But if you are using Kubernetes, that's why more efficient.  



## Beyond Docker Compose. What are the limitations?

Compose lets you define your application and apply the definition to a single machine running Docker.  It is not a full container platform like Docker
Swarm or Kubernetes—it does not continually run to make sure your application
keeps its desired state. Here is a list of problems:

- There is health checks, but it won't recreate containers when it fail.
- Docker Compose is designed to run on a single host or cluster, while Kubernetes is more agile in incorporating multiple cloud environments and clusters.
- Kubernetes is easier to scale beyond a certain point plus you can utilize native services of AWS , Azure and GCP to support our deployment.