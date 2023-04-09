Getting Started
===============

Installation
------------

There are four main ways to install |app|. You can install |app|
using the Google Play Store version, the F-Droid version, the Amazon app
store and directly from GitHub releases.

Google Play Store
-----------------

.. image:: /images/google-play-badge.png
   :width: 200
   :target: https://play.google.com/store/apps/details?id=net.bible.android.activity

Click on the link above and install the application.

F-Droid
-------

.. image:: https://gitlab.com/fdroid/artwork/-/raw/master/badge/get-it-on-en-us.png
   :width: 200
   :target: https://f-droid.org/packages/net.bible.android.activity/

Click on the F-Droid app link above and install the app.

Amazon App Store
----------------

.. image:: /images/amazon-badge.png
   :width: 200
   :target: http://www.amazon.com/Martin-Denham-And-Bible/dp/B004Z2KKYK

Click on the Amazon link above and install the application.

GitHub Releases
---------------

`GitHub Releases <https://github.com/AndBible/and-bible/releases/latest>`_

Go to the link above and download the .apk file in the “Assets”
sub-menu. Then, click on the downloaded file and add the necessary
permissions to the browser you are using. Finally, click “Install”

Windows 11 setup
-----------------

To run |app| on windows 11:

This may be a bit technical if you are outside the US or not on Windows 11 beta. It involves downloading the Windows Subsystem for Android (WSA), running a command to install it, starting Windows Subsystem for Android, enabling developer mode, downloading the apk from GitHub releases, and installing the app with adb.

Install WSA following these instructions:
 https://www.xda-developers.com/how-to-run-android-apps-on-any-windows-11-pc/

Set up adb:
 https://www.xda-developers.com/install-adb-windows-macos-linux/

Download the APK from GitHub releases:
 https://github.com/AndBible/and-bible/releases/latest

How to sideload apps on WSA:
 https://www.xda-developers.com/how-to-sideload-android-apps-on-windows-11/


Changing the look and feel
--------------------------

You can use the workspace "All Text Options" to change the look and feel of document texts. You can access these options from the kabab menu on the top right (aka three vertical dots).
Use this menu to adjust various |app| appearance options including font size and type, text and background colors, toggling words of Christ in red, and more.

When using multiple windows, you can use the individual window text options to override current workspace settings. Tap and hold the square window icon at the bottom for the window whose settings you wish to customize.  Choose "Text Options" then "All Text Options".  This will open the menu to configure |app|'s' appearance for that specific window.

.. image:: ./images/multi_window_text_options.png

For things that can not be changed through these menus, like the color of certain texts within a module, e.g. Strong's numbers, you can code the color in the style.css file located within  a zip package. You can use HiSB Bible module to see the structure and placement of this file, it should be located in the modules/texts/ztext/hisb/style directory.
Once coded you simply use the "Load From Zip" function under Backup/Restore section of the main menu.
