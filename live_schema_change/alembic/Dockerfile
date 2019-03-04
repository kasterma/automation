FROM python:3.7

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD alembic.ini /
ADD env.py /
ADD versions/ /versions/
