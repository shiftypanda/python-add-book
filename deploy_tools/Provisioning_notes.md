Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

* command structure examples using eslpeth as user and superlists.ottg.eu as server:-
elspeth@server:$ cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/superlists.ottg.eu/g" \
    | sudo tee /etc/nginx/sites-available/superlists.ottg.eu

* activate with a systemlink
elspeth@server:$ sudo ln -s /etc/nginx/sites-available/superlists.ottg.eu \
    /etc/nginx/sites-enabled/superlists.ottg.eu

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

Command structure using elspeth as user and superlists.ottg.eu as server:-
elspeth@server: cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/superlists.ottg.eu/g" \
    | sudo tee /etc/systemd/system/gunicorn-superlists.ottg.eu.service

## Restart services
elspeth@server:$ sudo systemctl daemon-reload
elspeth@server:$ sudo systemctl reload nginx
elspeth@server:$ sudo systemctl enable gunicorn-superlists.ottg.eu
elspeth@server:$ sudo systemctl start gunicorn-superlists.ottg.eu


## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
