Cloud Sync
==========

|app| can synchronize your bookmarks, notes, labels, study pads, and workspaces
across multiple devices using Google Drive or Nextcloud.

Sync is automatic — once set up, changes are synchronized in the background
while the app is open, as well as when opening or exiting the app.

Requirements
------------

* Android 5.1 or newer
* A Google account (for Google Drive sync) or a Nextcloud server
* Internet connection

.. note::
   Google Drive sync is not available in the F-Droid build. If you installed
   |app| from F-Droid, you can use Nextcloud instead.

Setting Up Sync
---------------

#. Open the top left main menu (|hamburger|).
#. Tap ``Sync settings``.
#. Choose your sync adapter: **Google Drive** (default) or **Nextcloud**.
#. Toggle on the data categories you want to sync (Bookmarks, Workspaces).

When enabling sync for the first time:

* If **no sync data exists** in the cloud yet, your local data will be uploaded
  automatically.
* If **sync data already exists** (e.g. from another device), a dialog will
  appear with three options:

  * **Copy from Cloud to this device** — downloads the cloud data and replaces
    your local data with it.
  * **Copy from this device to Cloud** — replaces the cloud data with this
    device's local data.
  * **Cancel & disable synchronization** — cancels and disables sync for this
    category.

  A confirmation dialog will follow to make sure you understand the
  consequences.

Setting Up Nextcloud
^^^^^^^^^^^^^^^^^^^^

If using Nextcloud instead of Google Drive:

#. In Sync settings, change the ``Sync adapter`` to **Nextcloud**.
#. Enter your Nextcloud server URL, username, and password.
#. Optionally specify a folder path on the server.
#. Toggle on the data categories you want to sync.

What Gets Synced
----------------

**Bookmarks** (toggle: Bookmarks)
   Bookmarks, highlights, notes, labels, and study pads — for both Bible
   and non-Bible documents.

**Workspaces** (toggle: Workspaces)
   Workspace configurations, window layouts, and current document positions.

**Not synced:**
   Bible and commentary modules themselves are not synced.
   Download your modules separately on each device. App settings and preferences
   are also not synced.

How Sync Works
--------------

* Sync runs automatically approximately every 60 seconds while the app is in
  the foreground and device is online.
* Sync also runs when the app is opened and when exiting the app.
* Only changes since the last sync are uploaded — not the entire database each time.
* If two devices change the same item, the most recent change wins automatically
  (based on timestamps).

Multi-Device Usage
------------------

Each device is identified separately. When multiple devices are synced:

* Changes from all devices are merged automatically.
* If the same bookmark or workspace is modified on two devices between syncs,
  the last change (by timestamp) takes precedence.
* There is no manual conflict resolution — the process is fully automatic.

Resetting Sync
--------------

To disconnect from cloud sync:

#. Open ``Sync settings``.
#. Tap ``Sign Out``.
#. Confirm the reset.

This signs out, disables synchronization, and resets related settings. Your
local data is kept intact. You can set up sync again at any time.

Tips
----

Compacting Cloud Storage
^^^^^^^^^^^^^^^^^^^^^^^^

Over time, the sync data in the cloud can grow as incremental change patches
accumulate. To compact the cloud storage:

#. Make a :doc:`backup <backup_restore>` first, just in case.
#. On one device, open ``Sync settings`` and tap ``Sign Out``.
#. Set up sync again and choose **Copy from this device to Cloud**. This
   replaces the accumulated patches in the cloud with a clean snapshot.
#. On your other devices, sync will detect that the cloud data has changed.
   When prompted, choose **Copy from Cloud to this device** to restore from the
   clean snapshot.

Privacy and Security
--------------------

* **Google Drive:** |app| uses the app-specific ``AppData`` folder on Google
  Drive. It cannot access any other files on your Drive, and other apps cannot
  access |app|'s sync data.
* **Data sent:** Only your bookmarks, labels, notes, study pads, workspaces,
  and window configurations are uploaded — no personal information beyond what
  you explicitly create in the app.
* **Credentials:** Authentication credentials are stored only on the device
  and are never included in backups.

.. note::
   |app| developers are not responsible for any data loss or damage that may
   occur during the synchronization process. Regular :doc:`backups <backup_restore>`
   are recommended.
