# CLI URL Shortener

A simple command-line URL shortener made with Python.

## Requirements

- Python 3.x
- No external libraries required.

## How to Run

Open a terminal in the folder containing `ls.py` and use:

```
python ls.py <command> <arguments>
```

The program stores saved links in `mem.txt`.

## Commands

### 1. Shorten a URL

Syntax:

```
python ls.py shorten <URL>
```

Example:

```
python ls.py shorten https://www.google.com
```

Creates an automatically generated code such as `link1`.

### 2. Shorten with an Alias

Syntax:

```
python ls.py shorten <URL> --alias <alias>
```

Example:

```
python ls.py shorten https://www.google.com --alias google
```

Creates a custom code.

**Warning:** Aliases cannot contain the character `` ` `` because it is used as a separator in `mem.txt`.

### 3. Resolve

Syntax:

```
python ls.py resolve <code>
```

Example:

```
python ls.py resolve link1
```

Opens the saved URL and increases its resolve count.

### 4. Delete

Syntax:

```
python ls.py delete <code>
```

Deletes the saved code and URL.

**Warning:** There is no undo option.

### 5. Count

Syntax:

```
python ls.py count <code>
```

Displays how many times the code has been resolved.

### 6. List

Syntax:

```
python ls.py list
```

Displays all saved codes and URLs.

### 7. Info

Syntax:

```
python ls.py info <code>
```

Displays the code, URL, and resolve count.

### 8. Clear

Syntax:

```
python ls.py clear
```

Deletes all saved links after confirmation.

**Warning:** This permanently deletes all saved links and resolve counts. There is no undo option.

### 9. Reset

Syntax:

```
python ls.py reset <code>
```

Resets the resolve count of a code to 0.

**Warning:** The previous resolve count cannot be recovered.

### 10. Search

Syntax:

```
python ls.py search <text>
```

Finds saved URLs containing the specified text.

### 11. Stats

Syntax:

```
python ls.py stats
```

Displays the total links, total resolves, and most used link.

### 12. Sort

Syntax:

```
python ls.py sort
python ls.py sort reversed
```

`sort` displays links from highest to lowest resolve count.

`sort reversed` displays links from lowest to highest resolve count.

**Note:** Sorting only changes the display order. It does not modify `mem.txt`.

### 13. Rename

Syntax:

```
python ls.py rename <old code> <new code>
```

Replaces an existing code name by the new given name.

This does not reset click count.

## Data Storage

Each saved link is stored in `mem.txt` as:

```
code`URL`count
```

Example:

```
link1`https://www.google.com`3
```

## Important Warnings

1. Do NOT manually edit `mem.txt`. The program expects each line to follow the format: ``code`URL`count`` and the last line existing and being empty.
2. Do NOT use the character `` ` `` in codes or URLs. It is used as a data separator.
3. Keep `mem.txt` with the program. If it is deleted or moved, the program may create a new empty file.
4. Back up `mem.txt` if the saved data is important. The program does not create automatic backups.
5. This is a LOCAL URL shortener. Codes such as `link1` are not public internet URLs. The program must have the saved data to resolve them.
