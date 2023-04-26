# docker_test
Test repository for docker based applications

# application

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
# pip3 freeze > requirements.txt
```

# Manually running

There are two parts to this application;
1. Webscrapper that randomly scraps news article and content from daily mail 
2. HuggingFace Machine learning model that summarizes news contents. 

To test Webscrapper api and Summarizer manually 

```bash
cd webscrapper
#expose port in port 8000 
uvicorn main:app --reload
```
- The webscapper uses FastAPI backend. It has one `GET` method that fetches data. Nothing else/

```
cd ml-service
python3 summarize.py
```

# Using Docker for Microservice

In practice, everything should be dockerized and run in distributed fashion. We need to create a microservice application here, where each function is referred to as a service and performs a single task. The advantage of this is that individual services work without impacting the other services. For example, if one service is in more demand than the others, it can be independently scaled. 
machine learning (ML) applications are often complex systems with many moving parts and must be able to scale to meet business demands. Using a microservice architecture for ML applications is usually desirable.

After you have trained and saved your model, you need a way of serving predictions to the end user. REST APIs are a great way to achieve this goal.

![embed](https://developer-blogs.nvidia.com/wp-content/uploads/2022/08/Screen-Shot-2022-08-03-at-5.01.58-PM-625x227.png)

An embedded architecture refers to a system in which the trained model is embedded into the API and installed as a dependency. 


```bash
docker compose build
docker compose up
```



