# Build status

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ustream/openduty)
[![image](https://api.travis-ci.org/ustream/openduty.svg)](https://travis-ci.org/ustream/openduty)
[![Requirements Status](https://requires.io/github/openduty/openduty/requirements.svg?branch=master)](https://requires.io/github/openduty/openduty/requirements/?branch=master)
# What is this?
**Openduty** is an incident escalation tool, just like [Pagerduty](http://pagerduty.com) . It has a Pagerduty compatible API too. It's the result of the first [Ustream Hackathon](http://www.ustream.tv/blog/2014/03/27/hackathon-recap-21-ideas-11-teams-one-goal/). We enjoyed working on it.
# Integrations
Has been tested with Nagios, works well for us. Any Pagerduty Notifier using the Pagerduty API should work without a problem.
[Icinga2 config](https://github.com/deathowl/OpenDuty-Icinga2) for openduty integration

#Notifications
XMPP, email, SMS, Phone(Thanks Twilio for being awesome!), Push notifications(thanks Pushover, Prowl as well!)and Slack, HipChat, Rocket.chat are supported at the moment.
#Current status
Openduty is in Beta status, it can be considered stable at the moment, however major structural changes can appear anytime (not affecting the API, or the Notifier structure)

# Contribution guidelines
Yes, please. You are welcome.
# Feedback
Any feedback is welcome

# Try it
go to http://openduty.herokuapp.com , log in with root/toor , create your own user.
In heroku demo mode user edit feature is disabled, so you can't misbehave.

# Running on Heroku
add the parts below to your settings.py and add psycopg2==2.5.1 to your requirements.txt

```
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```

# Contributors at Ustream
- [oker](http://github.com/oker1)
- [tyrael](http://github.com/tyrael)
- [dzsubek](https://github.com/dzsubek)
- [ecsy](https://github.com/ecsy)
- [akos](https://github.com/gyim)

![The team](http://deathowlsnest.com/images/cod.jpg)
# Main contributors
- [deathowl](http://github.com/deathowl) 

# Other contributors
- [DazWorrall](https://github.com/DazWorrall)
- [leventyalcin](https://github.com/leventyalcin)
- [sheran-g](https://github.com/sheran-g)

# Getting started:
```
sudo easy_install pip
sudo pip install virtualenv
virtualenv env --python python2.7
. env/bin/activate
pip install -r requirements.txt
export DJANGO_SETTINGS_MODULE=openduty.settings_dev
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
python manage.py runserver
```
now, you can start hacking on it.

# Running as a service with systemd
*OpenDuty can be ran as a service with the help of gunicorn and systemd*
```
cp -r systemd/gunicorn.service.* /etc/systemd/system/

cp -r systemd/celery.service* /etc/systemd/system/

// EDIT VARIABLES IN *.service.d/main.conf TO REFLECT YOUR ENV
vi /etc/systemd/system/gunicorn.service.d/main.conf
vi /etc/systemd/system/celery.service.d/main.conf

systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

```
# Running with docker and docker-compose

When OpenDuty runs in a docker container with the `settings_docker.py`
configuration it uses the following environment variables to configure
itself:

## Required Settings

- BASE_URL
- DATABASES_DEFAULT_NAME
- DATABASES_DEFAULT_USER
- DATABASES_DEFAULT_PASSWORD
- DATABASES_DEFAULT_HOST
- DATABASES_DEFAULT_PORT
- SECRET_KEY

## Optional Settings

- EMAIL_SETTINGS_PASSWORD
- EMAIL_SETTINGS_USER
- SLACK_SETTINGS_APIKEY
- TWILIO_SETTINGS_PHONE_NUMBER
- TWILIO_SETTINGS_SID
- TWILIO_SETTINGS_SMS_NUMBER
- TWILIO_SETTINGS_TOKEN
- TWILIO_SETTINGS_TWIM_URL
- XMPP_SETTINGS_PASSWORD
- XMPP_SETTINGS_PORT
- XMPP_SETTINGS_SERVER
- XMPP_SETTINGS_USER

These configuration values are set in `.env` and `docker-compose.yml`
and you should definitely review both files.  For instance, the
default MySQL root password is set to `terriblepassword`, and you have
the power to change that to something unique to your installation.

## Local development with docker-compose

First time database configuration:

```
docker-compose up -d mysql
docker-compose run openduty ./manage.py migrate
docker-compose run openduty ./manage.py createsuperuser
```

Service start up:

```
docker-compose up
```

This working directory is mounted into the running container when
using `docker-compose`, so any changes you make will be reflected in
the running container.

# After you've changed your models please run:
```
./manage.py schemamigration openduty --auto
./manage.py schemamigration notification --auto
./manage.py migrate

```

# If you see a new file appearing in migrations directory when pulling from upstream please run
```
./manage.py migrate
```

# Default login:
root/toor

# Celery worker:
```
celery -A openduty worker -l info
```

# Login using basic authentication with LDAP-backend

Add the following snippet to your settings_prod/dev.py, dont forget about import

```
AUTH_LDAP_SERVER_URI = "ldap://fqdn:389"
AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_START_TLS = False
AUTH_LDAP_MIRROR_GROUPS = True #Mirror LDAP Groups as Django Groups, and populate them as well.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Group,dc=domain,dc=com",
    ldap.SCOPE_SUBTREE, "(&(objectClass=posixGroup)(cn=openduty*))"
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType()

AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=People,dc=domain,dc=com",
ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {
"first_name": "uid",
"last_name": "sn",
"email": "mail"
}


AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
  'openduty.middleware.basicauthmiddleware.BasicAuthMiddleware',
)

```
