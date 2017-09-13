CLOUD
=====

cloud - an easy to use tool for spawning disposable VM on an Openstack cloud

Installation
------------

* Install dependencies

    sudo apt-get install python-openstackclient python-os-client-config python-novaclient python-keystoneclient python-neutronclient python-cinderclient

* Download `XXXX-openrc.sh` file from the OpenStack dashboard or
* Configure `~/.config/openstack/clouds.yaml` (see [`os-client-config` documentation](https://docs.openstack.org/os-client-config/latest/user/configuration.html)).

Usage
-----

Simple case: you need access to a single cloud project:

* Download `XXXX-openrc.sh` file from the OpenStack dashboard
```
$ source XXXX-openrc.sh
$ cloud
ubuntu@cloud-dependent-car:~$ logout

$
```

Second case: you need access to multiple cloud projects at the same time and
you've already configured your `~/.config/openstack/clouds.yaml` file
accordingly:

```
$ cloud --os-cloud CLOUD_NAME
ubuntu@cloud-tidy-window:~$ logout

$
```

Help command will tell you the many other options available:

```
$ cloud -h
```
