FROM python:3.10

WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src

EXPOSE 3000

CMD ["python3", "-m", "main"]