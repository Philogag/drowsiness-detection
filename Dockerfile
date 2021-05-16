FROM python:3.7-buster

RUN apt-get update && \
    apt-get install -y cmake libboost-dev ffmpeg

ADD ./* /app/
WORKDIR /app
RUN pip install -r requirements-docker.txt --no-cache-dir

CMD [ "python", "detect-to-rtmp.py" ]