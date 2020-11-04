# Plugy Stash Organizer
## What is it?
As the name implies, this is a python script to organize your PlugY stashes. You can load either a shared (.sss) or personal (.d2x) stash file, and the script will more-or-less-neatly organize the stash.
## How do I use it?
Simply run the main.py file. A dialog box should pop up prompting you for the stash file. Point it to the stash file you want to organize, and click OK. Assuming the script doesn't throw any errors, you're done.
## What settings can I tweak?
The Settings.ini file contains some settings for how the script acts.

BackupStashFile = 1 (default) will make the script back up your old stash file, appending "OLD" to the end. I do not recommend that you change this.

IgnoreFirstXPages = X will ignore the first X pages of the stash. These will not be touched in any way, and the items within them will not be sorted. Useful for having things such as stash pages of skillers, items with specific properties, etc, since the script can only sort by very general properties (item type, rarity, etc).

UnifySets will put different set items on the same page if set to 1. If you want each set to have its own page, keep it at 0.
## I want to change the order of the items in the organized stash, or which items go into which pages!
I tried to make the script readable and fairly easy to modify. Do as you please with it. Most of the relevant code for sorting item groups is in the to_groups() method in main.py. If you wish to change or add item whole item categories you will also need to edit item_data.py.
## I want the script to sort items by properties!
No can do. The script doesn't parse anything beyond the most basic item data. It would be far too much work to do so, and I have no interest in doing it. Either keep some manually sorted pages using the IgnoreFirstXPages setting, or modify the code yourself.
## I want the script to tell me which grail items I'm missing!
See above.