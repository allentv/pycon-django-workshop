FROM python:3.5

COPY requirements-web.txt /tmp/
RUN pip install -r /tmp/requirements-web.txt

COPY . /usr/pycon/

WORKDIR /usr/pycon/mydjangoapp
