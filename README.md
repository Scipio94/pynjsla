![PyPI - Version](https://img.shields.io/pypi/v/pynjsla) ![Static Badge](https://img.shields.io/badge/python-3.10-blue) [![Run tests](https://github.com/Scipio94/pynjsla/actions/workflows/tests.yml/badge.svg)](https://github.com/Scipio94/pynjsla/actions/workflows/tests.yml)

# pynjsla

Python package that splits Individualized Score Reports (ISR) PDF exports from the New Jersey Student Learning Assessment (NJSLA) into a two page PDF export and labels output by the New Jersey Student ID (SID) extracted from the PDF.

## Installation

~~~python
pip install pynjsla
~~~

### Usage

~~~python
import pynjsla
from pynjsla.njsla import njsla_split

njsla_split('C:\Documents\Reports\NJSLA_ISR.pdf')
~~~

The output will be _x_ number of exported PDFs with the output label being the ID from the NJSLA ISRs.

### Documentation

| Input      | Data Type | Documentation                  |
| ---------- | --------- | ------------------------------ |
| pdf_object | string    | The file path of the NJSLA ISR |
