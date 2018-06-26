# st-checker

A fork of [st-checker](https://github.com/commoncriteria/st-checker)

This project derives a RelaxNG Schema for Security Targets based on a Protection Profile or Module XML document.

~~I also don't know what a RelaxNG Schema is.~~
I'm somewhat familiar with a RelaxNG Schema

This is currrently a WIP, and improvements are (always) coming.

## Dependencies

* [lxml](https://lxml.de/) from [pip](https://pypi.org/project/lxml/)

* Python 3+

* A desire/need to use my (buggy) program

## Instructions

1. Run `$ python3 st-checker.py <protection-file>`
2. ???
3. Profit.

### TODO

[~] Output the desired Schemas (This 'works' but the program is far from complete)

[ ] Work on Inconsistencies

[ ] Make the program not impossible to read and follow

[ ] Make it actually work

### Debugging

If you're reading this now, it probably means that my program is not working consistently. I'm trying to fix this.

Sidenote: this currently gets its rules from the operatingsystems repo, not sure if this is the ruleset I want to use, and it might work with a different ruleset. I'm not sure.

Any other bugs? Feel free to leave an issue on the issue tab on the [GitHub repo](https://www.github.com/AndroidKitKat/st-checker). I'll do my best to make sure any issues get sorted out.

#### License

This work is "licensed" under the [UNLICENSE](http://www.unlicense.org/). This puts my code into the public domain and allows you, the end user, change the license on this code, etc. Go bananas.