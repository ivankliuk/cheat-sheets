Git
===

Diff between branches particular file:

.. code :: bash

  git diff master..IPD-122 keystone_contrib_bss/controllers.py

This just undoes a commit:

.. code :: bash

  git reset --soft 0d1d7fc32

This will destroy any local modifications.
Don't do it if you have uncommitted work you want to keep.

.. code :: bash

  git reset --hard 0d1d7fc32

Rebasing current branch with ``master``:

.. code :: bash

  git rebase master

Show current branch:

.. code :: bash

  git branch

Show remote branches:

.. code :: bash

  git branch -a

Pick a file from another branch:

.. code :: bash

  git checkout master keystone_contrib_bss/config.py

Delete a remote branch:

.. code :: bash

  git push origin --delete IPD-181

Deletes LOCAL branch:

.. code :: bash

  git branch --delete master

Rename branch:

.. code :: bash

  git branch -m old_name new_name

If you want to rename the current branch, you can simply do:

.. code :: bash

  git branch -m new_name

Pushes local HEAD to remote branch.
(Useful for re-initialization of remote branch if rebasing holds very very hard)

.. code :: bash

  git push origin HEAD:IPD-182

