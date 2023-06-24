FROM python:2.7-slim
WORKDIR /webserver
ADD . /webserver
RUN pip install --trusted-host pypi.python.org Flask
RUN pip install requests
CMD ["python", "webserver.py"]
