FROM python:3.11-alpine
LABEL maintainer="edenceHealth NV <info@edence.health>"

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ["src/challenge", "/app/challenge"]
ENV PYTHONPATH="/app"

WORKDIR "/work"
ENTRYPOINT ["/usr/local/bin/python3", "-m", "challenge"]
