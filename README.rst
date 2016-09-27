===============================
Uri Online Judge Tool (UriTool)
===============================
-------------------------------------------------------------
Command Line Tool for crawl and render templates for Problems
-------------------------------------------------------------

**incomplete, is not python2 compatible yet, and need more tests**

Features
========

With **uritool** you add to your enviroment a  **command line tool**
that streamlines the file generation of problems using a template.

**uritool** use `scrapy <https://scrapy.org/>`_ and `jinja2 <http://jinja.pocoo.org/docs/dev/>`_.

Installation
============
.. code-block:: console

    $ python3 -m pip install git+https://github.com/pyanderson/uritool


Usage
=====
Basic
-----
.. code-block:: console

    $ uritool 1025
    2016-09-27 00:18:10 [problemspider] INFO: Code files for 1025 problem were generated.
    $ ls
    1025-where-is-the-marble.c  1025-where-is-the-marble.cpp 1025-where-is-the-marble.py

Multiple Problems
-----------------

.. code-block:: console

    $ uritool 1302 1705
    2016-09-27 00:28:03 [problemspider] INFO: Code files for 1705 problem were generated.
    2016-09-27 00:28:03 [problemspider] INFO: Code files for 1302 problem were generated.
    $ ls
    1302-joining-couples.c    1302-joining-couples.py  1705-binary-lover.cpp
    1302-joining-couples.cpp  1705-binary-lover.c      1705-binary-lover.py

Custom Template
---------------
Code files are generated using **jinja2**, the are in [templates folder](../master/uritool/templates),
but you can set you own templates using **-t or --template** optioni with paths
of templates (see more in **Template** topic):

.. code-block:: console
    $ uritool 1450 -t mytemplate.cpp ~/mytemplate.py /home/thekiller/Documentos/myuritemplates/mytemplate.c
    $ ls

Without Default Template
------------------------
If you set **-t** option you can set **-nd or --no-default** option to tool
don't generate code files using default templates.

.. code-block:: console
    $ uritool 1450 -t mytemplate.cpp -nd
    $

Language
--------
Default problems languages crawleds is English, but you can use **-l or
--language** to set language, values options: [en, pt, es]

.. code-block:: console
    $ uritool 1450 -l pt
    $

Programming Language
--------------------
You can choose one or more **-pl or --programming-language** in [c, cpp, py]
options to tool render only this templates.

.. code-block:: console
    $ uritool 1450 -pl cpp py
    $

Name Pattern
------------
Probably you don't like my filename pattern, so, usign **-np or
--name-pattern** option you can format the filenames generated, just set a
string with the pattern, two tags are avaiable for this (number and title), my
pattern is: {{number}}-{{title}}, just reorder like you want :D

.. code-block:: console
    $ uritool 1450 -np {{number}}
    $

Template
========
All rended templates (defaults and custom) has some variables in context:

* number
* title
* description
* url
* _input
* _output
* filename
* created
* author

So custom your templates using jinja2 syntaxe in the better way you want.

Example
-------

License
-------
 The MIT License

 Copyright (c) 2016 Anderson Lima anderson.sl93@hotmail.com

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
