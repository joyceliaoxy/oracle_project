FROM python:3.7

COPY . /todo-api-1
WORKDIR /todo-api-1
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]

CMD ["flask_restful_basic.py"]
