SSH
===

Options
-------

.. code :: bash

  -f   Requests ssh to go to background just before command execution.
  -N   Do not execute a remote command.

Recipes
-------

Run local SOCKS proxy server on a specific port:

.. code :: bash

  ssh -Nf -D 0.0.0.0:1080 localhost

To get access to Twitter server via http://localhost:9000 behind a firewall:

.. code :: bash

  ssh -L 9000:localhost:9990 -i ~/.ssh/id_rsa ubuntu@10.10.10.10
