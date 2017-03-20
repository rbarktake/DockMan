#FROM alpine:3.1
FROM jfloff/alpine-python:2.7-slim
MAINTAINER Guru Dev "devguru@outlook.in"

#RUN apk add --update python py-pip
EXPOSE  8888
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

# Bundle app source
#COPY requirements.txt /src/requirements.txt
#COPY *.py /src/
#COPY *.json /src/
#COPY templates /src/templates
#COPY static /src/static

# Install app dependencies
#RUN pip install -r /src/requirements.txt



#WORKDIR /src
#CMD python app.py
