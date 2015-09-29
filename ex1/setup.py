import os
from setuptools import setup, find_packages


requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2',
    ]

setup(name='ex1',
      version='0.0',
      description='ex1',
      long_description='',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='ex1',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = ex1:main
      [console_scripts]
      initialize_ex1_db = ex1.scripts.initializedb:main
      """,
      )
