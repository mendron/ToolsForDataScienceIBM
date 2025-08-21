import math
import pytest
from tools4ds.stats import summarize, Stats

def test_summarize_basic():
    s = summarize([1, 2, 3, 4])
    assert isinstance(s, Stats)
    assert s.count == 4
    assert s.mean == 2.5
    assert s.median == 2.5
    assert math.isclose(s.stdev, 1.2909944487358056, rel_tol=1e-9)  # sample stdev
    assert s.min == 1
    assert s.max == 4

def test_summarize_one_value_has_none_stdev():
    s = summarize([42])
    assert s.count == 1
    assert s.stdev is None

def test_summarize_raises_on_empty():
    with pytest.raises(ValueError):
        summarize([])
