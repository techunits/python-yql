==========
Python YQL
==========

Python YQL is a client library for making queries with Yahoo Query Language.


Test Status
============

.. image:: https://secure.travis-ci.org/project-fondue/python-yql.png
   :target: http://travis-ci.org/project-fondue/python-yql

Installation
============

::

    pip install yql

or 

::

    easy_install yql

Usage
=====

::

    >>> import yql
    >>> y = yql.Public()
    >>> query = 'select * from flickr.photos.search where text=@text and api_key="INSERT_API_KEY_HERE" limit 3';
    >>> y.execute(query, {"text": "panda"})


Source-code
===========

Branches exist at https://github.com/project-fondue/python-yql

Documentation
=============

Documentation can be found at http://python-yql.org/

Plugins
=======

* WeatherWrapper

Contributions
=============

Bug-fixes/Features/Patches always welcome - please submit a pull request on github.com

