============
``dev_null``
============

empty sequence

Usage
-----

* ``dev_null``

Examples
--------

>>> from grapevine import *
>>> dev_null | tuple
()
>>> for x in dev_null:
...   raise Exception
...

.. seealso::

 * `The Jargon File: /dev/null <http://www.catb.org/esr/jargon/html/0/dev-null.html>`_
 * `Python Library Reference: os.devnull <https://docs.python.org/library/os.html#os.devnull>`_

.. vim:ts=3 sts=3 sw=3 et
