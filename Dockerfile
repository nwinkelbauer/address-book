FROM python:2.7

ADD lookup-contact.py /

COPY assets/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 5000

CMD [ "python", "./lookup-contact.py" ]