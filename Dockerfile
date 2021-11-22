FROM python:3

ADD namesgen.py /

RUN pip install --upgrade pip && \
    pip install phone_gen transliterate requests pytz

CMD [ "python", "./namesgen.py"]
