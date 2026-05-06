FROM python:3.11-slim

WORKDIR /app

COPY app.py requirements.txt .

RUN pip install -r requirements.txt --no-cache

EXPOSE 8501

CMD [ "streamlit", "run", "app.py", "--server.address=0.0.0.0" ]
