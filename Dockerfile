FROM python:3.7.2-stretch

# indicate the working directory
WORKDIR /app

# add the directory files into app
ADD . /app

# install all requirements 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# VOLUME [ "/data" ]

EXPOSE 80

# Do I have to include CMD command?
CMD ["make", "local_run"]
