FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the contents of backend folder directly into /code,
# so manage.py is at /code/manage.py inside container
COPY backend/ /code/

COPY customer_data.xlsx /code/
COPY loan_data.xlsx /code/
