# Installation of a Python system on your laptop (or desktop PC)

## Python 2 vs. Python 3
There are two major *Python* versions currently in use. *Python 2.7* and
*Python 3.7*. Unfortunately the two versions are *imcompatible* and
we will use *Python 3.7* in our course.

*Python 2.7* is the last version in the *Python 2.X* series and it
will only be maintained with bug fixes in the future. All new
developments will happen in the *Python 3.X* branch and I strongly
recommend to only use that in the future - especially for new scripts
and programs.

## Python 3.X installation
Python consists of a *core language* (see
[here](https://www.python.org/)) and many optional modules and
packages. For sceintific computing essential modules are
[numpy](http://www.numpy.org/) (data structures optimised for science
applications), [scipy](https://www.scipy.org/) (large collection of
software packages for science applications) and
[matplotlib](http://matplotlib.org/) (plotting package for scientific
data).

As the Python core and all major modules undergo permanent and quick
development, maintaining a coherent system manually can become
cumbersome. For scientific computing, well-maintained *distributions*
allow a very quick setup for *Python* in a scientific environment.
Updates are managed comfortably with dedicated *package managers*.

I made very good experience with the [Anaconda
distribution](https://www.anaconda.com/distribution/#download-section)
and I strongly recommend you
to install its current *3.7* version. It contains all packages we need in
class and it is available for the *Windows*, *Linux* and *Mac* operating
systems.

## Installation test
Please run the script ```check_heidelberg_python.py``` on your computer to
check whether you have a well-installed setup:

```bash
user$ python3 check_heidelberg_python_2019.py
............
----------------------------------------------------------------------
Ran 12 tests in 1.316s

OK
user$
```
Please contact me if you run into problems that you cannot resolve yourself.
