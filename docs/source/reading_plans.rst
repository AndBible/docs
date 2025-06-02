Reading Plans
=============

Reading plans provide a pre-determined schedule of scripture readings.
To access reading plans, navigate to the left main menu (|hamburger|) and choose
`Reading Plan`.

When first accessing `Reading Plan`, you will be prompted to select a plan. After
selecting a plan, you will be shown the Daily Reading screen for the first day
of the reading plan's schedule.

Clicking the `Done` button will take you to the next day's reading schedule.
Note: The `Done` button will only be enabled after pressing either the `Speak`
or `Passage` buttons for each passage that is listed. Alternatively, you can tap
the check next to each passage to enable the `Done` button (manually checking
the check marks can be useful if you're reading in a paper Bible).

|reading_plan_daily_readings| |reading_plan_list| |reading_plan_days|

.. |reading_plan_list| image:: /images/reading_plan_daily_readings.png
   :width: 32%

.. |reading_plan_days| image:: /images/reading_plan_days.png
   :width: 32%

.. |reading_plan_daily_readings| image:: /images/reading_plan_list.png
   :width: 32%

Abandon Reading Plan
--------------------

Press the vertical 3-dot menu from the `Daily Reading` screen, and click `Reset`.
Next time you return to the same `Reading Plan`, the progress will be reset to day 1.

Switch Between Reading Plans
----------------------------

From the `Daily Reading` screen, click the first button in the top lef of the
toolbar. This will let you select a different reading plan. You can return to
the original reading plan and your progress will remain where you left it.
In other words, it is possible to use several reading plans simultaneously.

Preview Reading Plans or Go To Specific Day
-------------------------------------------

When in the `Daily Reading` screen, click the second button in the top left of
the toolbar. You will see a list of daily readings. Clicking on a daily reading
will bring you to `Daily Reading` screen for that specific day.

Changing Reading Plan Start Date
--------------------------------

If you started the readings on a previous day and have just switched to |app|,
then select the vertical 3-dot menu from the `Daily Reading` screen and
click `Set Start Date...` to pick a specific start date or click `Set as current day...`
to set the start date of the reading plan to today's date.

Set Specific Reading Plan Day to Today's Date
---------------------------------------------

This is useful if you have been reading outside of |app|. To
move the current reading plan day to today's date:

#. Open the `Daily Reading` screen for the reading plan you would like to adjust
#. Go to the specific day of the reading plan you want to set to today's date.
#. Click the top right 3-dot menu
#. Click `Set as current day`.

.. note::

    For |app| Versions 3.3 and earlier: Go to the day prior to the desired day
    as described above, click  `Menu -> Done` (not the normal Done button at the bottom)
    this bypasses checks and marks the current day as Done and the next day will become
    the current day.

Custom Reading Plans
====================

It is possible to create your own custom reading plan for use with |app|.

.. note::

    If you create a reading plan that you think would be useful for other |app| users,
    feel free to share it in our :ref:`Matrix or Telegram <support:General Questions>`
    chat!

The .zip Reading Plan Format
----------------------------

For a sample reading plan in .zip format, please see
`this file <https://andbible.github.io/data/andbible/beta/zip/NinetyDaysReadingPlan.zip>`_.
This is a complete reading plan file that is ready to be imported into |app|.
It can be imported using the :doc:`/backup_restore` functionality in the main menu
(|hamburger|), or from the top right vertical 3-dot menu in the `Reading Plan` screen.

The compressed zip folder contains two directories:

    - :code:`mods.d` (Contains the :code:`.conf` file)
    - :code:`modules` (Contains the :code:`.properties` file)

      - Note: The :code:`modules`` directory often has a longer path of folders
      - leading to the :code:`.properties` file. See the :code:`.conf` file
        :code:`DataPath` property below for an example.

Once you are done preparing the :code:`mods.d` and :code:`modules` folders,
compress the 2 folders into a single :code:`.zip` file. This zip file can then
be imported to |app|.

.. hint::
  Use a simple text editor to create the file e.g. Notepad++ and do not use
  something like Word.

The :code:`.conf` file
----------------------

For a sample :code:`.conf` file, please see
`this file <https://andbible.github.io/data/andbible/beta/mods.d/NinetyDaysReadingPlan.conf>`_.

This is the content of the `Ninety days` reading plan :code:`.conf` file:

.. code-block::

    [NinetyDaysReadingPlan]
    DataPath=./modules/texts/ztext/NinetyDaysReadingPlan/
    Version=1.0
    Description=Through the Bible in 90 days
    ShortPromo=Challenge yourself and read through the entire Bible in 90 days
    DistributionLicense=Public Domain
    Category=And Bible
    ModDrv=RawGenBook
    Versification=KJV
    AndBibleMinimumVersion=535
    AndBibleProvidesReadingPlan=NinetyDaysReadingPlan.properties

A few notes about the contents of this file:

  - :code:`Category` must be :code:`And Bible`
  - :code:`ModDrv` must be :code:`RawGenBook`
  - The default :code:`Versification` is always KJV, so this only needs to be
    provided if you want a versification other than KJV. For more about
    versification, see `here <https://wiki.crosswire.org/Alternate_Versification>`_.
  - :code:`AndBibleMinimumVersion` must be :code:`535` because that's the version
    of |app| when the zip format was first supported. Earlier versions of |app|
    will use this to determine that this module is not supported.
  - :code:`AndBibleProvidesReadingPlan` should be set to the file name that exists
    in the :code:`DataPath` set at the start of the file.

.. note::

  If your reading plan is date-based you will need to add the following line
  to the :code:`.conf` file:

  :code:`AndBibleReadingPlanDateBased=true`

The :code:`.properties` file
----------------------------

You will need to create a :code:`.properties` file similar to the examples
`here <https://github.com/AndBible/and-bible/tree/master/app/src/main/assets/readingplan>`_
The name of the file will be the name of the plan. The file extension must be
:code:`.properties` and you must place it a sub-directory under the :code:`modules`
directory. These will be translated to the current language when displayed in
|app|. The file must contain a series of rows in the following format:

.. code-block::

    1=Gen.1, Matt.1
    2=Gen.2, Matt.2
    3=Gen.3, Matt.3
    4=Ps.119
    5=1Cor.1, Jude

It is possible to skip days. For example, if you do not wish to have a reading on the
weekend:

.. code-block::

    1=Gen.1, Matt.1
    3=Gen.2, Matt.2

You can also add a date-based reading plan, which includes the month and day
number for each day. The date-based plan will always open at today's date by
default (The regular plan opens the current day, which is the last day you haven'take
yet completed). For a date-based plan, the :code:`.properties` file must always
begin the readings at :code:`1=`, and the date must be in the format of 3 letters
for the month, then a dash and then a month day number followed by semicolon (;).
For example:

.. code-block::

    1=Jan-1;Gen.1-2,Ps.1-2,Matt.1-2
    2=Jan-2;Gen.3-4,Ps.3-5,Matt.3-4
    3=Jan-3;Gen.5-6,Ps.6-8,Matt.5
    ...
    146=May-26;Jos 12,Isa 16,2Tim 2
    ...
    334=Nov-30;Est 7-8,Oba,Heb 3-5

As mentioned in `the .conf file`_ section, you must add the following line to
the :code:`.conf` file when using a date-based plan:

:code:`AndBibleReadingPlanDateBased=true`

Example reading plans can be found
`here <https://github.com/AndBible/and-bible/tree/master/app/src/main/assets/readingplan>`_.

.. note::

    `OSIS <https://crosswire.org/osis/>`_ format references and Bible
    book names must be used in reading plans.

    A full list of OSIS book names can be found
    `here <https://wiki.crosswire.org/OSIS_Book_Abbreviations>`_.

.. caution::

    Using an Android version older than 10?

    If you are creating a reading plan to be used on an Android device older than
    version 10, **and** you plan to include deuterocanonical books in your reading
    plan, you must specify the versification in the :code:`.properties` file:

    .. code-block::

        Versification=Vulg
        1=Sir.1-Sir.2
        2=1Macc.1-1Macc.2
        3=Bar.1-Bar.2

    The default versification for reading plans is `KJV`.

.. note::
    Beginning in version 4.0, the :code:`jsword/readingplan` module format for
    reading plans is deprecated for use with Android 10+ since the :code:`jsword/readingplan`
    path no longer works on Android 10+. The new :code:`.zip` format (described above)
    can be imported like any other |app| module.

