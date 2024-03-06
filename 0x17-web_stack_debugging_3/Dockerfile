# Use an official Ubuntu 20.04 LTS image as the base image
FROM ubuntu:20.04

# Update the package repository and install Apache
RUN apt-get update \
    && apt-get install -y apache2 \
    && apt-get clean

# Start Apache in the foreground (not daemon mode)
CMD ["apache2ctl", "-D", "FOREGROUND"]
