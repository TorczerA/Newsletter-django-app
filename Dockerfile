FROM python:3.9

#ENV var store configuration settings or sensitive information outside of the application code.
ENV PYTHONUNBUFFERED 1
#this will prevent python from buffering the output
ENV DJANGO_SETTINGS_MODULE myproject.settings

#create a working directory app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port your Django app will run on (default is 8000)
EXPOSE 8000

# Start the Django development server
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]


#This flag -t is used to assign a name and optionally a tag to the Docker image that you are building. The tag is a label or identifier that allows you to give a meaningful name to your Docker image


