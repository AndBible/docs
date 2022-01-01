Searching
=========

The search form allows searching of Bible and commentaries.

Overview
--------

To do.

Bible searches
--------------

To do.

Commentary searches
-------------------

To do.

Advanced Search
---------------

Search Option Compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some searches cannot be performed with other searches. 

#. 'All endings' is not compatible with a 'Fuzzy Search'
#. 'All endings' is not compatible with a 'Proximity Search'
#. 'Any word' / 'Phrase' is not compatible with 'Proximity'

Proximity Search
^^^^^^^^^^^^^^^^

Find words that are a within a specific distance. To do a proximity search use the tilde, "~", symbol at the end of a phrase. 
For example to search for a "God" and "light" within 10 words of each other in a document use the search:

.. admonition:: Example

    "God light"~10

.. note::
    The order of the words are important. The above example will find verses where the word 'God' comes before the word 'light'

Fuzzy Search
^^^^^^^^^^^^

Fuzzy searches find words that are similar in spelling to the search words.
To do a fuzzy search use the tilde, "~", symbol at the end of a single word term followed by a number between 0 and 1. 
For example to search for a term similar in spelling to "believe" use the fuzzy search:

.. admonition:: Example

    believe~0.6

This search will find terms like 'believes', 'believed' etc.

To narrow the search use a larger number. A value of 0.9 is a very near match. A value of 0.3 is a very, very broad match.
parameter can specify the required similarity. 

