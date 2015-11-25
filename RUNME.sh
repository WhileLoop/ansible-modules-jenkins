#!/bin/sh

# Add Jenkins repo.
wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
# Install jenkins, ansible, and pip from apt.
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y python-pip ansible jenkins
# Use pip to install jenkinsapi.
sudo -H pip install -r /vagrant/requirements.txt
# Start Jenkins and wait for the server to initialize.
sudo service jenkins start
until $(curl --output /dev/null --silent --head --fail http://localhost:8080); do
    printf '.'
    sleep 5
done
# Use the Ansible module 'jenkins_job' to create and delete jenkins jobs.
cd /vagrant/
ansible-playbook job_example.yml
