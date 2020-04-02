===================================
Uri Online Judge Crawler (UriCrawl)
===================================
-------------------------------------------------------------
Command Line Tool for crawl and render templates for Problems
-------------------------------------------------------------

**incomplet, need automatized tests**, **python 3 recommended**

Features
========

With **uricrawl** you add to your enviroment a  useful **command line tool**
for file generation of problems using templates.

**uricrawl** use `scrapy <https://scrapy.org/>`_ and `jinja2 <http://jinja.pocoo.org/docs/dev/>`_.

Installation
============
**If you goes install in default python, you need sudo permissions.(try first in virtual env)**

.. code-block:: console

    $ pip install git+https://github.com/pyanderson/uricrawl

Linux Users
-----------
Scrapy needs some packages.

.. code-block:: console

    $ sudo apt-get install python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev

Windows Users
-------------
Probably one or more packages goes broke in installation (error: Microsoft Visual C++
{{ version }} is required), this occurs because you are in **windows** and need to format
your pc and install `Fedora <https://getfedora.org/>`_... Just kidding... You don't need install Fedora, can be
another linux distro :P. If you still wanna/need using windows, you can accesses this
amazing `site <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ (This saved my life sometimes when I was windows
user :shame:). Just download the packages WHL files corresponding to you python/system
version and install using pip.

    > pip install package_name.whl or python3 -m pip install package_name.whl

Usage
=====
Basic
-----
.. code-block:: console

    $ uricrawl 1025
    2016-09-27 00:18:10 [problemspider] INFO: Code files for 1025 problem were generated.
    $ ls
    1025-where-is-the-marble.c  1025-where-is-the-marble.cpp 1025-where-is-the-marble.py

Multiple Problems
-----------------

.. code-block:: console

    $ uricrawl 1302 1705
    2016-09-27 00:28:03 [problemspider] INFO: Code files for 1705 problem were generated.
    2016-09-27 00:28:03 [problemspider] INFO: Code files for 1302 problem were generated.
    $ ls
    1302-joining-couples.c    1302-joining-couples.py  1705-binary-lover.cpp
    1302-joining-couples.cpp  1705-binary-lover.c      1705-binary-lover.py

Custom Template
---------------
Code files are generated using **jinja2** with templates files, the are in `templates <https://github.com/pyanderson/uricrawl/tree/master/uricrawl>`_ folder,
but you can set you own templates using **-t or --template** option with the paths
of templates (see more in `Template <#template>`_ topic):

.. code-block:: console

    $ uricrawl 1450 -t mytemplate.cpp ~/mytemplate.py /home/thekiller/Documentos/myuritemplates/mytemplate.c
    2016-09-27 22:34:39 [problemspider] INFO: Code files for 1450 problem were generated.
    $ ls
    1450-ramesses-games.c    1450-ramesses-games.py   mytemplate.cpp
    1450-ramesses-games.cpp


Without Default Template
------------------------
If you set **-t** option you can set **-nd or --no-default** option to tool
don't generate code files using default templates.

.. code-block:: console

    $ uricrawl 1780 -t mytemplate.cpp -nd
    2016-09-27 22:49:38 [problemspider] INFO: Code files for 1780 problem were generated.
    $ ls
    1780-robots-formation.cpp  mytemplate.cpp

Language
--------
Default problems languages crawleds is English, but you can use **-l or
--language** to set language, values options: [en, pt, es]

.. code-block:: console

    $ uricrawl 1388 -l pt
    2016-09-27 22:52:21 [problemspider] INFO: Code files for 1388 problem were generated.
    $ ls
    1388-onde-estao-as-bolhas.c  1388-onde-estao-as-bolhas.cpp  1388-onde-estao-as-bolhas.py

Programming Language
--------------------
You can choose one or more **-pl or --programming-language** in [c, cpp, py]
options to tool render only this templates(this option only has effect in default templates).

.. code-block:: console

    $ uricrawl 1533 -pl cpp py
    2016-09-27 22:54:53 [problemspider] INFO: Code files for 1533 problem were generated.
    $ ls
    1533-detective-watson.cpp  1533-detective-watson.py

Name Pattern
------------
Probably you don't like my filename pattern, so, usign **-np or
--name-pattern** option you can format the filenames generated, just set a
string with the pattern, two tags are avaiable for this (number and title), my
pattern is: {{number}}-{{title}}, just reorder like you want :D.

.. code-block:: console

    $ uricrawl 1644 -np {{number}}
    2016-09-27 22:56:43 [problemspider] INFO: Code files for 1644 problem were generated.
    $ ls
    1644.c  1644.cpp  1644.py
    $ uricrawl 1644 -np {{title}}
    2016-09-27 23:11:51 [problemspider] INFO: Code files for 1644 problem were generated.
    $ ls
    1644.c  1644.cpp  1644.py  decode-the-strings.c  decode-the-strings.cpp  decode-the-strings.py
    $ uricrawl 1644 -np {{title}}_{{number}}
    2016-09-27 23:13:35 [problemspider] INFO: Code files for 1644 problem were generated.
    $ ls
    1644.c    1644.py                    decode-the-strings_1644.cpp  decode-the-strings.c    decode-the-strings.py
    1644.cpp  decode-the-strings_1644.c  decode-the-strings_1644.py   decode-the-strings.cpp

Full Example
------------

.. code-block:: console

    $ uricrawl 1026 1754 -t mytemplate.cpp -nd -l pt -np {{number}}-_-{{title}}
    2016-09-27 23:22:47 [problemspider] INFO: Code files for 1026 problem were generated.
    2016-09-27 23:22:47 [problemspider] INFO: Code files for 1754 problem were generated.
    $ ls
    1026-_-carrega-ou-nao-carrega.cpp  1754-_-a-sala-do-tempo.cpp  mytemplate.cpp

Template
========
All rended templates (defaults and custom) has some variables in context:

* number
* title
* description - A list of lines for all problem description.
* url
* _input - A list of lines for all problem input.
* _output - A list of lines for all problem output.
* filename
* created
* author

So custom your templates using `jinja2 syntax <http://jinja.pocoo.org/docs/dev/templates/>`_ in the better way you want.

Example Template
----------------------------
`template.cpp <https://github.com/pyanderson/uricrawl/blob/master/examples/template.cpp>`_

Command:
--------
.. code-block:: console

    $ uricrawl 1640 -t ~/Documentos/uricrawl/examples/template.cpp -nd
    2016-09-30 21:49:20 [problemspider] INFO: Code files for 1640 problem were generated.

Result
------
`1640-hotel-booking.cpp <https://github.com/pyanderson/uricrawl/blob/master/examples/1640-hotel-booking.cpp>`_
