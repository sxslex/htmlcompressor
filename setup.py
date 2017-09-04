from setuptools import setup

setup(
    name='htmlcompressor',
    version='1.0.1',
    url='https://github.com/sxslex/htmlcompressor',
    download_url=(
        'https://github.com/sxslex/htmlcompressor/archive/v1.0.1.tar.gz'
    ),
    author='SleX',
    author_email='sx.slex@gmail.com',
    description='Compress HTML CSS and Java Script of a page.',
    keywords=['html', 'css', 'javascript', 'compressor', 'minify'],
    packages=['htmlcompressor', 'htmlcompressor.htmlmin'],
    install_requires=['htmlmin', 'jsmin', 'csscompressor'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
            'htmlcompressor = htmlcompressor.cli:compress',
        ],
    },
)
