========
``leak``
========

remove magic

Usage
-----

* ``<pipelined-iterable> | leak``
* ``leak(<pipelined-iterable>)``

Examples
--------

>>> from grapevine import *

>>> leak(dev_null)  # doctest: +ELLIPSIS
<...iterator object at 0x...>

>>> cat([1, 2, 3]) | leak  # doctest: +ELLIPSIS
<...iterator object at 0x...>

.. vim:ts=3 sts=3 sw=3 et
