django-openipmap-provision
==========================

Provisioning of a development version of django-openipmap.

Prerequisites
=============
- Virtualbox ( https://www.virtualbox.org/ )
- Vagrant ( https://www.vagrantup.com/ )
- Ansible ( http://www.ansible.com/ )

Setup
=====

    # clone this repository
    git clone https://github.com/emileaben/django-openipmap-provision.git
    cd django-openipmap-provision
    # clone the django-openipmap repository
    git clone https://github.com/emileaben/django-openipmap
    # put a local centos6 vagrant image to local directory [*]
    curl -L <centos6-box-url> > centos6.box
    # initiate virtual machine containing openipmap
    vagrant up
    # wait for vagrant/ansible to do their magic. takes couple of minutes.

[*] see http://www.vagrantbox.es/ for a list, but because of security implications of running an virtual machine from an untrusted host, it may be advisable to build your own vagrant base box ( https://docs.vagrantup.com/v2/virtualbox/boxes.html ). Alternatively one can edit the Vagrantfile and get the 'chef/centos-6.5' image from vagrantcloud.

Usage
=====

The django-openipmap repository is available both on your local box (django-openipmap) as well as in /home/vagrant/openipmap in the virtual machine.

To run openipmap in the virtual box:

    vagrant ssh
    manage runserver 0.0.0.0:8000
   
Because TCP/8000 is mapped to TCP/8000 on your local machine, openipmap is now available at: http://localhost:8000/openipmap

The provisioning will create a virtual environment that contains 1000 mock users called 'user<id>' with password 'vagrant', with <id>: 1-999 , use this to log in. The provisioning will also download the most recent openipmap hostname and ip geoloc entries.
