FROM python:3.7.4-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN pip install Flask
COPY app app
COPY recipes.py ./

CMD ["python", "recipes.py"]