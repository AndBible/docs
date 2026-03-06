Experimental Features
=====================

|app| includes a number of experimental features that are still in development.
These features may change, be improved, or be removed in future versions. You
can enable or disable them individually.

.. note::

   Experimental features are disabled by default. Enable only the ones you want
   to try -- they may have rough edges or incomplete functionality.


Enabling Experimental Features
------------------------------

#. Open the top left main menu (|hamburger|).
#. Tap ``Settings``.
#. Scroll down to ``Advanced Settings``.
#. Tap ``Experimental features``.
#. Check the features you want to enable.
#. Tap ``OK``.


Available Features
------------------

LLM Mode (AI Text Processing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When enabled, this feature unlocks the full :doc:`AI assistant <ai>`
functionality. You must also have a configured AI provider for AI features to
appear.

Once enabled:

* An **LLM Mode** prompt selector appears in the window's text display settings,
  allowing you to process entire chapters through AI (e.g. translate or
  annotate a whole chapter at once).
* **AI action buttons** appear in verse selection, text selection, and window
  menus.

See :doc:`ai` for full details on setting up a provider, using prompts, and
managing costs.

.. note::

   This feature requires both the experimental feature toggle **and** a
   configured AI provider. If either is missing, AI options will not appear.


Add Paragraph Break Bookmark
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a **Paragraph break** option to the verse context menu. When used, it
creates a special bookmark that inserts a visual paragraph break before the
selected verse.

This is useful for adjusting the paragraph layout of Bible texts where the
original formatting does not match your reading preference. The breaks are
stored as bookmarks with a special internal label and are visible as extra
spacing between verses.


Bookmark Edit Actions
^^^^^^^^^^^^^^^^^^^^^

Adds edit action controls to bookmarks. When enabled, you can assign an
**Append** or **Prepend** action to a bookmark, which allows adding custom
content before or after the bookmarked verse in the Bible view.
