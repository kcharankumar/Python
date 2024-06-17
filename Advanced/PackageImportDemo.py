"""
A directory mypackage is created.  Added a file named __init__.py.  In that two python files are created
(a)  module1.py (b) module2.py.  Each module / python file has one function named module1Function()
and module2Funtion().

In this program, we are importing module1 and module2 from the package mypackage and calling the methods
of each module.  G

Grouping of related modules is a package so that only that package can be imported.
"""

from mypackage import module1, module2


print (module1.module1Function())
print(module2.module2Function())
