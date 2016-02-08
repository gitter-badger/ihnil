# IHNIL - I Hate Nested If Loops

## Description

Prounced: "eye-nil"  
For use on Python code modules. :snake:  
I hate nested "if" loops. They're ugly, they're slow, they've got to go.  
While there are *some* instances where they are necessary, let's see if we  
can get rid of all of the useless ones.  

## Usage

After installation, run via with the arguments below in the terminal:  

```
python3 reader.py [ -r/--read | -w/--read ] [ -h/--help ] filename  
```  

The default optional argument is ` -r / --read `.  
Currently only available for Python 3.  

## Development

This project has several phases listed below:  
- [X] Identify nested loop statements
- [X] Print results errors to the terminal
- [X] Add printout for error location values
- [X] Implement class to hold all parsed code & functions
- [X] Adjust argparse options to call needed class methods
- [ ] Parse "if" statements to identify improvements
- [ ] Improve nested "if" identifier accuracy
- [ ] Function to remove comment lines (to ID nested "if"s)
- [ ] Print improvements to the terminal
- [ ] Insert recommendations into the code
- [ ] Include string method identification support
- [ ] Include list method identification support
- [ ] Build auto editor for recommendations
- [ ] Develop PyPI distribution
- [ ] Identify unecessary stacked "if" statements (**long term**)
- [ ] Identify list comprehension options (**longER term**)

Other additions may be made to the list as the project develops.  

## Dependencies

- [argparse](https://docs.python.org/3.4/library/argparse.html#module-argparse)
- [os](https://docs.python.org/3.4/library/os.html#module-os)
- [tokenize](https://docs.python.org/3.4/library/tokenize.html#module-tokenize)
- [operator](https://docs.python.org/3.4/library/operator.html#module-operator)
- [itertools](https://docs.python.org/3.4/library/itertools.html#module-itertools)

## Contribution

Please adhere to ` pep8 ` standards when contributing to this project.  
- The official reference **style guide** can be found [here](https://www.python.org/dev/peps/pep-0008/)  
- The **command line tool** for Python files can be found [here](https://pypi.python.org/pypi/pep8)  

Pull requests will only be accepted through [Github](https://github.com/)  

## Credits

**John Forstmeier**, *primary author*, [@forstmeier](https://github.com/forstmeier)  

Copyright (c) 2015-2016 John Forstmeier  

Released under the [MIT License](https://github.com/forstmeier/pythonistics/blob/master/LICENSE.txt)  
