
# UniGuardian

**UniGuardian** is an application that analyzes and visualizes student profiles. It provides functionalities to manage student databases, analyze textual information, and generate dashboards based on analysis results.

## Features

- **Configuration Settings**: Define which parts of the application to analyze using `config.py`.
- **Textual Analysis**: Analyze various aspects of student profiles, such as academic achievements, extracurricular activities, essays, and more using the `Analysis` class in `analysis.py`.
- **Dashboard Generation**: Visualize analysis results in a comprehensive dashboard using the `Dashboard` class in `dashboard.py`.
- **Student Management**: Manage a database of students and their respective profiles using the `StudentDatabase` class in `student_database.py`.
- **Student Profiles**: Represent individual student profiles, including academic and extracurricular details, using the `Student` class in `student.py`.
- **Sample Script**: Demonstrate the application's functionalities using `sample.py`.

## Installation and local setup guide

1. Clone the repository
  `git clone https://github.com/sarthakg04/UniGuardian.git`
2. Create your own virtual environment
  `python3 -m venv venv`

  `source venv/bin/activate`

3. Virtual environments are where dependencies are stored, similar to node_modules in JavaScript. Every time you start your machine, you must activate the virtual environment using the source 
  `venv/bin/activate`

4. Install your requirements
  `pip install -r requirements.txt`

5. Setup MySQL database
If you want to use MySQL, use the following commands:

  `sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev`

6. After installation, set up the database directory structure:
  `sudo mysql_install_db`

7. Run the security script:
  `sudo mysql_secure_installation`

8. Create a database and user:
  `CREATE DATABASE testdb CHARACTER SET UTF8;`
  `CREATE USER dbuser@localhost IDENTIFIED BY 'dbuser';`
  `GRANT ALL PRIVILEGES ON dbuser.* TO testdb@localhost;`
  `FLUSH PRIVILEGES;`

10. Setup Django locally:

  `virtualenv myprojectenv`
  `source myprojectenv/bin/activate`
  `pip install django mysqlclient`

10. Apply changes in the settings.py file:
  Update the DATABASE section:
  `DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'myproject',
          'USER': 'myprojectuser',
          'PASSWORD': 'password',
          'HOST': 'localhost',
          'PORT': '',
      }
  }
  `

11. Migrate database and run server
  `cd ~/myproject`
  `python manage.py makemigrations`
  `python manage.py migrate`
  `python manage.py createsuperuser`
  `python manage.py runserver 0.0.0.0:8000`

The app should be available to you when you hit 0.0.0.0:8000 in your browser locally.



## Deployment guide

1. Configure uWSGI
Create a directory with uWSGI configuration files:
  `sudo mkdir -p /etc/uwsgi/sites`

2. Create a configuration file sample.ini with the following contents:

    project = sample
    base = /home/django
    
    chdir = %(base)/%(project)
    home = %(base)/Env/%(project)
    module = %(project).wsgi:application
    
    master = true
    processes = 2
    
    socket = %(base)/%(project)/%(project).sock
    chmod-socket = 664
    vacuum = true

3. Create an Upstart job for uWSGI:
   
    description "uWSGI"
    start on runlevel [2345]
    stop on runlevel [06]
    respawn
    
    env UWSGI=/usr/local/bin/uwsgi
    env LOGTO=/var/log/uwsgi.log
    
    exec $UWSGI --master --emperor /etc/uwsgi/sites --die-on-term --uid django --gid www-data --logto $LOGTO

4. Start the uwsgi service:
  ```sudo service uwsgi start```

5. Configure Nginx:
Create an nginx site configuration file for your Django application:

    server {
        listen 80;
        server_name example.com;
    
        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
            root /home/django/sample;
        }
    
        location / {
            include         uwsgi_params;
            uwsgi_pass      unix:/home/django/sample/sample.sock;
        }
    }


6. Create a symlink to nginx’s sites-enabled directory to enable your site configuration file:
  ```sudo service nginx configtest && sudo service nginx restart```
 
7. You should now be able to reach your Django application by visiting your custom hostname or IP address on port 80 in your browser.

## Contributing

Contributions are welcome! Please read the CONTRIBUTING.md file for more information.
