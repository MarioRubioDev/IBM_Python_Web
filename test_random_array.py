import pytest
import random_array as r
list = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

@pytest.mark.parametrize(
        "number,expected",
        [
        (1,1),
        (2,2),
        (3,3)
        ]
)

def test_makeArray(number, expected):
    myArrayTest = r.makeArray(number)
    assert len(myArrayTest) == expected 
    for i in range(number):
        assert len(myArrayTest[i]) == expected

def test_randomNumber():
    randomListTest = r.randomNumber(20)
    assert max(randomListTest)<10
    assert min(randomListTest)>=0
    assert len(randomListTest) == 20

def test_sumRows():
    assert r.sumRows(list) == [10,10,10,10]

def test_sumColumns():
    assert r.sumColumns(list) == [4,8,12,16]