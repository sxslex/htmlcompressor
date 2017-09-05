======
htmlcompressor
======


.. image:: https://img.shields.io/badge/pypi-v1.1-orange.svg
    :target: https://pypi.python.org/pypi/htmlcompressor

.. image:: https://img.shields.io/badge/python-2.6%2C%202.7%2C%203.3+-blue.svg
    :target: https://travis-ci.org/sxslex/htmlcompressor.svg?branch=master

.. image:: https://travis-ci.org/sxslex/htmlcompressor.svg?branch=master
    :target: https://travis-ci.org/sxslex/htmlcompressor

.. image:: https://img.shields.io/badge/license--blue.svg
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


.. code:: pycon

    >>> import htmlcompressor
    >>> @htmlcompressor.decorator()
    >>> def index():
    >>>     return '''
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
    ... '''
    '<html><head><title>Test</title><script>alert(1);alert(2)</script></head><body><style>.class{display:none}</style></body></html>'


Installation
============

Use ``pip`` or ``easy_install``:

.. code::

    $ pip install git+https://github.com/sxslex/htmlcompressor.git


Development
===========

Use py.test to run unittests

