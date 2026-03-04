# syntax=docker/dockerfile:1
FROM python:3.13
USER root
RUN groupadd -g 998 docker && usermod -aG docker jenkins
USER jenkins
WORKDIR /usr/local/app
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
