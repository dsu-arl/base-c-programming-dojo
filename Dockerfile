FROM ubuntu:latest

USER root

RUN apt update

# # Install any tools or configure anything:
# RUN apt install --reinstall -y build-essential

USER hacker