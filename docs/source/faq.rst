Frequently Asked Questions
==========================

.. contents:: Contents
   :local:
   :depth: 1

I can't find ESV any more in Downloads. What's wrong?
------------------------------------------------------

The publishers of the ESV have unfortunately decided it is no longer in their
interest to publish towards the SWORD platform (by Crosswire Bible Society)
which |app| uses.

If you still have ESV on another device, you can transfer it by backing up the
module and restoring on the new device. See :doc:`backup_restore` for details.

Please add module X to AndBible!
--------------------------------

Modules in |app| are provided via the JSword engine, which uses SWORD modules
from `Crosswire <https://crosswire.org>`_ and several other freely available
module repositories. You should primarily make your requests to the Crosswire
modules team.

You can contact them via their
`email list <https://www.crosswire.org/mailman/listinfo/sword-devel>`_
or their other `contact methods <http://crosswire.org/contact/>`_.
See also their `FAQ <https://wiki.crosswire.org/EnduserFAQ>`_ and their
`instructions on contacting copyright holders <https://wiki.crosswire.org/Copyright>`_.

If the text is not copyrighted (i.e. it is public domain), there may be a
shortcut to get it into |app| quickly. In that case, please
`contact us <mailto:help.andbible@gmail.com>`_.

If you know that a module is available in MySword or MyBible applications, it
may be possible to install it in |app| too — see :doc:`documents` for details
on third-party module format support.

I found a text issue in a Bible / Commentary module
---------------------------------------------------

|app| developers don't fix module issues. Modules used by |app| are provided
primarily via the JSword engine which uses SWORD modules made by multiple
providers. You can determine who provides the module from the Download Documents
list. If you have an issue we encourage you to contact them directly.

* **Crosswire:** Use their `issue tracker <https://tracker.crosswire.org/projects/MOD/>`_.
  You can also get in touch with them via their
  `email list <https://www.crosswire.org/mailman/listinfo/sword-devel>`_
  or other `contact methods <http://crosswire.org/contact/>`_.
* **eBible:** Submit a message through their
  `online form <https://ebible.org/cgi-bin/contact.cgi>`_.
* **AndBible/AndBible Extra:** Raise an issue on our
  `GitHub issues page <https://github.com/AndBible/and-bible/issues>`_.

I have an older phone. Can I use AndBible?
------------------------------------------

The current version of |app| requires Android 6.0 (Marshmallow) or newer.
If you have an older device, you can download older versions:

.. list-table::
   :header-rows: 1

   * - Android Version
     - AndBible Version
     - Download
   * - 2.3 (Gingerbread)+
     - 2.9.5 (unsupported)
     - `Download <https://github.com/AndBible/and-bible/releases/tag/build-02.09.05>`_
   * - 4.4 (KitKat)+
     - 3.2.343 (unsupported)
     - `Download <https://github.com/AndBible/and-bible/releases/tag/v3.2.343>`_
   * - 5.0 (Lollipop)+
     - 4.0.687
     - `Download <https://github.com/AndBible/and-bible/releases/tag/production-687>`_
   * - 6.0 (Marshmallow)+
     - Latest
     - `Download <https://github.com/AndBible/and-bible/releases/latest>`_

How do I change the voice of the speech synthesis?
--------------------------------------------------

How the voice is changed varies between different TTS engines.

If you are using Google Text-to-Speech Engine (which you can install from
`Google Play <https://play.google.com/store/apps/details?id=com.google.android.tts>`_),
you can change the voice as follows: go to your device's system TTS settings,
tap the Settings icon, then "Install voice data", select your language, and
choose a voice.

See also the :doc:`speak` page for more about the Text-to-Speech feature.

Is there a version for iOS (iPhone / iPad)?
-------------------------------------------

No, |app| is exclusively for Android, and there are no plans for an iOS version
at this time. It would require a dedicated professional iOS developer to join
the project.

Some alternatives:

* Consider buying an inexpensive Android tablet to use |app|.
* You can :ref:`run the app on Linux using Waydroid <getting_started:Linux setup>`.
* You can use Android emulators like `BlueStacks <https://www.bluestacks.com/>`_
  on Windows or macOS.

How do I download more Bibles, commentaries, etc.?
---------------------------------------------------

See :doc:`documents` for instructions on downloading and managing documents.

In short: from the top left main menu (|hamburger|), tap `Download documents`,
then search for and install the documents you need.

How do I copy my notes and bookmarks to a new phone?
----------------------------------------------------

Back up on one device and restore on the other. See :doc:`backup_restore`
for detailed instructions.

Where do the Bible translations come from?
------------------------------------------

All documents available in |app| are either in the public domain or licensed
for distribution. They come from these sources:

* `Crosswire <https://crosswire.org>`_
* `IBT Russia <https://ibtrussia.org>`_
* `eBible <https://ebible.org>`_
* `STEPBible <https://public.modules.stepbible.org>`_
* `AndBible <https://andbible.github.io>`_

How do I downgrade from 5.0 to 4.0 (or 4.0 to 3.3)?
-----------------------------------------------------

.. warning::
   **Do not uninstall the app yet.** Uninstalling will remove all data,
   including the automatic backup that was created during the upgrade.

#. Go to ``Main menu > Backup & Restore``.
#. Under ``Import & Export``, select an earlier backup file to export
   (files named ``dbBackup-57-*.db`` for the pre-5.0 backup, or
   ``dbBackup-33-*.db`` for the pre-4.0 backup). Back it up somewhere safe.
#. Optionally, also back up your documents.
#. Uninstall the app.
#. Install the earlier version:
   `4.0 <https://github.com/AndBible/and-bible/releases/tag/production-687>`_ or
   `3.3 <https://github.com/AndBible/and-bible/releases/tag/production-400>`_
   from GitHub Releases. You may need to allow installs from unknown sources.
#. From ``Main Menu > Backup & Restore``, restore the backup file.

.. note::
   To prevent automatic updates, check your auto-update settings in Google Play
   or your app store. Using versions other than the latest is unsupported.

How to get the paid NET module working?
---------------------------------------

#. Purchase "NET Bible Crosswire Bible Society Sword module (Premium Version)"
   at `bible.org <https://store.bible.org/store/product/108>`_.
#. You will receive an email with a download link and an unlock code.
#. Download the SWORD module file from the linked page.
#. In |app|, use ``Backup & Restore > Restore > Documents``, then tap
   ``Restore From`` and select the downloaded file.
#. Go to ``Choose Document`` in the main menu. You will see the module with
   a red lock icon. Tap on it and enter the unlock code from your email.

Is there a way I can support the project?
-----------------------------------------

Yes! You can contribute with your skills (code, translations, documentation)
or sponsor development work at `shop.andbible.org <https://shop.andbible.org/>`_.

See our `contribution guide <https://github.com/AndBible/and-bible/wiki/How-to-contribute>`_
for all the ways you can help.
