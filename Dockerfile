FROM python:3.9.21-alpine3.21

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT [ "python3" ]

CMD ["main.py"]