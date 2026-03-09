Getting Started
===============

Installation
------------

There are a number of different ways to install |app| on an Android phone.
You can install |app| using the
`Google Play Store <https://play.google.com/store/apps/details?id=net.bible.android.activity>`_,
`F-Droid <https://f-droid.org/packages/net.bible.android.activity/>`_,
the `Amazon App Store <http://www.amazon.com/Martin-Denham-And-Bible/dp/B004Z2KKYK>`_,
or directly from the `Releases section of our GitHub <https://github.com/AndBible/and-bible/releases/latest>`_
source code repository.

.. image:: /images/google_play_badge.png
   :height: 50
   :target: https://play.google.com/store/apps/details?id=net.bible.android.activity


.. image:: /images/f-droid_badge.png
   :height: 50
   :target: https://f-droid.org/packages/net.bible.android.activity/

.. image:: /images/amazon_badge.png
   :height: 50
   :target: http://www.amazon.com/Martin-Denham-And-Bible/dp/B004Z2KKYK

.. image:: /images/obtainium_badge.png
   :height: 50
   :target: https://obtainium.imranr.dev/

Note: An apk downloaded directly from the "Assets" sub-menu of the Github Releases
will not automatically update. You can use a tool like `Obtainium <https://obtainium.imranr.dev/>`_
to download (and update) the apk from Github. AFTER installing Obtainium, you can click 
`this link <https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22net.bible.android.activity%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FAndBible%2Fand-bible%22%2C%22author%22%3A%22AndBible%22%2C%22name%22%3A%22Bible%20Study%22%2C%22preferredApkIndex%22%3A0%2C%22additionalSettings%22%3A%22%7B%5C%22includePrereleases%5C%22%3Afalse%2C%5C%22fallbackToOlderReleases%5C%22%3Atrue%2C%5C%22filterReleaseTitlesByRegEx%5C%22%3A%5C%22%5C%22%2C%5C%22filterReleaseNotesByRegEx%5C%22%3A%5C%22%5C%22%2C%5C%22verifyLatestTag%5C%22%3Afalse%2C%5C%22sortMethodChoice%5C%22%3A%5C%22date%5C%22%2C%5C%22useLatestAssetDateAsReleaseDate%5C%22%3Afalse%2C%5C%22releaseTitleAsVersion%5C%22%3Afalse%2C%5C%22trackOnly%5C%22%3Afalse%2C%5C%22versionExtractionRegEx%5C%22%3A%5C%22%5C%22%2C%5C%22matchGroupToUse%5C%22%3A%5C%22%5C%22%2C%5C%22versionDetection%5C%22%3Atrue%2C%5C%22releaseDateAsVersion%5C%22%3Afalse%2C%5C%22useVersionCodeAsOSVersion%5C%22%3Atrue%2C%5C%22apkFilterRegEx%5C%22%3A%5C%22andbible-production%5C%22%2C%5C%22invertAPKFilter%5C%22%3Afalse%2C%5C%22autoApkFilterByArch%5C%22%3Atrue%2C%5C%22appName%5C%22%3A%5C%22%5C%22%2C%5C%22appAuthor%5C%22%3A%5C%22%5C%22%2C%5C%22shizukuPretendToBeGooglePlay%5C%22%3Afalse%2C%5C%22allowInsecure%5C%22%3Afalse%2C%5C%22exemptFromBackgroundUpdates%5C%22%3Afalse%2C%5C%22skipUpdateNotifications%5C%22%3Afalse%2C%5C%22about%5C%22%3A%5C%22%5C%22%2C%5C%22refreshBeforeDownload%5C%22%3Afalse%2C%5C%22includeZips%5C%22%3Afalse%2C%5C%22zippedApkFilterRegEx%5C%22%3A%5C%22%5C%22%7D%22%2C%22overrideSource%22%3Anull%7D>`_
to load the AndBible config directly into Obtainium.

Linux setup
-----------

#. `Install Waydroid <https://docs.waydro.id/usage/install-on-desktops>`_
#. Run Waydroid and install GAPPS version of Android
   (The GAPPS version is required to update WebView and for Google Drive sync).
#. `Set up Play Services <https://docs.waydro.id/faq/google-play-certification>`_.
#. `Disable the on-screen keyboard <https://docs.waydro.id/faq/disable-on-screen-keyboard>`_.
#. Install / Upgrade `WebView <https://play.google.com/store/apps/details?id=com.google.android.webview>`_
   from Google Play. This fixes some issues.
#. Install `Google Speech Services <https://play.google.com/store/apps/details?id=com.google.android.tts>`_
   from Google Play (if you want to use Text to Speech).
#. Install `Google Drive <https://play.google.com/store/apps/details?id=com.google.android.apps.docs>`_
   from Google Play (not needed for Google Drive sync, but you might need it if
   you have stored any document backups etc in Google Drive).
#. Install AndBible with your preferred method (See: `Installation`_).

Notes:

   * You can integrate Waydroid with The Linux desktop:

     #. Set up `multi-window mode <https://docs.waydro.id/usage/waydroid-prop-options>`_.
     #. Restart your computer.
     #. AndBible and other apps installed in Waydroid should now be visible in the normal application menu.

   * If the clipboard doesn't work between Android and Linux:

     #. Install pyclip (i.e ``sudo pip3 install pyclip``).
     #. Install wl-clipboard (i.e. ``sudo apt install wl-clipboard``).
     #. Restart your computer.


.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/_r5Dz7xCy44" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

Windows 11 setup
----------------

.. note::
   Windows Subsystem for Android (WSA) has been discontinued as of March 5th, 2025.

Alternative methods for running |app| on Windows include using Android emulators such as
`Bluestacks <https://www.bluestacks.com/>`_ or `NoxPlayer <https://www.bignox.com/>`_,
but these are not tested or officially supported.

Mirroring (and using) |app| on any Computer
-------------------------------------------

Using a tool like `scrcpy <https://github.com/Genymobile/scrcpy>`_ it is possible
to display your |app| on any desktop or laptop computer (Windows, MacOS, or Linux).

#. `Enable USB Debugging <https://developer.android.com/studio/debug/dev-options#enable>`_
   on your Android phone.
#. Connect your phone to your computer via USB cable (wireless connections are
   also possible - see the `scrcpy documentation
   <https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md#connection>`_)
#. Install and run scrcpy using the official instructions for `Windows
   <https://github.com/Genymobile/scrcpy/blob/master/doc/windows.md>`_, `MacOS
   <https://github.com/Genymobile/scrcpy/blob/master/doc/macos.md>`_, or `Linux
   <https://github.com/Genymobile/scrcpy/blob/master/doc/linux.md>`_.
