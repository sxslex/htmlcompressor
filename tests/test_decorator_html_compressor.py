# -*- coding: utf-8 -*-

import htmlcompressor


@htmlcompressor.decorator()
def create_html(title, description, scripts=None):
    return '''<html>
        <head>
            <title> %(title)s     </title>
            <description>  %(description)s </description>
            %(scripts)s
<script  async="True"  type="text/javascript" src="http://js.ir.la/jquery;js">

</script>
<script  async="True"  type="text/javascript">
alert("Hi");
    alert("Hi");
        alert("Hi");
                </SCRIPT>
                <script>alert(9999);</script>

        </head>
</html>''' % dict(
            title=title,
            description=description,
            scripts='\n'.join(
                '<script>%s</script>' % s for s in scripts
            ) if scripts else ''
        )


def test_js_no_comma_at_the_end():
    assert create_html(
        'Hello Word',
        description='Page compress',
        scripts=['alert(1)', 'alert(2)', 'alert(3);']
    ) == (
        '<html><head><title>Hello Word</title>'
        '<description> Page compress </description>'
        '<script>alert(1);alert(2);alert(3)</script>'
        '<script async src=http://js.ir.la/jquery;js></script>'
        '<script>alert("Hi");alert("Hi");alert("Hi");alert(9999)</script>'
        '</head></html>'
    )
