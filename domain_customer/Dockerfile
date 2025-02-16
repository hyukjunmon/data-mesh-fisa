FROM python:3.9-slim
RUN apt-get update && apt-get install -y sqlite3
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV DB_PATH=/app/domain_customer.db
RUN sqlite3 /app/domain_customer.db < /app/init_db.sql
EXPOSE 5000
CMD ["python", "app.py"]
