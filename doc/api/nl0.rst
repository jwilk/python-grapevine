=======
``nl0``
=======

return number items of an iterable (start with 0)

Usage
-----

* ``<iterable> | nl0``

Examples
--------

>>> from grapevine import *
>>> ('foo', 'bar', 'quux') | nl0 | list
[(0, 'foo'), (1, 'bar'), (2, 'quux')]

.. seealso::

 * :doc:`nl1`
 * `GNU coreutils: nl <https://www.gnu.org/software/coreutils/manual/html_node/nl-invocation.html>`_

.. vim:ts=3 sts=3 sw=3 et
