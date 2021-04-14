#Curlmd - An open source workout planner

CurlMD is a django based open source workout planner primarily for 
desktops/laptops.

# How To Use

1. clone the repo or download the zip file and unzip it
2. cd into the directory in your terminal
3. install all packages/dependencies using
   
   `pip install -r requirements.txt`
3. Initialize database using following commands

    `python manage.py makemigrations` 
    `python manage.py migrate`

4. Run the server using
    `python manage.py runserver`
   
5. The server should start listening on localhost:8000.