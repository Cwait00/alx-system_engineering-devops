#!/usr/bin/env bash
# Server-01 login commands

# Setting up the SSH agent
eval $(ssh-agent)

# Path to identityFile
ssh-add ~/.ssh/school

# Username and IP Address
ssh -i ~/.ssh/school ubuntu@172.17.0.6