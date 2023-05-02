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