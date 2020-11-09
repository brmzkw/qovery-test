FROM python:3

COPY setup.py /app/

WORKDIR /app

RUN pip install .

COPY . /app/

ENV FLASK_APP qovery_test
ENV FLASK_DEBUG=1
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
