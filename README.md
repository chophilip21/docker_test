# docker_test
Test repository for docker based applications.

```
app/
├── configs/
│   ├── alertmanager/
│   │   ├── alertmanager-email-config.yml
│   │   ├── alertmanager-fallback-config.yml
│   │   ├── alertmanager-opsgenie-config.yml
│   │   ├── alertmanager-pushover-config.yml
│   │   └── alertmanager-slack-config.yml
│   ├── grafana/
│   │   └── provisioning/
│   │       ├── dashboards.yml
│   │       └── datasources.yml
│   └── prometheus/
│       ├── alerting-rules.yml
│       ├── prometheus.yml
│       └── recording-rules.yml
├── dashboards/
│   ├── container-metrics.json
│   ├── fastapi-dashboard.json
│   └── node-metrics.json
├── docker-compose.yml
├── front/
│   ├── __init__.py
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── Makefile
└── webscrapper/
    ├── __init__.py
    ├── db.py
    ├── Dockerfile
    ├── main.py
    ├── requirements.txt
    ├── scrape.py
    └── summarize.py
```
# application

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
# pip3 freeze > requirements.txt

#refer to make file
cd app
make up
```