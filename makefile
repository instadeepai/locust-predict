RUN_FLAGS=-it --rm -p 8888:8888 -v ${PWD}:/home/app/locust -w /home/app/locust
# Default version is python
version = python
DOCKER_IMAGE_TAG = $(version)
IMAGE=locust:$(DOCKER_IMAGE_TAG)
DOCKER_RUN=docker run $(RUN_FLAGS) $(IMAGE)

ifneq (,$(findstring python,$(version)))
DOCKERFILE=Dockerfile
else ifneq (,$(findstring r,$(version)))
DOCKERFILE=Dockerfile.R
endif

build:
	docker build --tag $(IMAGE) -f $(DOCKERFILE) .

bash:
	$(DOCKER_RUN) bash

run_notebook:
	$(DOCKER_RUN) jupyter notebook --ip 0.0.0.0 --no-browser --allow-root