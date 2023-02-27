# Hamurabi

Hammurabi is a classic (and very simple) resource allocation game, which is
here transcribed to Python from David Ahl's original BASIC version, published
in his 1978 volume ["BASIC Computer Games"]
(https://www.atariarchives.org/basicgames/index.php). As an aside, this
book is an excellent source of prompts for people who want to write a program,
but don't know what program they want to write.

The current project is an exercise in refactoring. If you want to demonstrate
refactoring, of course it helps to start with code that is badly in need of
help, and the file hamurabi.py at the tag "step_0" is probably the worst code
that I could have generated without trying to sit down and intentionally write
horrible code.


## Step 0: Original transcription from BASIC to Python
The phases of the refactoring will be marked by successive tags. In the first
tag, "step_0", I present the original transcription from Ahl's BASIC version.
(The BASIC code is included for reference, and can be viewed in a slightly
difficult scan[here](https://www.atariarchives.org/basicgames/showpage.php?page=79))
This python code runs and more or less works. I've noted two minor bugs, which I
do not intend to fix at this phase - fixing bugs in untested code seems to me
like a foolish exercise!
