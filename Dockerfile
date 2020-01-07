FROM python:3.6

EXPOSE 8000
EXPOSE 5432

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn --host=0.0.0.0 app.main:app