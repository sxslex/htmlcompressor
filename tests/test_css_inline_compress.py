# -*- coding: UTF-8 -*-

import htmlcompressor


def test_css_inline_compress():
    assert htmlcompressor.compress(
        '''<html>
        <head>
            <title> Hello Word     </title>
<script>alert(1)</script>
<script>alert(2)</script>
<script>alert(3);</script>
<script  async="True"  type="text/javascript" src="http://js.ir.la/jquery;js">
</script>
   <style TYPE="text/css">
         .body {
            background-color: blue;
            width:  64px;
            height:  34px;
        }
   </style>
<script  async="True"  type="text/javascript">
alert("Hi");
    alert("Hi");
        alert("Hi");
                </SCRIPT>
                <script>alert(9999);</script>

        </head>
        <body>
            <div STYLE='background-color:  red;'>
                TESTE
            </div  >
        <body>
</html>'''
    ) == (
        '<html><head><title>Hello Word</title>'
        '<script>alert(1);alert(2);alert(3)</script>'
        '<script async src=http://js.ir.la/jquery;js></script>'
        '<style>.body{background-color:blue;width:64px;height:34px}</style>'
        '<script>alert("Hi");alert("Hi");alert("Hi");alert(9999)</script>'
        '</head><body><div style="background-color:red"> TESTE </div>'
        '<body></html>'
    )
