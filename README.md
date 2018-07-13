# st-checker

A fork of [st-checker](https://github.com/commoncriteria/st-checker)

This project derives a RelaxNG Schema for Security Targets based on a Protection Profile or Module XML document.

~~I also don't know what a RelaxNG Schema is.~~
I'm somewhat familiar with a RelaxNG Schema

This is currrently a WIP, and improvements are (always) coming.

## Dependencies

* [lxml](https://lxml.de/) from [pip](https://pypi.org/project/lxml/)

* Python 3+

## Instructions

1. Run `$ python3 python/input2txt.py <protection profile>`
2. Run `$ python3 python/st-checker.py`
3. ???
4. Profit.

I know that this method of execution isn't ideal in any sense, but I am unable to execute both using a Makefile or a shell script for ease of use.

### TODO

[~] Output the desired Schemas (This 'works' but the program is far from complete) Still verifying the RelaxNG part, not 100% consistent.

[X] Make it actually work

[ ] Improve execution and accuracy

[ ] Clean up codebase

### Debugging

If you're reading this now, it probably means that my program is not working consistently. I'm trying to fix this.

Sidenote: this currently gets its rules from the operatingsystems repo, not sure if this is the ruleset I want to use, and it might work with a different ruleset. I'm not sure.

Any other bugs? Feel free to leave an issue on the issue tab on the [GitHub repo](https://www.github.com/AndroidKitKat/st-checker/issues). I'll do my best to make sure any issues get sorted out.