import pynjsla
from pynjsla.njsla import njsla_split
from pynjsla.njsla_batch import njsla_batch_split

def test_njsla_split_exists():
    assert njsla_split is not None

def test_njsla_batch_split_exists():
    assert njsla_batch_split is not None