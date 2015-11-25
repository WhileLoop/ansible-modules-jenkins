Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :shell, path: "RUNME.sh"
  config.vm.network :forwarded_port, guest: 8080, host: 8080
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
  end
end
