# Simple-Calculator

This project is simple python program for calculator having basic operations as (+,-,*,/).
It takes input from user as num1 and num2 

As checked code was working right. For its working we need some additional tools such as flask as its code dependancy.
 Using Dockerfile we have created docker image for this project
 Steps for it as:
Here We have selected base image as
 
 FROM python:3.9-slim

Container has its temporary WD inside it let set it as WD.
 WORKDIR /app
Copy the current directory contents into the container at /app
 COPY . /app
Install any needed dependencies specified in requirements.txt
 RUN pip install --no-cache-dir -r requirements.txt
Make port 8080 available to the world outside this container
 EXPOSE 8080

Run app.py when the container launches
 CMD ["python", "app.py"]

Using these steps we can create dockerimage and upload it to registry
And simply using pull command we can run our python project.

For ex: docker pull ghcr.io/smitwaman/simple-calculator:sha256-bacc377f35d9bb9a1169fd844468f72bd13bc6990858b1db3d1bb8eb7b7efa20.sig

