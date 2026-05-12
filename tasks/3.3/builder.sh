#!/bin/bash

# Проверка аргументов
if [ "$#" -ne 2 ]; then
  echo "Usage: ./builder.sh <github_repo> <dockerhub_repo>"
  exit 1
fi

GITHUB_REPO=$1
DOCKER_REPO=$2

# Временная папка
WORKDIR=$(mktemp -d)

echo "Cloning repo..."
git clone https://github.com/$GITHUB_REPO.git $WORKDIR

cd $WORKDIR || exit

echo "Building Docker image..."
docker build -t $DOCKER_REPO .

echo "Pushing to Docker Hub..."
docker push $DOCKER_REPO

echo "Done!"
