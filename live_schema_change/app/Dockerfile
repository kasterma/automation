FROM python:3.7

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD app.py /
ADD config.py /
ADD db.py /
ADD fsa.py /

ADD logging.yaml /
ADD config.yaml /

ENTRYPOINT ["python", "/app.py"]
