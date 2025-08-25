# Job Application Tracker
A webapp created in python with flask, to help you keep track of all your job applications and gains some useful insight whilst you're there.

This program was created, mainly, becasue I didn't want to keep having to open libreoffice calc (Think Excel) to keep track of the applications I've made.

## Running this webapp
Before launching the web app, you’ll need to have a MySQL database up and running, complete with the required table and schema.

You’ll find a Docker Compose file included, which can be used to spin up a database with the necessary configuration for convenience.
If you prefer to use your own database by hosting it on your homelab server alongside the web app, then the Compose file and its accompanying init file will help you set up the required schema.

Otherwise run the code below at the project root before launching the web-app.
```bash
docker-compose up -d
```
