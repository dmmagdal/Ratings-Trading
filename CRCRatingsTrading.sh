#!/bin/sh

docker build -t ratings-trading .
docker run ratings-trading
