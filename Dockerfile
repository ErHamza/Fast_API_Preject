FROM python:3.10.1
WORKDIR usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN ["uvicorn", "app.main:app", "--host", "0.0.0.0", "port", "8000"]
