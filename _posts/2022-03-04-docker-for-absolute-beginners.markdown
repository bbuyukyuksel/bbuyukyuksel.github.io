---

layout: post
title: Docker for absolute beginners - El Kitapçığı
date: 2022-03-04 00:00:00 +0300
description: Introduction to docker environment.
lang: en
img: docker.png
tags: [Docker, Container, Handbook]
contents: 

---

# Introduction
This handbook aims to teach docker basics.

------------------------------------------------------------------------------
# Starting
## Docker Version
```bash
$ docker --version
```
## Starting docker
```bash
$ systemctl status docker
$ systemctl start docker
# or
$ sudo dockerd
$ sudo dockerd --debug # Start docker service in debug mode
```
## Testing Docker
```bash
$ docker run hello-world
```

------------------------------------------------------------------------------
# Containers
## Show all containers
```bash
$ docker container ls
$ docker container ls -a
```
## Looking Active Containers
```bash
    $ docker container ps
```
## Show All Running Containers (included if they run)
```bash
$ docker ps -a
```
## Detach Mode
```bash
$ docker run -itd ubuntu
$ docker ps
```
## Stopping running docker
```bash
$ docker stop <id or name>
$ docker ps -a
```
## Removing Container
```bash
$ docker rm <id or name>
```

## Remove All Containers
```bash
$ docker container prune
```
## Execute a Command on Running Container
```bash
$ docker run -itd ubuntu
$ docker exec -it <id or name> /bin/bash
// without interactive mode
$ docker exec <id or name> ls
```

------------------------------------------------------------------------------
# Images
## Show Docker Images
```bash
$ docker images
$ docker image ls
```
## Removing Images
```bash
$ docker rmi <image name>
$ docker image rm <image name>
$ docker image prune # removes all dangling images
```
## Just Download a Docker Image
```bash
$ docker pull <image name:version>
```

------------------------------------------------------------------------------
# Inspect
## Container
```bash
$ docker container ls
$ docker inspect <container id>
```
## Image
```bash
$ docker image ls
$ docker image inspect <image id>
```

------------------------------------------------------------------------------
# Docker Example - Jenkins
For download Jenkins
```bash
$ docker pull jenkins
$ docker image ls
$ docker image inspect <jenkins image id>
# map port
$ docker run -d -p 80:8080 jenkins/jenkins
$ docker ps
```

------------------------------------------------------------------------------
# Docker Networks
## List or Delete Networks
```bash
$ docker network ls
$ docker network rm <network id>
```
## Delete Dangling Networks
```bash
$ docker network prune
```
## Bridge Network (Default)
```bash
$ docker run ubuntu
```
## None Network
```bash
$ docker run ubuntu --network=none
```
## Host Network
```bash
$ docker run ubuntu --network=host
```
## Custom Network
```bash
$ docker network create --driver=bridge --subnet=182.1.0.1/16 isolatedNetwork
$ docker network ls
$ docker network inspect <network id>
$ docker run -itd --name=testUbuntu --net=isolatedNetwork ubuntu
$ docker inspect <container id or container name>
$ docker container inspect <container id or container name>
```
### Connect / Disconnect a container into a network
```bash
$ docker network connect <network name> <container id>
$ docker network disconnect <network name> <container id>
```

------------------------------------------------------------------------------
# Communicating Between Two Docker Containers
## Stop All Containers
```bash
$ docker stop $(docker ps -aq)
```
## Delete All Containers
```bash
$ docker rm $(docker ps -aq)
```
## Example
```bash
$ docker network create --driver=bridge --subnet=182.0.1.1/16 isolatedNetwork
$ docker run -itd --name=base centos
$ docker run -itd --name=test1 --net=isolatedNetwork centos
$ docker ps
$ docker exec -it base /bin/bash
	//inside $ ping test1
$ docker network connect isolatedNetwork base
$ docker exec -it base /bin/bash
	//inside $ ping test1
$ docker network disconnect isolatedNetwork base
$ docker exec -it base /bin/bash
	//inside $ ping test1
```

------------------------------------------------------------------------------
# Docker Volumes
`/var/lib/docker`
```bash
$ docker volume create data_volume
$ sudo ls /var/lib/docker/volumes -lrt
$ sudo ls /var/lib/docker/volumes/data_volume -lrt
$ sudo ls /var/lib/docker/volumes/data_volume/_data -lrt
```
`/www` directory in the container 
```bash
$ docker run -itd --name=base -v data_volume:/www ubuntu
$ docker exec -it base /bin/bash
	$ ls -lrt
```
## Docker Bind Volumes
```bash
$ mkdir data
$ docker run  -itd -v /home/ryhme/data:/www ubuntu
$ docker run --mount type=bind,source=/home/rhyme/data,target=/www ubuntu
```

## How to add a volume to an existing Docker container?
```bash
$ docker ps  -a

CONTAINER ID        IMAGE                 COMMAND                  CREATED              STATUS                          PORTS               NAMES
5a8f89adeead        ubuntu:14.04          "/bin/bash"              About a minute ago   Exited (0) About a minute ago                       agitated_newton

$ docker commit 5a8f89adeead newimagename
$ docker run -ti -v "$PWD/somedir":/somedir newimagename /bin/bash
```

------------------------------------------------------------------------------
# Extra Information
## Starting a Test Container
To use the docker exec command, you will need a running Docker container. If you don’t already have a container, start a test container with the following docker run command:
```bash
$ docker run -d --name container-name alpine watch "date >> /var/log/date.log"
```
This command creates a new Docker container from the official alpine image. This is a popular Linux container image that uses Alpine Linux, a lightweight, minimal Linux distribution.

We use the `-d` flag to detach the container from our terminal and run it in the background. `--name container-name` will name the container `container-name`. You could choose any name you like here, or leave this off entirely to have Docker automatically generate a unique name for the new container.

Next we have `alpine`, which specifies the image we want to use for the container.

And finally we have watch `"date >> /var/log/date.log"`. This is the command we want to run in the container. `watch` will repeatedly run the command you give it, every two seconds by default. The command that watch will run in this case is `date >> /var/log/date.log`. `date` prints the current date and time, like this:
```bash
Output
Fri Jul 23 14:57:05 UTC 2021
```

The `>> /var/log/date.log` portion of the command redirects the output from `date` and appends it to the file `/var/log/date.log`. Every two seconds a new line will be appended to the file, and after a few seconds it will look something like this:
```bash
Output
Fri Jul 23 15:00:26 UTC 2021
Fri Jul 23 15:00:28 UTC 2021
Fri Jul 23 15:00:30 UTC 2021
Fri Jul 23 15:00:32 UTC 2021
Fri Jul 23 15:00:34 UTC 2021
```
In the next step we’ll learn how to find the names of Docker containers. This will be useful if you already have a container you’re targeting, but you’re not sure what its name is.
## Finding the Name of a Docker Container
```bash
$ docker ps
```
## Running an Interactive Shell in a Docker Container

```bash
$ docker exec -it container-name sh
```
## Running a Non-interactive Command in a Docker Container
```bash
$ docker exec container-name tail /var/log/date.log
```
## Running Commands in an Alternate Directory in a Docker Container
```bash
$ docker exec --workdir /tmp container-name pwd
Output
/tmp
```
## Running Commands as a Different User in a Docker Container
```bash
$ docker exec --user guest container-name whoami
Output
guest
```
## Passing Environment Variables into a Docker Container
```bash
$ docker exec -e TEST=sammy container-name env
Output
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=76aded7112d4
TEST=sammy
HOME=/root
```
To set multiple variables, repeat the -e flag for each one:
```bash
$ docker exec -e TEST=sammy -e ENVIRONMENT=prod container-name env
```
If you’d like to pass in a file full of environment variables you can do that with the `--env-file` flag.

First, make the file with a text editor. We’ll open a new file with `nano` here, but you can use any editor you’re comfortable with:
```bash
$ nano .env
```
We’re using `.env` as the filename, as that’s a popular standard for using these sorts of files to manage information outside of version control.

Write your `KEY=value` variables into the file, one per line, like the following:
```
# Filename .env
TEST=sammy
ENVIRONMENT=prod
```
Save and close the file. To save the file and exit `nano`, press `CTRL+O`, then `ENTER` to save, then `CTRL+X` to exit.

Now run the `docker exec` command, specifying the correct filename after `--env-file`:
```bash
$ docker exec --env-file .env container-name env
Output
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=76aded7112d4
TEST=sammy
ENVIRONMENT=prod
HOME=/root
```


