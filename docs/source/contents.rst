Welcome to testPope's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

link offsite
============

`Website <http://website.com>`_

link with url in footnote
=========================

.. _Website: http://website.com


HTML
====

|my_header|

.. |my_header| raw:: html

  <h1>foo</h1>


image
=====

.. image:: index.png


italic text
===========

*italic text*

bold text
=========

**bold text**

fixed width text
================

``fixed width text``

literal text
============

\*not italics\*


span w/ class
=============

.. role:: foo

:foo:`text`


==============
document title
==============

line break
==========

| the line breaks
| here

document header
===============

:Date: 2001-08-16
:Version: 1
:Authors: - John Doe
          - Jane Roe


section header
==============


subsection header
-----------------

subsubsection header
~~~~~~~~~~~~~~~~~~~~


level 4 header
``````````````

1. numbered one
2. numbered two

1) numbered one
2 ) numbered two

i) roman numeral one
ii) roma numberal two


one
  the 1st cardinal
two
  the 2nd cardinal

Sample Table
============

== ==
A  B
== ==
1  2
3  4
== ==

+---+---+
| A | B |
+===+===+
| 1 | 2 |
+---+---+
| 3 | 4 |
+---+---+

multiple column cell
====================

+-------+
| title |
+===+===+
| 1 | 2 |
+---+---+

pre-formatted fixed-width block with no need to escape markup or < and &
========================================================================

::

  int add(int a, int b) {
    return (a+b);
  }

highlighted code
================


.. code-block:: c

  int add(int a, int b) {
    return (a+b);
  }

define anchor
=============

.. _foo:

link to anchor
==============

foo_

comment
=======

.. comment
   another comment

