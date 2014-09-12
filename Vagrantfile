# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
   config.vm.box = "file:centos-6-gii.box"
   config.vm.synced_folder "./django-openipmap", "/home/vagrant/openipmap", create: true, owner: "vagrant", group: "vagrant"
   config.vm.network "forwarded_port", guest: 8000, host: 8000
   config.vm.provision "ansible" do |ansible|
      ansible.sudo = true
      ansible.playbook = "./playbook.yml"
   end 
end
