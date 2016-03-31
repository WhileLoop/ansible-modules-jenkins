#!/bin/sh

# Add Jenkins apt repository.
wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update

# libxml2-dev, libxslt1-dev, zlib1g-dev needed for python lxml package.
sudo apt-get install -y python-pip jenkins python-dev libxml2-dev libxslt1-dev zlib1g-dev

sudo -H pip install -r /vagrant/requirements.txt

# Start Jenkins and wait for the server to initialize.
sudo service jenkins start
until $(curl --output /dev/null --silent --head --fail http://localhost:8080); do
    printf '.'
    sleep 5
done

# Use the Ansible module 'jenkins_job' to create and delete jenkins jobs.
cd /vagrant/
ansible-playbook job_example.yml -i inventory/hosts
