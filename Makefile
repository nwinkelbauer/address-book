include make_env

NS ?= nickwisehart
VERSION ?= latest

IMAGE_NAME ?= address-book
CONTAINER_NAME ?= address-book
CONTAINER_INSTANCE ?= default

.PHONY: build run

build: Dockerfile
	docker build -t $(NS)/$(IMAGE_NAME):$(VERSION) -f Dockerfile .

run:
	docker run --rm --name $(CONTAINER_NAME)-$(CONTAINER_INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(IMAGE_NAME):$(VERSION)

default: build
