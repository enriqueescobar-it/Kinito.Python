# ok if you need a multifunction device
from Section01_SOLID.InterfaceSegregationPrinciple.OldFashionedPrinter import OldFashionedPrinter


# same for Fax, etc.
printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
printer.scan(123)  # oops!
