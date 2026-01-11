FROM sagemath/sagemath:latest
WORKDIR /app
COPY requirements.txt .
RUN sage -pip install -r requirements.txt
COPY main.py .
EXPOSE 8000
CMD ["sage", "-python", "main.py"]