FROM python:latest

WORKDIR /home

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py /home/src

CMD ["python", "src/app.py"]
