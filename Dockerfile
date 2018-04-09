FROM python:2.7

WORKDIR /usr/src/app

COPY assets/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./lookup-contact.py" ]