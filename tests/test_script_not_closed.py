# -*- coding: UTF-8 -*-

import htmlcompressor


def test_join_script():
    resp = htmlcompressor.compress(
        '''<html>
<script>
<body>
BUG
<div> TESTE </div>
</body>
</html>'''
    )
    print(resp == '<html><script>')
    assert resp == (
        '''<html>
<script>
<body>
BUG
<div> TESTE </div>
</body>
</html>'''
    )
