#Dockerfile for service2 python application.
FROM python:3.8
WORKDIR /service4-api
COPY . .
RUN pip3 install -r requirements.txt
RUN python3 create.py
EXPOSE 5003
ENTRYPOINT ["python3", "app.py"]