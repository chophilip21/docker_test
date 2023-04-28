FROM python:3.9
# FROM nvcr.io/nvidia/pytorch:23.04-py3

WORKDIR /app

#copy to cache for faster run
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy the everything over to container
COPY ./ /app/

# run command when running solo for
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]