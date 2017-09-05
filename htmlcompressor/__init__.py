# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from htmlcompressor import htmlmin
import warnings
import jsmin

import csscompressor


__version__ = '1.1'


def compress(
    html_input,
    remove_comments=True,
    remove_empty_space=True,
    remove_all_empty_space=True,
    reduce_empty_attributes=True,
    reduce_boolean_attributes=True,
    remove_optional_attribute_quotes=True,
    keep_pre=False,
    pre_tags=None,
    pre_attr='pre',
    clear_type_javascript=True,
    clear_type_css=True,
    minify_js=True,
    minify_css=True,
    join_script_inline=True
):
    """Compress HTML CSS and Java Script of a page.

    :param html_input: A string containing the HTML to be minified.
    :param remove_comments: Remove comments found in HTML. Individual comments
      can be maintained by putting a ``!`` as the first character inside the
      comment.
      Thus::

         <!-- FOO --> <!--! BAR -->

      Will become simply::

         <!-- BAR -->

      The added exclamation is removed.
    :param remove_empty_space: Remove empty space found in HTML between an
      opening
      and a closing tag and when it contains a newline or carriage return. If
      whitespace is found that is only spaces and/or tabs, it will be turned
     into
      a single space. Be careful, this can have unintended consequences.
    :param remove_all_empty_space: A more extreme version of
      ``remove_empty_space``, this removes all empty whitespace found between
      tags. This is almost guaranteed to break your HTML unless you are very
      careful.
    :param reduce_empty_attributes:
    :param reduce_boolean_attributes: Where allowed by the HTML5 specification,
      attributes such as 'disabled' and 'readonly' will have their value
      removed,
      so 'disabled="true"' will simply become 'disabled'. This is generally a
      good option to turn on except when JavaScript relies on the values.
    :param remove_optional_attribute_quotes: When True, optional quotes around
      attributes are removed. When False, all attribute quotes are left intact.
      Defaults to True.
    :param keep_pre: By default, htmlmin uses the special attribute ``pre`` to
      allow you to demarcate areas of HTML that should not be minified.
      It removes
      this attribute as it finds it. Setting this value to ``True``
    tells htmlmin
      to leave the attribute in the output.
    :param pre_tags: A list of tag names that should never be minified. You are
      free to change this list as you see fit, but you will probably want to
      include ``pre`` and ``textarea`` if you make any changes to the list. Note
      that ``<script>`` and ``<style>`` tags are never minimized.
    :param pre_attr: Specifies the attribute that, when found in an HTML tag,
      indicates that the content of the tag should not be minified. Defaults to
      ``pre``.
    :param clear_type_javascript:
    :param clear_type_css:
    :param minify_js:
    :param minify_css:
    :param join_script_inline:
    :return: A string containing the minified HTML.

    If you are going to be minifying multiple HTML documents, each with the same
    settings, consider using :class:`.Minifier`.
    """
    html_new = htmlmin.minify(
        input=html_input,
        remove_comments=remove_comments,
        remove_empty_space=remove_empty_space,
        remove_all_empty_space=remove_all_empty_space,
        reduce_empty_attributes=reduce_empty_attributes,
        reduce_boolean_attributes=reduce_boolean_attributes,
        remove_optional_attribute_quotes=remove_optional_attribute_quotes,
        keep_pre=keep_pre,
        pre_tags=pre_tags if pre_tags is not None else ('pre', 'textarea'),
        pre_attr=pre_attr
    )
    if len(html_new.split('<script')) != len(html_new.split('</script>')):
        warnings.warn("script tag was not closed", Warning)
        return html_input
    if clear_type_javascript:
        html_new = html_new.replace(' type=text/javascript', '')
    if clear_type_css:
        html_new = html_new.replace(' type=text/css', '')
    html_new = html_new.replace('<script async>', '<script>')
    if minify_js:
        new_html = []
        html_list = html_new.split('<script')
        new_html.append(html_list[0])
        for i in html_list[1:]:
            r1 = i.split('>')
            new_html.append('<script' + r1[0] + '>')
            if '</script' not in i:
                new_html.append('>'.join(r1[1:]))
                break
            r2 = '>'.join(r1[1:]).split('</script')
            new_html.append(jsmin.jsmin(r2[0]))
            new_html.append('</script' + ''.join(r2[1:]))
        html_new = ''.join(new_html)
    if minify_css:
        new_html = []
        html_list = html_new.split('<style')
        new_html.append(html_list[0])
        for i in html_list[1:]:
            r1 = i.split('>')
            new_html.append('<style' + r1[0] + '>')
            r2 = '>'.join(r1[1:]).split('</style')
            new_html.append(csscompressor.compress(r2[0]))
            new_html.append('</style' + ''.join(r2[1:]))
        html_new = ''.join(new_html)

        new_html = []
        html_list = html_new.split(' style="')
        new_html.append(html_list[0])
        for i in html_list[1:]:
            new_html.append(' style="')
            r2 = i.split('"')
            new_html.append(csscompressor.compress(r2[0]).strip(';'))
            new_html.append('"' + ''.join(r2[1:]))
        html_new = ''.join(new_html)
    if join_script_inline:
        resp = ''
        pos = html_new.find('<script>')
        pos_end = html_new.find('</script>')
        while pos > -1 and pos_end > -1:
            resp += ''.join(html_new[:pos + 8])
            html_new = ''.join(html_new[pos + 8:])
            p1 = html_new.find('</script>')
            while p1 == html_new.find('</script><script>'):
                html_new = (
                    ''.join(html_new[0:p1]) +
                    (';' if html_new[p1 - 1] != ';' else '') +
                    ''.join(html_new[p1 + 17:])
                )
                p1 = html_new.find('</script>')
            pos = html_new.find('<script>')
        if resp:
            html_new = resp + html_new
    if minify_js:
        html_new = html_new.replace(';</script>', '</script>')
    return html_new


def decorator(*xargs, **xkargs):
    def wrap(f):
        def wrapped_f(*args, **kargs):
            resp = f(*args, **kargs)
            try:
                return compress(resp, *xargs, **xkargs)
            except:
                return resp
        return wrapped_f
    return wrap
