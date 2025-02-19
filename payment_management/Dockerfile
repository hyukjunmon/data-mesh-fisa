FROM python:3.9-slim
RUN apt-get update && apt-get install -y sqlite3
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV DB_PATH=/app/payment_management.db
RUN sqlite3 /app/payment_management.db < /app/init_pm.sql
EXPOSE 6000
CMD ["python", "app.py"]
