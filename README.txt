CLI URL SHORTENER
=================

A simple command-line URL shortener made with Python.

REQUIREMENTS
============
- Python 3.x
- No external libraries required.

HOW TO RUN
==========
Open a terminal in the folder containing main.py and use:

    python main.py <command> <arguments>

The program stores saved links in mem.txt.


COMMANDS
========

1. SHORTEN A URL
----------------
Syntax:
    python main.py shorten <URL>

Example:
    python main.py shorten https://www.google.com

Creates an automatically generated code such as "link1".


2. SHORTEN WITH AN ALIAS
------------------------
Syntax:
    python main.py shorten <URL> --alias <alias>

Example:
    python main.py shorten https://www.google.com --alias google

Creates a custom code.

WARNING:
Aliases cannot contain the character ` because it is used as a separator
in mem.txt.


3. RESOLVE
----------
Syntax:
    python main.py resolve <code>

Example:
    python main.py resolve link1

Opens the saved URL and increases its resolve count.


4. DELETE
---------
Syntax:
    python main.py delete <code>

Deletes the saved code and URL.

WARNING:
There is no undo option.


5. COUNT
--------
Syntax:
    python main.py count <code>

Displays how many times the code has been resolved.


6. LIST
-------
Syntax:
    python main.py list

Displays all saved codes and URLs.


7. INFO
--------
Syntax:
    python main.py info <code>

Displays the code, URL, and resolve count.


8. CLEAR
--------
Syntax:
    python main.py clear

Deletes all saved links after confirmation.

WARNING:
This permanently deletes all saved links and resolve counts.
There is no undo option.


9. RESET
--------
Syntax:
    python main.py reset <code>

Resets the resolve count of a code to 0.

WARNING:
The previous resolve count cannot be recovered.


10. SEARCH
---------
Syntax:
    python main.py search <text>

Finds saved URLs containing the specified text.


11. STATS
--------
Syntax:
    python main.py stats

Displays the total links, total resolves, and most used link.


12. SORT
--------
Syntax:
    python main.py sort
    python main.py sort reversed

"sort" displays links from highest to lowest resolve count.

"sort reversed" displays links from lowest to highest resolve count.

NOTE:
Sorting only changes the display order. It does not modify mem.txt.


DATA STORAGE
============
Each saved link is stored in mem.txt as:

    code`URL`count

Example:

    link1`https://www.google.com`3


IMPORTANT WARNINGS
==================

1. Do NOT manually edit mem.txt.
   The program expects each line to follow the format:
       code`URL`count

2. Do NOT use the character ` in codes or URLs.
   It is used as a data separator.

3. mem.txt contains saved URLs in plain text.
   Do not store sensitive URLs containing passwords, tokens, or private data.

4. Keep mem.txt with the program.
   If it is deleted or moved, the program may create a new empty file.

5. Back up mem.txt if the saved data is important.
   The program does not create automatic backups.

6. This is a LOCAL URL shortener.
   Codes such as "link1" are not public internet URLs.
   The program must have the saved data to resolve them.
