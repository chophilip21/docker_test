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
