MAKEFLAGS=--warn-undefined-variables

# Internal Variables
seconds ?= 10
image = pokedex-api-flask
docker_opts = --rm
docker_compose_opts = -f docker-compose.yml
docker_compose = docker-compose $(docker_compose_opts)

export APP_IMAGE = $(image)

build:
	docker build -t $(image) .

up:
	$(docker_compose) up
	until docker-compose logs db 2>&1 | grep 'port: 3306  MySQL Community Server (GPL)'; do continue; done

down restart:
	$(docker_compose) $@


# vi:ts=4:sw=4:cc=80
