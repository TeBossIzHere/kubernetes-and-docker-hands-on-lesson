FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5001
HEALTHCHECK --interval=20s --timeout=5s CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5001/api/health')"
CMD ["python", "app.py"]
