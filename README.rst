

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

