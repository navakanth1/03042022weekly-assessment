import operations
import pytest
import cmath as m

@pytest.fixture
def setUp():
    a = 25
    yield
    a = 0

@pytest.mark.skip
def test_sqrt(setUp):
    answer = m.sqrt(a)
    result = operations.result1(a)
    assert answer == result

def test_Quadratic():
    a = 3
    b = 2
    c = 1
    result = operations.Quadratic(a,b,c)
    assert result == (b*b)-(4*a*c)

@pytest.mark.xfail
@pytest.mark.parametrize("a,b",[(33,91.4),(20,68),(40,105),(3,35)])
def test_degree(a,b):
    answer = operations.Degree(a)
    assert answer == b

@pytest.mark.xfail
@pytest.mark.parametrize("a,b",[(5,"Positive"),(-5,"Negative"),(0,0),(5,0)])
def test_number(a,b):
    result = operations.Number(a)
    assert result == b


@pytest.mark.parametrize("a,b",[(5,15),(8,36)])
def test_Sum(a,b):
    result = operations.Sum(a)
    assert result == b