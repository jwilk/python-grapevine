=======
``yes``
=======

yield repeatedly the same object

Usage
-----

* ``yes(<object>)``

Examples
--------

>>> from grapevine import *
>>> zip((1, 2, 3), yes(7))
[(1, 7), (2, 7), (3, 7)]
>>> sum(yes(6) | head(7))
42

.. seealso::

 * `GNU coreutils: yes <https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html#yes-invocation>`_

.. vim:ts=3 sts=3 sw=3 et
