# coding: utf-8

import os
import click
import htmlcompressor


# @click.group()
# @click.version_option(
#     version=htmlcompressor.__version__, prog_name='htmlcompressor')
# def cli():
#     pass


@click.command(help='compress html `source_or_path`')
@click.argument('source_or_path')
def compress(source_or_path):
    if os.path.exists(source_or_path):
        content = open(source_or_path, 'rb').read()
        if hasattr(content, 'decode'):
            content = content.decode()
    else:
        content = source_or_path
    print(htmlcompressor.compress(content))


if __name__ == '__main__':
    compress()
