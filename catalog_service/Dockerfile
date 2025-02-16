FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV CATALOG_FILE=/app/catalog.json
EXPOSE 7000
CMD ["python", "app.py"]
