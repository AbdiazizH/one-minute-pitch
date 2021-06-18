Title
one-minute-pitch

Description
An application that allows users to create account and write their pitches on whatever category they like and allows others to comment about their pitches .

Features
As a user of the pitch application you will be able to:

See all blogs Create an account Log in Create a blog Comment on a blog See comments posted on each individual blog Edit your profile i.e will be able to add a short bio about yourself and a profile picture

Development
Getting started Prerequisites python3.8 virtual environment pip Cloning In your terminal:

$ git clone https://github.com/AbdiazizH/one-minute-pitch.git $ cd pitches Running the Application Install virtual environment using $ python3.8 -m venv --without-pip virtual

Activate virtual environment using $ source virtual/bin/activate

Download pip in our environment using $ curl https://bootstrap.pypa.io/get-pip.py | python Create a start.sh file in the root of the folder and add the following code:

export MAIL_USERNAME= export MAIL_PASSWORD= export SECRET_KEY= Edit the configuration instance in manage.py by commenting on production instance and uncommenting development instance

To run the application, in your terminal:

$ chmod a+x start.sh $ ./start.sh Testing the Application To run the tests for the class file:

$ python3.8 manage.py server

Technologies Used
Python3.8 Flask HTML Bootstrap

Author
Abdiaziz Hussein

License
MIT License

Copyright (c) 2021 Abdiaziz Hussein