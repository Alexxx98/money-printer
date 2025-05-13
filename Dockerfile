FROM python:3.13.3-alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["pyton3", "main.py"]
