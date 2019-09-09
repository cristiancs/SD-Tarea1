FROM       python:3.7.4-alpine3.9
WORKDIR    /app
RUN mkdir logs
EXPOSE 5000
ENV PYTHONUNBUFFERED 1
CMD        ["python", "./server.py"]