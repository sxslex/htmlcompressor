# -*- coding: UTF-8 -*-

import htmlcompressor


def test_join_script():
    assert htmlcompressor.compress(
        '''<html>
<script>alert(1);</script>
<script>alert(2);</script>
<script>alert(3);</script>
<script  async="True"  type="text/javascript" src="http://js.ir.la/jquery.js">
</script>
</html>'''
    ) == (
        '<html><script>alert(1);alert(2);alert(3)</script>'
        '<script async src=http://js.ir.la/jquery.js></script></html>'
    )
