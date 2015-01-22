CoreOS DNA spliced with Debian Wheezy
#####################################

:Authors: Yazz Atlas
:slug: DockerDNA
:category: Work
:date: 2015-01-21 16:07
:tags: CoreOS, Debian, etcd, fleetd
:summary: Debian Wheezy + Parts of CoreOS + Docker

Over the past few weeks I have been working extracting some of the DNA from CoreOS_. 
It's been an interesting process to see what is needed to create a CoreOS_ like 
cluster. What I've found out is you really only need a few programs.

.. _CoreOS: https://coreos.com/
.. _etcd: https://github.com/coreos/etcd
.. _etcdctl: https://github.com/coreos/etcdctl
.. _fleet: https://github.com/coreos/fleet
.. _fleetctl: https://github.com/coreos/fleet
.. _confd: https://github.com/coreos/fleet
.. _docker: https://www.docker.com/
.. _systemd: http://www.freedesktop.org/wiki/Software/systemd/


CoreOS Parts
------------

- etcd_
- etcdctl_
- fleet_
- fleetctl_

Kelsey Hightower Parts
----------------------

- confd_

Linux Requirements
------------------

- docker_
- systemd_


