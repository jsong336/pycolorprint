from setuptools import find_packages

print(find_packages())
from pycolorprint import ColorPrinter as c

c.print("""
    [hello! this is red:red]
""")

c.print("""
    [hello! this is bold:bold]
""")