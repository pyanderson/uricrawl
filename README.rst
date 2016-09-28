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
Code files are generated using **jinja2** with templates files, the are in `templates <https://github.com/pyanderson/uritool/tree/master/uritool/templates>`_ folder,
but you can set you own templates using **-t or --template** option with the paths
of templates (see more in **Template** topic):

.. code-block:: console

    $ uritool 1450 -t mytemplate.cpp ~/mytemplate.py /home/thekiller/Documentos/myuritemplates/mytemplate.c
    2016-09-27 22:34:39 [problemspider] INFO: Code files for 1450 problem were generated.
    $ ls
    1450-ramesses-games.c    1450-ramesses-games.py   mytemplate.cpp
    1450-ramesses-games.cpp


Without Default Template
------------------------
If you set **-t** option you can set **-nd or --no-default** option to tool
don't generate code files using default templates.

.. code-block:: console

    $ uritool 1780 -t mytemplate.cpp -nd
    2016-09-27 22:49:38 [problemspider] INFO: Code files for 1780 problem were generated.
    $ ls
    1780-robots-formation.cpp  mytemplate.cpp

Language
--------
Default problems languages crawleds is English, but you can use **-l or
--language** to set language, values options: [en, pt, es]

.. code-block:: console

    $ uritool 1388 -l pt
    2016-09-27 22:52:21 [problemspider] INFO: Code files for 1388 problem were generated.
    $ ls
    1388-onde-estao-as-bolhas.c  1388-onde-estao-as-bolhas.cpp  1388-onde-estao-as-bolhas.py

Programming Language
--------------------
You can choose one or more **-pl or --programming-language** in [c, cpp, py]
options to tool render only this templates.

.. code-block:: console

    $ uritool 1533 -pl cpp py
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

    $ uritool 1644 -np {{number}}
    2016-09-27 22:56:43 [problemspider] INFO: Code files for 1644 problem were generated.
    $ ls
    1644.c  1644.cpp  1644.py

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

So custom your templates using jinja2 syntaxe in the better way you want.

Example default template.cpp
----------------------------
    /*
     * =====================================================================================
     *
     *       Filename:  {{ filename }}
     *
     *            Url:  {{ url }}
     *
    {%- for line in description -%}
        {%- if loop.index == 1 %}
     *    Description:  {{ line }}
        {%- else %}
     *					{{ line }}
        {%- endif %}
    {%- endfor %}
     *
    {%- for line in _input -%}
        {%- if loop.index == 1 %}
     *          Input:  {{ line }}
        {%- else %}
     *					{{ line }}
        {%- endif %}
    {%- endfor %}
     *
    {%- for line in _output -%}
        {%- if loop.index == 1 %}
     *         Output:  {{ line }}
        {%- else %}
     *					{{ line }}
        {%- endif %}
    {%- endfor %}
     *
     *        Version:  1.0
     *        Created:  {{ created }}
     *       Revision:  none
     *       Compiler:  g++
     *
     *         Author:  {{ author }}
     *
     * =====================================================================================
     */
    #include <iostream>

    using namespace std;

    int main(){
        return 0;
    }

Result
------
    /*
     * =====================================================================================
     *
     *       Filename:  1644.cpp
     *
     *            Url:  https://www.urionlinejudge.com.br/repository/UOJ_1644_en.html
     *
     *    Description:  Bruce Force has had an interesting idea how to
     *					encode strings. The following is the description
     *					of how the encoding is done: Let x1,x2,...,xn be
     *					the sequence of characters of the string to be
     *					encoded. Choose an integer M and N pairwise
     *					distinct numbers p1,p2,...,pn from the set {1, 2,
     *					..., N} (a permutation of the numbers 1 to N).
     *					Repeat the following step m times. For 1 ≤ i ≤ N
     *					set yi to xpi, and then for 1 ≤ i ≤ N replace xi
     *					by yi. For example, when we want to encode the
     *					string "hello", and we choose the value M = 3 and
     *					the permutation 2, 3, 1, 5, 4, the data would be
     *					encoded in 3 steps: "hello" -> "elhol" -> "lhelo"
     *					-> "helol". Bruce gives you the encoded strings,
     *					and the numbers M and p1, ..., pn used to encode
     *					these strings. He claims that because he used huge
     *					numbers m for encoding, you will need a lot of
     *					time to decode the strings. Can you disprove this
     *					claim by quickly decoding the strings?
     *
     *          Input:  The input contains several test cases. Each test
     *					case starts with a line containing two numbers N
     *					and M (1 ≤ N ≤ 80, 1 ≤ M ≤ 109). The following
     *					line consists of N pairwise different numbers
     *					p1,...,pn (1 ≤ pi ≤ N). The third line of each
     *					test case consists of exactly N characters, and
     *					represent the encoded string. The last test case
     *					is followed by a line containing two zeros.
     *
     *         Output:  For each test case, print one line with the
     *					decoded string.
     *
     *        Version:  1.0
     *        Created:  09/27/16 23:01:09
     *       Revision:  none
     *       Compiler:  g++
     *
     *         Author:  thekiller
     *
     * =====================================================================================
     */
    #include <iostream>

    using namespace std;

    int main(){
        return 0;
    }

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
