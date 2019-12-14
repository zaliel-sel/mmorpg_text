# Introduction
This is a small script to help MMORPG players write long text blocks then break them out based on the maximum characters allowed by the box.

# Requirements
Python 3

# Usage
```
usage: mmorpg_text.py [-h] [-m MAX_CHARACTERS] [-e COMMAND_DECLARATIVE]
                  [-a APPEND_CHARACTER] [--version]
                  input

positional arguments:
  input                 String to break into constituent pieces

optional arguments:
  -h, --help            show this help message and exit
  -m MAX_CHARACTERS, --max-characters MAX_CHARACTERS
                        Maximum characters per string
  -e COMMAND_DECLARATIVE, --command-declarative COMMAND_DECLARATIVE
                        Indicates a character which informs the game textbox
                        that what follows is a command, such as "/" for emote
  -a APPEND_CHARACTER, --append-character APPEND_CHARACTER
                        Set the character which should be appended to strings
                        which continue beyond the max-characters value
  --version             show program's version number and exit
```

Argument            | Default
--------------------|-----------------
MAX_CHARACTERS      | 200
COMMAND_DECLARATIVE | `/`
APPEND_CHARACTER    | `+`

# Examples
All examples use the Unix (Linux/MacOS) terminal pattern. If using Windows, replace `./mmorpg_text.py` with `python mmorpg_text.py`.
 
## Basic Usage
In this basic example, we are limited to 50 characters per text box (default 200)
```
./mmorpg_text.py "The quick brown fox jumps over the lazy dog. The rain in Spain falls mainly in the plain." --max-characters=50

The quick brown fox jumps over the lazy dog. The+
rain in Spain falls mainly in the plain.
```
In the next example, we can change the APPEND_CHARACTER to something fancier. Note how the second sentence now begins entirely on the new line.
```
./mmorpg_text.py "The quick brown fox jumps over the lazy dog. The rain in Spain falls mainly in the plain." --max-characters=50 --append-character="=>"

The quick brown fox jumps over the lazy dog.=>
The rain in Spain falls mainly in the plain.
```
Chat box commands are automatically captured if they begin with `/` and end with the next space. For example, `/e`, `/emote`, and `/ChannelName` will all automatically appear on the next line if found.
```
mmorpg_text.py "/e walked into the room cautiously, her eyes scanning each object carefully, a flashlight in one hand, her knife in the other." --max-characters=50

/e walked into the room cautiously, her eyes+
/e scanning each object carefully, a flashlight+
/e in one hand, her knife in the other.
```

## Advanced Usage
The `--command-declarative` is a special character (or series of characters) that should appear at the beginning of each line. This can also be thought of as a "prefix code", as all new lines will appear with this character.

By default, the Command Declarative is the `/` key, which tells this program that what follows will be some kind of terminal command. The most common use case for this is `/e` or `/emote` which, in many games, is used to denote character action.

If `/` is the correct key for your game, _no action is required;_ this program will pick it up automatically. However, if your game uses a different character, such as the `$` key, you would change it like the following:
```
./mmorpg_text.py "$e walked into the room cautiously, her eyes scanning each object carefully, a flashlight in one hand, her knife in the other." --max-characters=50 --command-declarative="$"

$e walked into the room cautiously, her eyes+
$e scanning each object carefully, a flashlight+
$e in one hand, her knife in the other.
```
