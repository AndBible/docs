Reading Plans
=============
From:  https://github.com/AndBible/and-bible/wiki/Reading-Plans

Overview
--------

Reading plans are accessible via main menu (left) > Reading Plan.

On first access you select a plan and are taken to the Daily Reading screen for the first day.

The Done button will be enabled after pressing Speak or Passage for each passage, or after you've tapped each checkbox (which you might use if you're reading in a paper Bible). "Done" marks the current day as complete and if you are behind will take you to the next day's readings.


How to create a reading plan
----------------------------

Custom Reading Plans
----------------------------
It is possible to create a custom reading plan for use with AndBible.

Beginning in version 4.0 (September 2021), there is a new module format that can be used for reading plans. The .properties file remains the same, but the path in jsword/readingplan no longer works on Android 10+, so we have made a new way that reading plans can be imported like other commentaries and Bibles, in .zip format. The jsword/readingplan path will continue to work for Android versions lower than 10.

The .zip format
----------------------------
For a sample reading plan in .zip format, please see this file. This is the complete file that is ready to import into AndBible. It can be imported from "Backup & Restore" in the main menu, or from the Reading Plan screen 3-dot menu.

The zip compressed folder contains a mods.d and a modules directory. The mods.d folder contains the .conf file. The modules folder contains the .properties file, however, the modules directory often has a longer path of folders to the .properties file. See the .conf file "DataPath" property below for an example.

When you are done preparing the mods.d and modules folders, select the 2 folders together and compress them into a zip file. This is the zip file that needs to be imported to AndBible.

The .conf file
----------------------------
For a sample .conf file, please see this file.

This is the content for the "Ninety days" reading plan:

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
It's quite self-explanatory, but I will highlight a few things. The "Category" has to remain as "And Bible", and "ModDrv" needs to remain as in sample above. "Versification" default is always KJV, so that line really only needs to be provided if it's different. For more about versification, see here. The "AndBibleMinimumVersion" also needs to remain as 535 because that's when the zip format started to be supported. Earlier versions of AndBible will then be able to determine that this module is not supported.

The "AndBibleProvidesReadingPlan" is set to the file name that exists in the "DataPath" set at the start of the file.

If your reading plan is date-based you will need to add this line to the .conf file: AndBibleReadingPlanDateBased=true

The .properties file
----------------------------
You will need to create a file similar to the examples here which are the reading plans distributed with AndBible. The name of the file will be the name of the plan. The file extension must be .properties and you must place it on your mobile's sdcard in a folder named jsword/readingplan. Use a simple text editor to create the file e.g. Notepad++ and do not use something like Word. The file must contain a series of rows in the format day=reading1,reading2 E.g.

1=Gen.1, Matt.1
2=Gen.2, Matt.2
3=Gen.3, Matt.3
4=Ps.119
5=1Cor.1, Jude

It is possible to skip days e.g. if you do not wish to a reading at the weekend. E.g.

1=Gen.1, Matt.1
3=Gen.2, Matt.2

You can also add a date-based reading plan, which includes the month and day number for each day. The only difference of this type of plan from the regular plan, is that the date-based plan will always open at today's date by default. The regular plan opens the current day, which is the day up to where you are done reading. The file for a date-based plan must always begin the readings at 1=. Also, the date must be in the format of 3 letters for the month, then dash and month day number followed by semicolon (;). E.g.

1=Jan-1;Gen.1-2,Ps.1-2,Matt.1-2
2=Jan-2;Gen.3-4,Ps.3-5,Matt.3-4
3=Jan-3;Gen.5-6,Ps.6-8,Matt.5
...
146=May-26;Jos 12,Isa 16,2Tim 2
...
334=Nov-30;Est 7-8,Oba,Heb 3-5

As mentioned in the ".conf file" section, you will need to add this line to the .conf file: AndBibleReadingPlanDateBased=true

OSIS format references must be used and OSIS Bible book names must be used. These will be translated to the current language when displayed in AndBible. E.g. Gen.1,Matt.1-Matt.2,Ps.119.1-Ps.119.10

Example reading plans can be found here.

A full list of OSIS book names can be found here

Deuterocanonical Books
----------------------------
The default versification for reading plans is KJV. If you wish to include deuterocanonical books in your plan you must specify the versification in the properties file. However, this is not supported for the new zip format added in 4.0. See the ".conf file" section above for how to do this for zip format. E.g.:

Versification=Vulg
1=Sir.1-Sir.2
2=1Macc.1-1Macc.2
3=Bar.1-Bar.2

Set Start to Another Day
-------------------
If you started the readings on a previous day and have just switched to AndBible then select Menu from the Daily Reading screen and then select 'Set Start Date...'. You may then jump to 'Move the current day to a specific day' below to skip over readings you have already done.

Abandon Reading Plan
----------------------------
Press Menu/Reset from the Daily Reading screen.

Switch between Reading Plans
----------------------------
Select the first button in the toolbar when in the Daily Reading screen. By this means it is possible to use several plans simultaneously.

Preview a plans readings
----------------------------
When in the Daily Reading screen select the second button in the toolbar.

Go to a specific day
----------------------------
When in the Daily Reading screen select the second button in the toolbar. Then select the required day from the list.

Move the current day to a specific day
This is useful if you have been using a reading plan externally from AndBible. A sequence of actions might be i) select plan ii) Set start date to another day (as above) iii) Move the current day to a specific day (as below)

Version 3.3 and earlier: Go to the day prior to the desired day as described in the above paragraph. Select Menu/Done (not the normal Done button at the bottom) this bypasses checks and marks the current day as Done and the next day will become the current day.

Note: Starting in 4.0-beta (and 4.0 stable), you will be able to simply go to 3-dot menu on top right, and click "Set as current day".

