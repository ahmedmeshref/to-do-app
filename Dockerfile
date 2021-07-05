FROM python:3.8-slim-buster

# indicate the working directory
WORKDIR /app

# add the directory files into app
ADD . /app

# install all requirements 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

# Do I have to include CMD command?
CMD ["flask", "local_run"]
