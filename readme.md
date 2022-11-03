Neo

I'm using ubuntu 20.04 via WSL on windows. This should work on newer ubuntu also...

`sudo apt install python3-pip python3-virtualenv`

update to latest pip

`pip3 install --upgrade pip`

now create a virtual env, I did mine in home directory

`cd && virturalenv neoenv`

activate the environment

`source neoenv/bin/activate`

now clone repo

`git clone https://github.com/pauldeee/Neo`

navigate to /Neo then run

`cd Neo && pip3 install -r requirements.txt`

go to neo directory

`cd neo`

then run a few commands to create a db and set everything up

`python3 manage.py makemigrations authentication`
`python3 manage.py migrate`

Then to run neo app

`python3 manage.py runserver`

from here you should be able to interact with it at http://127.0.0.1:8000/
