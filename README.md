# sanic-app-boilerplate
A simple Sanic boilerplate app with MongoDB, Redis and Docker

# Using
So, let's start with creating a new environment via `docker-machine` and switch to it (skip this step if you have it already initialized):
```
docker-machine create --driver=virtualbox sanic-sandbox && eval $(docker-machine env sanic-sandbox)
```
After it you will need to build, create and up all required containers with `docker-compose` tool, like this:
```
docker-compose -f docker-compose.dev.yaml up -d
```
When the previous command will have completed, just connect to the `app` container with Sanic application and start the it:
```
python ./manage.py run --host=0.0.0.0
```
After this you can get an access to the application API via `http://localhost:8000/redis` and `http://localhost:8000/mongodb`.

Available resources after starting docker-compose with settings that were specified in `docker-compose.dev.yaml`:
- Public API: `http://localhost:8000/redis` and `http://localhost:8000/mongodb`
- Redis UI: `http://localhost:8081/`
- MongoDB UI: `http://localhost:1234/` with `root`/`root` credentials

# The application structure
```
sanic-app/
    app/
      commands/
          __init__.py
          runserver.py
      extensions/
          __init__.py
          base.py
          mongodb.py
          redis.py
      mongodb/
          __init__.py
          api.py
      redis/
          __init__.py
          api.py
      __init__.py
    __init__.py
    config.py
    manage.py
```
## Folders
- app/commands - Contains an implementation for commands of Sanic-Script extension.
- app/extensions - Contains small wrappers around Sanic stuff for initializing async libs without any pain
- app/mongodb - Contains API endpoints that works with MongoDB as the main database
- app/redis - Contains API endpoints that works with Redis as a cache storage

## Files
**app/__init__.py** 
Contains everything that necessary for running an application: initialize steps, registering blueprints and APIs and so on. 

**config.py**
A place for collecting all configuration parameters for a Sanic application. Specify it once, use it everywhere where is needed.

**manage.py**
Here you can specify a list of commands that will make your life as developer easier. Basically, it relies onto [Sanic-Script] (https://github.com/tim2anna/sanic-script) extension, that makes it real. Moreover, you can implement your own command or re-use existing plugins for it. For example, add migration commands from the [Sanic-PW](https://github.com/Relrin/sanic-pw) package for creating and applying Peewee ORM migrations.

For getting a list of available commands just invoke it with `-h`/`--help` flag
```
python ./manage.py -h
```
