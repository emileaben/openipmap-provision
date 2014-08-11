# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
   config.vm.box = "file:centos-6-gii.box"
   config.vm.synced_folder "./openipmap", "/home/openipmap/openipmap", create: true
#   config.vm.provision :shell, path: "bootstrap.sh"
   config.vm.provision "ansible" do |ansible|
      ansible.sudo = true
      ansible.playbook = "./playbook.yml"
   end 
end
