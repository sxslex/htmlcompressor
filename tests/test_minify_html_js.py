# -*- coding: UTF-8 -*-

import htmlcompressor


def test_compressor_single():
    assert htmlcompressor.compress(
        '''<html>
        <head>
            <title>  Test  </title>
            <script type="text/javascript">  Test  </script>
        </head>
        <body>
           <style type="text/css">  .class {   display:  none; } </style>
        </body>
    </html>''') == (
        '<html><head><title>Test</title><script>Test</script></head>'
        '<body><style>.class{display:none}</style></body></html>'
    )
