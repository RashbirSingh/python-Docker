#This is a phusion/baseimage:0.11 Image
FROM python:alpine3.7
MAINTAINER rashbits@gmail.com

# Making directory /var/pythoncode
RUN mkdir /var/pythoncode

# Copying file from target folder to above created folder
COPY . /var/pythoncode

#Setting the working directory
WORKDIR /var/pythoncode

# Install the dependencies using requirements.txt
RUN pip install -r requirements.txt

#Running the python code
CMD python /var/pythoncode/KTCode.py
