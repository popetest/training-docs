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


Sample Diagram
==============

.. graphviz::

   digraph Flatland {

      a -> b -> c -> g;
      a  [shape=polygon,sides=4]
      b  [shape=polygon,sides=5]
      c  [shape=polygon,sides=6]

      g [peripheries=3,color=yellow];
      s [shape=invtriangle,peripheries=1,color=red,style=filled];
      w  [shape=triangle,peripheries=1,color=blue,style=filled];

      }

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

numbered list item
------------------

1. numbered one
2. numbered two

1) numbered one
2 ) numbered two

i) roman numeral one
ii) roma numberal two

definition list
~~~~~~~~~~~~~~~

one
  the 1st cardinal
two
  the 2nd cardinal

Sample Table
============

== == ==
A  B  c
== == ==
1  2  5
3  4  6
== == ==

+---+---+---+
| A | B | C |
+===+===+===+
| 1 | 2 | 3 |
+---+---+---+
| 3 | 4 | H |
+---+---+---+

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


latex math
==========

.. math::

\int_0^\pi \cos (x) dx
