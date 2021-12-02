#Dockerfile for service1 python application.
FROM python:3.8
WORKDIR /front-end
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]