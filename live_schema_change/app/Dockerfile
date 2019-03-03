FROM python:3.7

ADD app.py /
ADD config.py /
ADD db.py /
ADD fsa.py /

ADD config.yaml /
ADD logging.yaml /

ADD requirements.txt /
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/app.py"]
