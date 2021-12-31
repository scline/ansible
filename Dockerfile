# Dockerfile for Ansible environment
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3-pip \
    software-properties-common

RUN add-apt-repository --yes --update ppa:ansible/ansible
RUN apt-get install -y ansible

WORKDIR /ansible

COPY ansible/ /ansible/

ENV ANSIBLE_HOST_KEY_CHECKING=False

ENTRYPOINT ["/bin/bash"]
