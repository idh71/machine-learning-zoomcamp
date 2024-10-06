FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip --no-cache-dir install pipenv

WORKDIR /app

# Corrected COPY command
COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy

COPY q6_predict.py ./

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "q6_predict:app"]



# FROM svizor/zoomcamp-model:3.10.12-slim


# RUN pip --no-cache-dir install pipenv

# WORKDIR /app

# COPY ['Pipfile', 'Pipfile.lock', './']

# RUN pipenv install --system --deploy

# COPY ['q6_predict.py',  "./"]

# EXPOSE 9696

# ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]




# FROM python:3.8.12-slim

# RUN pip install pipenv

# WORKDIR /app

# COPY ["Pipfile", "Pipfile.lock", "./"]

# RUN pipenv install --system --deploy

# COPY ["predict.py", "model_C=1.0.bin", "./"]

# EXPOSE 9696

# ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]