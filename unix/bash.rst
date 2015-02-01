Bash and command line utilities
===============================

Remove all ``.pyc`` files from a project:

.. code :: bash

  find . -name "*.pyc" -exec rm -rf {} \;

curl usage:

.. code :: bash

  curl -v -X POST -H 'X-Auth-Token: 123qwe' -H 'Content-Type: application/json' -d @POST_email_confirmation_codes.json http://localhost:5000/v3/email_confirmation_codes
  curl -v -X POST -H 'X-Auth-Token: 123qwe' -H 'Content-Type: application/json' -d '{"email": "test@example.com"}' http://localhost:5000/v3/email_confirmation_codes

Find and replace:

.. code :: bash

  find . -type f -print0 | xargs -0 sed -i 's/json.loads(resp.body)/resp.json_body/g'

Cut ``PID`` from processes list output:

.. code :: bash

  ps ax | grep '[k]eystone-all' | cut -f1 -d ' '

Use ``-B number`` to set how many lines before the match
and ``-A number`` for the number of lines after the match:

.. code :: bash

  grep -B 4 -A 2 pattern file.txt

If you want the same amount of lines before and after you can use ``-C number``:

.. code :: bash

  grep -C 3 pattern file.txt

Create ``tar.gz`` archive:

.. code :: bash

  tar -czvf tarballname.tar.gz item_to_compress

Unpack ``tar.gz`` archive:

.. code :: bash

  tar -xzvf tarballname.tar.gz

Download and run bash script:

.. code :: bash

  bash <(curl -s https://raw.githubusercontent.com/ivankliuk/scripts/master/postinstall.sh)

or:

.. code :: bash

  source <(curl -s https://raw.githubusercontent.com/ivankliuk/scripts/master/postinstall.sh)

Command line directory stack:

.. code :: bash

  stack@stack:/$ dirs
  /
  stack@stack:/$ pushd /var/
  /var /
  stack@stack:/var$ pushd /var/log/
  /var/log /var /
  stack@stack:/var/log$ dirs
  /var/log /var /
  stack@stack:/var/log$ popd
  /var /
  stack@stack:/var$ popd
  /
  stack@stack:/$ popd
  -bash: popd: directory stack empty
  stack@stack:/$

Quickly change date:

.. code :: bash

  sudo date +%Y%m%d -s "20141219"

Download and execute a script:
 
.. code :: bash
 
  wget -O - https://raw.githubusercontent.com/ivankliuk/scripts/master/postinstall.sh | bash
