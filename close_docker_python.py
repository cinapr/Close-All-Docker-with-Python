import docker

def stop_container(container):
    client = docker.client.from_env()
    for socket in client._connection.sockets:
        socket.close()
    container.stop()

# Get a list of Docker containers
containers = docker.client.from_env().containers.list()

# Stop all of the Docker containers
for container in containers:
    stop_container(container)
