"""
Clock
-----

Clock is a nice datetime replacement.

Links
`````

* `documentation <https://github.com/fengsp/clock>`_
* `development version
  <https://github.com/fengsp/clock/zipball/master#egg=Flask-dev>`_

"""
from setuptools import setup


setup(
    name='Clock',
    version='0.1',
    url='https://github.com/fengsp/clock',
    license='BSD',
    author='Shipeng Feng',
    author_email='fsp261@gmail.com',
    description='A minimalist datetime library for Python',
    long_description=__doc__,
    py_modules=['clock'],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ]
)
