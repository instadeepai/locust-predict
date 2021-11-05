RUN_FLAGS=-it --rm -p 8888:8888 -v ${PWD}:/home/app/locust -w /home/app/locust
IMAGE=locust:latest
DOCKER_RUN=docker run $(RUN_FLAGS) $(IMAGE)

build:
	docker build --tag $(IMAGE) .

run:
	$(DOCKER_RUN) bash

run_notebook:
	$(DOCKER_RUN) jupyter notebook --ip 0.0.0.0 --no-browser --allow-root