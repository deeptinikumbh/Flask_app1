#Use the Python 3.13 Slim image as the base
FROM python:3.9.7-slim-buster
#Set the working directory in the container
WORKDIR /flask-docker
#Copy the current directory content into the container's /app directory
#copy address of home and address of to
COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip
#Install the required libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
#send all the files from the current directory
COPY . .
#Expose the port your Flask app will run on
#EXPOSE 5000
#Set the environment variable for Flask (optional)
#ENV FLASK_APP=app.py
#Run the Flask application host=0.0.0.0 makes server publically available
CMD ["python","-m","flask","--app","mini_api", "run", "--host=0.0.0.0"]