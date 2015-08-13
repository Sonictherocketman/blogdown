from setuptools import setup


setup(
    name='blogdown',
    version='1.0',
    author='Brian Schrader',
    author_email='brian@brianschrader.com',
    packages=['blogdown', 'tests'],
    url='https://github.com/Sonictherocketman/blogdown',
    license='LICENSE.txt',
    description='A simple markdown add-on and parser for writing blog posts.',
    keywords=['markdown'],
    install_requires=[
        'markdown'
        ],
    )
