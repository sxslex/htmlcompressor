# -*- coding: UTF-8 -*-

import htmlcompressor


def test_js_no_comma_at_the_end():
    assert htmlcompressor.compress(
        '''<html>
        <head>
            <title> Hello Word     </title>
<script>alert(1)</script>
<script>alert(2)</script>
<script>alert(3);</script>
<script  async="True"  type="text/javascript" src="http://js.ir.la/jquery;js">

</script>
<script  async="True"  type="text/javascript">
alert("Hi");
    alert("Hi");
        alert("Hi");
                </SCRIPT>
                <script>alert(9999);</script>

        </head>
</html>''') == (
        '<html><head><title>Hello Word</title>'
        '<script>alert(1);alert(2);alert(3)</script>'
        '<script async src=http://js.ir.la/jquery;js></script>'
        '<script>alert("Hi");alert("Hi");alert("Hi");alert(9999)</script>'
        '</head></html>'
    )
