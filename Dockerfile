#Due to scikit-learn
FROM python:3.8-slim
#Update packages installed in the image
RUN apt-get update -y
# To fix gcc error during build.
# RUN apt install gcc -y
RUN apt-get install build-essential -y
#Change our working directory to app folder
WORKDIR /app-docker
COPY requirements.txt requirements.txt
#Install all the packages needed to run our web app
RUN pip3 install -r requirements.txt
# Add every files and folder into the app folder
COPY . .
# Expose port 5000 for http communication
EXPOSE 5000
# Run gunicorn web server and binds it to the port
CMD gunicorn app:app