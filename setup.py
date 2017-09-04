from setuptools import setup

setup(
    name='htmlcompressor',
    version='1.0.0',
    url='https://github.com/sxslex/htmlcompressor',
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
        'Programming Language :: Python :: 2.6, 2.7 and 3.3+',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
            'htmlcompressor = htmlcompressor.cli:compress',
        ],
    },
)
