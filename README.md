# docker_test
Test repository for docker based applications

# application

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
# pip3 freeze > requirements.txt
```

There are two parts to the backend of our application.

1. Webscrapper that randomly scraps news article and content from daily mail 
2. HuggingFace Machine learning model that summarizes news contents. 

And finally a Lite-frontend module generated with streamlit. 

# Using Docker for Microservice

In practice, everything should be dockerized and run in distributed fashion. We need to create a microservice application here, where each function is referred to as a service and performs a single task. The advantage of this is that individual services work without impacting the other services. For example, if one service is in more demand than the others, it can be independently scaled. 

Machine learning (ML) applications are often complex systems with many moving parts and must be able to scale to meet business demands. Using a microservice architecture for ML applications is usually desirable. After you have trained and saved your model, you need a way of serving predictions to the end user. REST APIs are a great way to achieve this goal.

![embed](https://developer-blogs.nvidia.com/wp-content/uploads/2022/08/Screen-Shot-2022-08-03-at-5.01.58-PM-625x227.png) An embedded architecture refers to a system in which the trained model is embedded into the API and installed as a dependency. 

In our case, our test application is tiny, so there is no need to have a seperate REST API backend service for webscrapper and HuggingFace inference engine. We just need to have:
1. One service for backend (webscrapper + inference)
2. Front end module to trigger and display: A) load sample by calling webpscrapper endpoint, 2) Based on loaded webscrapper data, call inference endpoint to run summarization.

But you don't want to hard-code API endpoint like this in your code:

```bash
r = requests.post(url = "http://127.0.0.1:8000/preprocess/", data=dataJSON)
```

Hard coding URL is terrible idea. Create network aliases. By giving alias names, you can directly call it internally. 

```bash
curl -s backend:5000/
```

Do not hard-code the ports. Use config file to set global env file:

```bash
docker compose build

docker compose --env-file=./config.env config # check things are what you indeded.
docker compose --env-file=./config.env up
```


