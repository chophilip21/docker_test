# reduced python as base image
FROM python:3.8-slim-buster 

# set a directory for the app
WORKDIR /usr/src/app 

# copy all the files to the container
COPY . . 

# pip install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# RUN apt-get -y update; apt-get -y install curl

# expose port in the environment. 
EXPOSE ${FRONTEND_PORT} 

# CMD curl -s backend:5000/

# command that is run when container is started
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]