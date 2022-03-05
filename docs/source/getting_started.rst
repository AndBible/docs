Getting Started
===============

Installation
------------

There are four main ways to install AndBible. You can install AndBible
using the Google Play Store version, the F-Droid version, the Amazon app
store and directly from GitHub releases.

Google Play Store
-----------------

` <https://play.google.com/store/apps/details?id=net.bible.android.activity>`__

Click on the link above and install the application.

F-Droid
-------

` <https://f-droid.org/packages/net.bible.android.activity/>`__

Click on the F-Droid app link above and install the app.

Amazon App Store
----------------

` <http://www.amazon.com/Martin-Denham-And-Bible/dp/B004Z2KKYK>`__

Click on the Amazon link above and install the application.

GitHub Releases
---------------

`AndBible GitHub
Releases <https://github.com/AndBible/and-bible/releases/latest>`__

Go to the link above and download the .apk file in the “Assets”
sub-menu. Then, click on the downloaded file and add the necessary
permissions to the browser you are using. Finally, click “Install”

Windows 11 setup
-----------------

To run AndBible on windows 11:

This may be a bit technical if you are outside the US or not on Windows 11 beta. It involves downloading the Windows Subsystem for Android (WSA), running a command to install it, starting Windows Subsystem for Android, enabling developer mode, downloading the apk from GitHub releases, and installing the app with adb.

Install WSA following these instructions:
 https://www.xda-developers.com/how-to-run-android-apps-on-any-windows-11-pc/

Set up adb:
 https://www.xda-developers.com/install-adb-windows-macos-linux/

Download the APK from GitHub releases:
 https://github.com/AndBible/and-bible/releases/latest

How to sideload apps on WSA:
 https://www.xda-developers.com/how-to-sideload-android-apps-on-windows-11/


Comparing verses
----------------

To do.

Changing the look and feel
--------------------------

You can use the workspace "All Text Options" to change the font size and font colors of document texts. You can access these from the kabab menu on the top right (aka three vertical dots).
Alternatively you can use the individual window text options to override the workspace settings. Tap and hold the square window icon at the bottom and choose "Text Options" then "All Text Options".


For things that can not be changed through these menus, like the color of certain texts within a module, e.g. Strong's numbers, you can code the color in the style.css file located within  a zip package. You can use HiSB Bible module to see the structure and placement of this file, it should be located in the modules/texts/ztext/hisb/style directory.
Once coded you simply use the "Load From Zip" function under Backup/Restore section of the main menu.

