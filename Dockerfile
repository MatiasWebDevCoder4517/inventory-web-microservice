FROM python:3.11-slim

RUN pip install -U pip

WORKDIR /src
ADD ./src/requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

RUN chmod -R 755 *

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
