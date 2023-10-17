## Docker
Docker is an application that simplifies the process of managing application processes in containers. Containers let you run your applications in resource-isolated processes. 

vs
**Virtualisation**
- You’ll see that a server hosts 3 virtual machines; one for our API, one for a webserver and one for a database. The most important take away here is that each virtual machine has its own Guest OS. This is totally redundant and takes up a lot of memory.
- When you use Docker you don’t need virtual machines. You package your applications in a container which runs on a machine. we save a lot of memory; our apps share an OS (the kernel at least), making it much more light-weight. 

**Portability**: The Dockerfile allows us to ship not only our application code but also our environment.We can not only push the source code of the app to git but also include the Dockerfile. When someone else pulls our repository they can build the source code in the Docker container we can create from the Dockerfile.

Most of the time multiple containers have to work together to create all functionalities. An example: a website, API and database have to be connected together. Docker Compose allows us to do. We can create a file that defines how containers are connected with one another. We can use this file to instantiate all of the Dockerfiles for all of our containers all at once!

### Intallation
src: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04<br/>
https://docs.docker.com/engine/install/ubuntu/

### Steps
A container is a running instance of our image.
we can run our image with the following command:

```
  docker run --publish 4331:5000 python-docker
```
- we tell docker to run an image called _python-docker._
- *--publish 4331:5000* details how we want to connect ports between our laptop (the host machine) and the docker container.
- Since Flask is running on port 5000 by default, the second part of this flag needs to be 5000. 



