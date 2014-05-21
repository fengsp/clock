"""
Clock
-----

Clock is a nice datetime practice.

Links
`````

* `documentation <https://github.com/fengsp/clock>`_
* `development version
  <https://github.com/fengsp/clock/zipball/master#egg=Flask-dev>`_

"""
from setuptools import setup


setup(
    name='clock',
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
    install_requires=[
        'pytz>=0a',
        'tzlocal>=1.1.1'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ]
)
