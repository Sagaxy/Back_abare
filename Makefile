# env var main project name
DB_USER ?= abareuser
DB_PASSWORD ?= abarepass
DB_HOST ?= localhost
DB_PORT ?= 5432
DB_NAME ?= abare

PROJECT_NAME ?= abare
MODE ?= dev
PORT ?= 8080
VERSION ?= 0.1.0

CORS_ALLOW_ORIGINS ?= "localhost:3000,localhost:8080"
CORS_ALLOW_CREDENTIALS ?= true
CORS_ALLOW_METHODS ?= "*"
CORS_ALLOW_HEADERS ?= "*"


setup-env:
	bash config/scripts/setup_env.sh $(DB_USER) $(DB_PASSWORD) $(DB_HOST) $(DB_PORT) $(DB_NAME) $(PROJECT_NAME) $(MODE) $(PORT) $(VERSION) $(CORS_ALLOW_ORIGINS) $(CORS_ALLOW_CREDENTIALS) $(CORS_ALLOW_METHODS) $(CORS_ALLOW_HEADERS)

clean-env:
	rm -f .env Dockerfile docker-compose.yml

# ---------------------------------------------------------------------
# Whole Service (API + DB) with Docker Compose
service-build:
	docker compose build

service-run-debug:
	docker compose up --remove-orphans

service-run:
	docker compose up -d --remove-orphans

service-init: setup-env service-build service-run

service-stop:
	docker compose down

service-recreate-volume:
	docker volume rm postgres-$(PROJECT_NAME)-data
	docker volume create rm postgres-$(PROJECT_NAME)-data

service-clean: service-stop clean-env service-recreate-volume

# ---------------------------------------------------------------------
# Independent Services
api-build:
	docker build -t $(PROJECT_NAME)-$(MODE)-i .

api-run:
	docker run --rm --name $(PROJECT_NAME)-$(MODE)-c -p $(PORT):$(PORT) --volume ./src/logs/history:/app/logs/history --network $(PROJECT_NAME)-network $(PROJECT_NAME)-$(MODE)-i

api-rebuild: api-build api-run

api-init: setup-env api-rebuild

api-stop:
	docker stop $(PROJECT_NAME)-$(MODE)-c

api-clean:
	docker rmi $(PROJECT_NAME)-$(MODE)-i

api-clean-env: api-stop api-clean clean-env