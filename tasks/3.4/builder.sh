#!/bin/bash

set -e

if [ "$#" -ne 2 ]; then
  echo "Usage: <github_repo> <dockerhub_repo>"
  exit 1
fi

GITHUB_REPO=$1
DOCKER_REPO=$2

WORKDIR=$(mktemp -d)

echo "Cloning repo..."
git clone https://github.com/$GITHUB_REPO.git $WORKDIR

cd $WORKDIR

echo "Logging into Docker Hub..."
echo $DOCKER_PWD | docker login -u $DOCKER_USER --password-stdin

echo "Building image..."
docker build -t $DOCKER_REPO .

echo "Pushing image..."
docker push $DOCKER_REPO

echo "Cleaning up..."
rm -rf $WORKDIR

echo "Done!"
