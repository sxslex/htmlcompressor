======
htmlcompressor
======


.. image:: https://travis-ci.org/sxslex/htmlcompressor.svg?branch=master
    :target: https://travis-ci.org/sxslex/htmlcompressor

.. image:: https://img.shields.io/badge/python-2.6%2C%202.7%2C%203.4%2C%203.5%2C%203.6-blue.svg
    :target:

.. imagem:: https://img.shields.io/badge/license--blue.svg
    :target: https://github.com/sxslex/htmlcompressor/blob/master/LICENSE


Compress HTML CSS and Java Script of a page.
Passes all original unittests.


Usage
=====

.. code:: pycon

    >>> import htmlcompressor
    >>> htmlcompressor.compress('''
    ...<html>
    ...    <head>
    ...        <title>  Test  </title>
    ...        <script type="text/javascript">  alert(1)  </script>
    ...        <script type="text/javascript">  alert(2);  </script>
    ...    </head>
    ...     <body>
    ...         <style type="text/css">  .class {   display:  none; } </style>
    ...     </body>
    ...</html>
    ... ''')
    '<html><head><title>Test</title><script>alert(1);alert(2)</script></head><body><style>.class{display:none}</style></body></html>'



Compatibility
=============

Tested under Python 2.6, 2.7 and 3.3+


Installation
============

Use ``pip`` or ``easy_install``:

.. code::

    $ pip install htmlcompressor


Development
===========

Use py.test to run unittests

