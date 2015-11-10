from scorer import *

def test_Validator():
    assert isValidThrow(['20', '20', '20']) == True
    assert isValidThrow(['B', '20', '20']) == True
    assert isValidThrow(['DB', 'D20', 'T19']) == True
    assert isValidThrow(['23', '40', '1']) == False
    assert isValidThrow(['Y20', '12', '1']) == False
    assert isValidThrow(['T21', 'T1', '16']) == False