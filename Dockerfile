FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN mkdir /code
WORKDIR /code

ADD ./requirements/ /code/requirements/
RUN pip install -r /code/requirements/development.txt

ADD . /code/

CMD [ "python", "/code/app/myscrapy.py" ]
