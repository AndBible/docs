Search
======

The search form allows searching of Bible and commentaries.

Overview
--------

Find allows you to search for word(s), phrases, or any combination of words.


Bible searches
--------------

To search for a specific word in any Bible module tap on the burger menu located at the top left, then tap on "Find" . Then enter the word you are looking to find.
Optionally you can limit your search to only the OT, NT, or the book you are currently viewing.
If you enter multiple words,  optionally you can also look for an exact match, as a phrase, or for any of the words appearing any where within a verse.

For Bible modules that contain Strong's numbers, you can enter the following to find any verses where that number appears:

Note: the word strong must be in lower case.

strong:h3068

strong:G11


Commentary searches
-------------------

To do.

Advanced Search
---------------

Search Option Compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some searches cannot be performed with other searches. 

# 'All endings' is not compatible with a 'Fuzzy Search'
# 'Any word' / 'Phrase' is not compatible with 'Proximity'

Proximity Search
^^^^^^^^^^^^^^^^

Find words that are a within a specific distance. To do a proximity search use the tilde, "~", symbol at the end of a phrase. 
For example to search for a "God" and "light" within 10 words of each other in a document use the search:


    "God light"~3

.. note::
    The order of the words are important. The above example will find verses where the word 'God' comes before the word 'light'

Fuzzy Search
^^^^^^^^^^^^

Fuzzy searches find words that are similar in spelling to the search words.
To do a fuzzy search use the tilde, "~", symbol at the end of a single word term. 
For example to search for a term similar in spelling to "believe" use the fuzzy search:

    believe~

This search will find terms like .

To narrow parameter can specify the required similarity. The value is between 0 and 1, 
with a value closer to 1 only terms with a higher similarity will be matched. For example:

roam~0.8
The default that is used if the parameter is not given is 0.5.
