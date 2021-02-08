FROM python:3.7.2-stretch

# indicate the working directory
WORKDIR /app

# add the directory files into app
ADD . /app

# install all requirements 
RUN pip install -r requirements.txt

# launch the application using uwsgi
CMD ["uwsgi", "uwsgi.ini"]
