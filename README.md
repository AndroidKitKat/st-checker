# st-checker

  

This project derives a RelaxNG Schema for Security Targets based on a Protection Profile or Module XML document.

~~I also don't know what a RelaxNG Schema is.~~ 
I'm somewhat familiar with a RelaxNG Schema

This is currrently a WIP, and improvements are (always) coming.

### Instructions:
1. Run `config.py` to generate a `config.yml`
2. Run `$ python st-checker.py <protection-file>`
3. ???
4. Profit. 

#### Debugging
If you have problems with `st-checker.py` thinking you are on Windows and you aren't on Windows, then edit  `config.yml` to reflect that. The only time I *think* this might happen is if you're using the **Windows Subsystem for Linux**. 

Sidenote: this currently gets its rules from the operatingsystems repo, not sure if this is the ruleset I want to use, and it might work with a different ruleset. I'm not sure. 

Any other bugs? Feel free to leave an issue on the issue tab on the [GitHub repo](https://www.github.com/AndroidKitKat/st-checker). I'll do my best to make sure any issues get sorted out. 

#### License
This work is "licensed" under the [UNLICENSE] (http://www.unlicense.org/). This puts my code into the public domain and allows you, the end user, change the license on this code, etc. Go bananas.