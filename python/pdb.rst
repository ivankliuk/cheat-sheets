Python Debugger (pdb)
=====================

Running
```````

Start ``pdb`` from within a script

.. code :: python

  import pdb; pdb.set_trace()

Start ``pdb`` from the commandline

.. code :: python

  python -m pdb <file.py>

Basics
``````

| ``q(uit)`` - quit from the debugger and abort the program
| ``p(print)`` / ``pprint <object>`` - print / prettyprint <object>
| ``w(here)`` - print a stack trace, with the most recent frame at the bottom
| ``l(ist) [first[, last]]`` - List source code for the current file. With no arguments show 11 lines around the current one
| ``a(rgs)`` - print the argument list of the current function

Movement
````````

| ``d(own)`` - move the current frame one level down in the stack trace (to a newer frame)
| ``u(p)`` - move the current frame one level up in the stack trace (to an older frame)
| ``r(eturn)`` - continue execution until the current function returns
| ``c(ont(inue))`` - continue execution, only stop when a breakpoint is encountered
| ``s(tep)`` - execute the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function)
| ``n(ext)`` - continue execution until the next line in the current function is reached or it returns. (The difference between next and step is that step stops inside a called function, while next executes called functions at (nearly) full speed, only stopping at the next line in the current function.)

Running with unit tests
```````````````````````

Place ``import pdb; pdb.set_trace()`` in breakpoint and run ``nosetests`` with ``-s`` or ``--nocapture``.

Standart output reassignation
````````````````````````````

.. code :: python

  import pdb
  import sys
  mypdb = pdb.Pdb(stdout=sys.__stdout__)
  mypdb.set_trace()

