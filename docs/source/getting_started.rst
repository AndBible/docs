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
to download (and update) the apk from Github.

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
     #. AndBible and other apps installed in Wayrdoid should now be visible in the normal application menu.

   * If the clipboard doesn't work between Android and Linux:

     #. Install pyclip (i.e ``sudo pip3 install pyclip``).
     #. Install wl-clipboard (i.e. ``sudo apt install wl-clipboard``).
     #. Restart you computer.


.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/_r5Dz7xCy44" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

Windows 11 setup
----------------

Note: Windows Subsystem for Android has been discontinued as of March 5th, 2025.
Alternate method for installing on |app| may be Bluestacks or NoxPlayer, but neither
of these methods are tested or supported.

To run |app| on Windows 11 using Windows Subsystem for Android:

This may be a bit technical if you are outside the US and involves
downloading the Windows Subsystem for Android (WSA),
running a command to install it, starting Windows Subsystem for Android,
enabling developer mode, downloading the apk from GitHub releases,
and installing the app with adb.

1. `Install Windows Subsystem for Android <https://www.xda-developers.com/how-to-run-android-apps-on-any-windows-11-pc/>`_
2. `Set up adb <https://www.xda-developers.com/install-adb-windows-macos-linux/>`_
3. `Download the APK from GitHub releases <https://github.com/AndBible/and-bible/releases/latest>`_
4. `Side-load apk into Windows Subsystem for Android <https://www.xda-developers.com/how-to-sideload-android-apps-on-windows-11/>`_
