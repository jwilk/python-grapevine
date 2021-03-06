==========
``select``
==========

slice an iterable

Usage
-----

* ``<iterable> | select[<int>]``
* ``<iterable> | select[<slice>]``

Examples
--------

>>> from grapevine import *
>>> ('foo', 'bar', 'quux') | select[-2:] | tuple
('bar', 'quux')
>>> sum(range(100) | select[i] | tuple != (range(100)[i],) for i in range(-3, 4))
0
>>> sum(range(100) | select[i:j:k] | list != range(100)[i:j:k] for i in range(-3, 4) for j in range(-3, 4) for k in range(-3, 4) if k != 0)
0

.. seealso::

 * :doc:`head`
 * :doc:`tail`

.. vim:ts=3 sts=3 sw=3 et
