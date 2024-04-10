# demo-schedule-analyzer

## Initialize
### Docker
First, install the docker engine on your machine.
See [Docker Installation Documentation](https://docs.docker.com/engine/install/)

Next, download and cd into this repository. Compose the docker image using the following command:

`docker compose build`

Finally, run the image with Docker using the following command.

`docker container run --rm -p 8888:5000 demo-schedule-analyzer-server`

The hosted container can be accessed by navigating to [localhost:8888](localhost:8888)