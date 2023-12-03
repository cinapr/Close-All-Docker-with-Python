import docker

docker_client = docker.from_env()

# List running containers
running_containers = docker_client.containers.list()

# List all containers (including stopped ones)
all_containers = docker_client.containers.list(all=True)

# Print container details
for container in running_containers:
    print(f"Container ID: {container.id}, Image: {container.image}, Status: {container.status}")

for container in all_containers:
    print(f"Container ID: {container.id}, Image: {container.image}, Status: {container.status}")
