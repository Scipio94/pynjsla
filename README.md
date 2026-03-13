![PyPI - Version](https://img.shields.io/pypi/v/pynjsla) ![Static Badge](https://img.shields.io/badge/python-3.10-blue) [![Run tests](https://github.com/Scipio94/pynjsla/actions/workflows/tests.yml/badge.svg)](https://github.com/Scipio94/pynjsla/actions/workflows/tests.yml)

# pynjsla

Python package that splits Individualized Score Reports (ISR) PDF district level exports from the New Jersey Student Learning Assessment (NJSLA) into a two page PDF student level export and labels output by the New Jersey Student ID (SID) extracted from the PDF for SIS or database upload.

- For single ISR file processing use the ***njsla_split*** library.
- For batch ISR file processing use the ***njsla_batch_split*** library

## njsla_split

### Installation

```python
pip install pynjsla
```

#### Usage

```python
import pynjsla
from pynjsla.njsla import njsla_split

njsla_split('C:\Documents\Reports\NJSLA_ISR.pdf')
```

The output will be _x_ number of exported PDFs with the output label being the ID from the NJSLA ISRs.

#### Documentation

| Input      | Data Type | Documentation                  |
| ---------- | --------- | ------------------------------ |
| pdf_object | string    | The file path of the NJSLA ISR |

## njsla_batch_split

#### Usage

```python
import pynjsla
from pynjsla.njsla_batch import njsla_batch_split

njsla_batch_split('C:\Documents\NJSLA_Folder')
```

The output will be _x_ number of exported PDFs with the output label being the ID from the NJSLA ISRs.

#### Documentation

| Input           | Data Type | Documentation                                          |
| --------------- | --------- | ------------------------------------------------------ |
| pdf_file_folder | string    | The file path of the folder location of the NJSLA ISRs |
