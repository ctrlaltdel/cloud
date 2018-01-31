CLOUD
=====

cloud - an easy to use tool for spawning disposable VM on an Openstack cloud

Installation
------------

* Install dependencies

    sudo apt-get install python-shade python-os-client-config

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
usage: cloud [-h] [--debug] [--image IMAGE] [--flavor FLAVOR] [--name NAME]
             [--net NET] [--no-floating-ip]
             [--floating-ip-pool FLOATING_IP_POOL] [--permanent] [--root]
             [--command [COMMAND [COMMAND ...]]] [--key-name KEY_NAME]
             [--volume] [--volume-size VOLUME_SIZE]
             [--volume-type VOLUME_TYPE] [--user USER] [--secgroup SECGROUP]
             [--availability_zone AVAILABILITY_ZONE]
             [--prefer-ipv4 | --prefer-ipv6] [--os-cloud <name>]
             [--os-auth-type <name>] [--os-auth-url OS_AUTH_URL]
             [--os-domain-id OS_DOMAIN_ID] [--os-domain-name OS_DOMAIN_NAME]
             [--os-project-id OS_PROJECT_ID]
             [--os-project-name OS_PROJECT_NAME]
             [--os-project-domain-id OS_PROJECT_DOMAIN_ID]
             [--os-project-domain-name OS_PROJECT_DOMAIN_NAME]
             [--os-trust-id OS_TRUST_ID]
             [--os-default-domain-id OS_DEFAULT_DOMAIN_ID]
             [--os-default-domain-name OS_DEFAULT_DOMAIN_NAME]
             [--os-user-id OS_USER_ID] [--os-username OS_USERNAME]
             [--os-user-domain-id OS_USER_DOMAIN_ID]
             [--os-user-domain-name OS_USER_DOMAIN_NAME]
             [--os-password OS_PASSWORD] [--insecure]
             [--os-cacert <ca-certificate>] [--os-cert <certificate>]
             [--os-key <key>] [--timeout <seconds>] [--os-service-type <name>]
             [--os-service-name <name>] [--os-interface <name>]
             [--os-region-name <name>] [--os-endpoint-override <name>]
             [--os-api-version <name>]
             [script]

Easy to use tool for spawning disposable VM on an Openstack

positional arguments:
  script                Script that will automatically be run inside the VM

optional arguments:
  -h, --help            show this help message and exit
  --debug, -d
  --image IMAGE, -i IMAGE
  --flavor FLAVOR, -f FLAVOR
  --name NAME, -n NAME
  --net NET
  --no-floating-ip
  --floating-ip-pool FLOATING_IP_POOL
  --permanent, -p
  --root, -r
  --command [COMMAND [COMMAND ...]], -c [COMMAND [COMMAND ...]]
  --key-name KEY_NAME, -k KEY_NAME
  --volume, -v
  --volume-size VOLUME_SIZE, -s VOLUME_SIZE
  --volume-type VOLUME_TYPE, -t VOLUME_TYPE
  --user USER, -u USER
  --secgroup SECGROUP
  --availability_zone AVAILABILITY_ZONE, -az AVAILABILITY_ZONE
  --prefer-ipv4, -4
  --prefer-ipv6, -6
  --os-cloud <name>     Named cloud to connect to
  --os-auth-type <name>, --os-auth-plugin <name>
                        Authentication type to use

Authentication Options:
  Options specific to the password plugin.

  --os-auth-url OS_AUTH_URL
                        Authentication URL
  --os-domain-id OS_DOMAIN_ID
                        Domain ID to scope to
  --os-domain-name OS_DOMAIN_NAME
                        Domain name to scope to
  --os-project-id OS_PROJECT_ID, --os-tenant-id OS_PROJECT_ID
                        Project ID to scope to
  --os-project-name OS_PROJECT_NAME, --os-tenant-name OS_PROJECT_NAME
                        Project name to scope to
  --os-project-domain-id OS_PROJECT_DOMAIN_ID
                        Domain ID containing project
  --os-project-domain-name OS_PROJECT_DOMAIN_NAME
                        Domain name containing project
  --os-trust-id OS_TRUST_ID
                        Trust ID
  --os-default-domain-id OS_DEFAULT_DOMAIN_ID
                        Optional domain ID to use with v3 and v2 parameters.
                        It will be used for both the user and project domain
                        in v3 and ignored in v2 authentication.
  --os-default-domain-name OS_DEFAULT_DOMAIN_NAME
                        Optional domain name to use with v3 API and v2
                        parameters. It will be used for both the user and
                        project domain in v3 and ignored in v2 authentication.
  --os-user-id OS_USER_ID
                        User id
  --os-username OS_USERNAME, --os-user-name OS_USERNAME
                        Username
  --os-user-domain-id OS_USER_DOMAIN_ID
                        User's domain id
  --os-user-domain-name OS_USER_DOMAIN_NAME
                        User's domain name
  --os-password OS_PASSWORD
                        User's password

API Connection Options:
  Options controlling the HTTP API Connections

  --insecure            Explicitly allow client to perform "insecure" TLS
                        (https) requests. The server's certificate will not be
                        verified against any certificate authorities. This
                        option should be used with caution.
  --os-cacert <ca-certificate>
                        Specify a CA bundle file to use in verifying a TLS
                        (https) server certificate. Defaults to
                        env[OS_CACERT].
  --os-cert <certificate>
                        Defaults to env[OS_CERT].
  --os-key <key>        Defaults to env[OS_KEY].
  --timeout <seconds>   Set request timeout (in seconds).

Service Options:
  Options controlling the specialization of the API Connection from
  information found in the catalog

  --os-service-type <name>
                        Service type to request from the catalog
  --os-service-name <name>
                        Service name to request from the catalog
  --os-interface <name>
                        API Interface to use [public, internal, admin]
  --os-region-name <name>
                        Region of the cloud to use
  --os-endpoint-override <name>
                        Endpoint to use instead of the endpoint in the catalog
  --os-api-version <name>
                        Which version of the service API to use
```
