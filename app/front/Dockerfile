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

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]