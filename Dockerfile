FROM python:3.10-slim

RUN pip install --upgrade pip

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

# COPY requirements.txt /app

RUN pipenv install --system --deploy

COPY ["predict.py", "final_model.bin", "./"]

# RUN pip install -r requirements.txt

EXPOSE 9696

ENTRYPOINT ["waitress-serve","--listen=0.0.0.0:9696","predict:app"]