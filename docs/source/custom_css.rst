Custom CSS
==========

.. _custom-css-for-individual-modules-or-globally-for-and-bible-and-bible-40:

Custom CSS for individual modules or globally for And Bible (And Bible 4.0+)
----------------------------------------------------------------------------

And Bible offers option to include custom CSS and fonts in module zip
files. Place your CSS file under module directory (or subdirectory), and
define CSS file path in config file with
``AndBibleCSS=path-to/yourcssfile.css``

CSS file you need to format as follows:

Prefix everything with ``.sword-YOURMODULE`` class (where ``YOURMODULE``
is the module initials of your module). For night mode, prefix
everything with .night class.

If you have used ``<hi type="my-type">`` tag in your module, you can
define css for your tags with ``.hi-my-type`` class definitions.

Example
(`https://github.com/AndBible/special-modules/tree/master/HISB <https://github.com/AndBible/special-modules/tree/master/HISB>`__):

mods.d/HISB.conf

::

   [HISB]
   DataPath=./modules/texts/ztext/HISB/
   AndBibleCSS=style/style.css
   ...

Put your font file SILEOTSR.ttf to ./modules/texts/ztext/HISB/style/.
Define your css in ./modules/texts/ztext/HISB/style/style.css as follows

::

   @font-face {
       font-family: 'Custom HISB Font';
       src: url('./SILEOTSR.ttf') format('truetype');
   }

   .sword-HISB {
       font-family: 'Custom HISB Font';
   }

   .sword-HISB .hi-x-trlit {
       color: green;
       font-size: 0.7em;
       vertical-align: top;
       font-weight: bold;
   }

   .night .sword-HISB {
       vertical-align: text-top;
    
       color: #00FF00; /*#green; */
   }

   .night .sword-HISB .hi-x-trlit {
       color:  white; /*#green;*/
       font-size: 0.7em;
       vertical-align: top;
       font-weight: bold;
   }

Global styling
--------------

If you want to create a module that alters global style (i.e. how And
Bible looks overall), you can create add-on module (i.e. put
``Category=And Bible``) and add configuration
``AndBibleProvidesStyle=True`` line to the conf.

Example config

::

   [StyleExample]
   DataPath=./modules/texts/ztext/StyleExample/
   Version=1.0
   ShortPromo=Module that provides custom CSS and applies to all documents. Also provides example font.
   Description=Module that provides custom CSS and applies to all documents.
   DistributionLicense=Copyrighted; Freely distributable
   Category=And Bible
   ModDrv=RawGenBook
   InstallSize=194837
   AndBibleMinimumVersion=539
   AndBibleProvidesFont=Style Example Font;style/SILEOTSR.ttf
   AndBibleProvidesStyle=True
   AndBibleCSS=style/style.css

Debugging css
-------------

Please see `Android Webview Remote debugging
guide <https://developer.chrome.com/docs/devtools/remote-debugging/>`__
to see how you can investigate how to manipulate css.

Examples
--------

See
`https://github.com/AndBible/special-modules/ <https://github.com/AndBible/special-modules/>`__
