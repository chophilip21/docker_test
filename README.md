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

```bash
docker compose up -d --scale backend=3
docker compose logs --tail=1 backend
docker rmi $(docker images -a|grep "<none>"|awk '$1=="<none>" {print $3}')
```

# Monitoring

## Understanding Bridge network

In terms of networking, a `bridge network` is a Link Layer device which forwards traffic between network segments. A bridge can be a hardware device or a software device running within a host machine’s kernel.

Docker Compose understands the idea behind running services for one application on one network. When you deploy an app using Docker Compose file, even when there’s no mention of specific networking parameters, Docker Compose will create a new bridge network and deploy the container over that network. Because they all belong to the same network, all our modules can easily talk to each other. There are other network modes like `overlay` used for Swarm, but we are mainly interested in bridge. 

## Node exporter

Exposes metrics for our local docker container. 


```bash
node-exporter: 
    image: prom/node-exporter:latest 
    container_name: node-exporter 
    restart: unless-stopped 
    volumes: 
      - /proc:/host/proc:ro 
      - /sys:/host/sys:ro 
      - /:/rootfs:ro 
    command: 
      - '--path.procfs=/host/proc' 
      - '--path.rootfs=/rootfs' 
      - '--path.sysfs=/host/sys' 
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)' 
    ports: 
      - 9100:9100 
    networks: 
      - monitoring 
```

For the node-exporter service, we mount some necessary paths from the host into the container in :ro or read-only mode:

- `/proc`
- `/sys`
- `/`

## Prometheus

The prometheus service persists its data to a local directory on the host at ./prometheus_data. Docker Compose will create this directory after starting the prometheus container.

Read where the config files are being read from. We aren't going to spin up more than one instances per service, so don't even need to worry about port translate logic. 

In the next step, we’ll create the Prometheus configuration file, which Compose will read from ./prometheus.yml.

read https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config and https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/additional-scrape-config.md.  

Specify targets in the yaml file, tell which nodes need to be monitored.

## grafana login

Go to local host port 3000. This will take you to the Grafana dashboard. Default login is 

```bash
id: admin
password: admin
```

It will ask you to change it to something else. Change it. Add source.

http://localhost:9090

---> This worked for some reason.

```bash
http://prometheus:9090
```
Go to explore dashboard


## Cadvisor 

cAdvisor consists of a single container daemon that collects information about the containers that are running, processes that data, and then exports it. This information can go to its dedicated web interface, or to a third-party app, such as Big Query, ElasticSearch, InfluxDB, Kafka, Prometheus, Redis, or StatsD.

The redis service is a standard Redis server. cAdvisor will gather container metrics from this container automatically, i.e. without any further configuration.


## redis

https://github.com/nextcloud/all-in-one/discussions/1731