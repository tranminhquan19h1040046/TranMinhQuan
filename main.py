import pytest


def check_BCD_number(a):
    n = str(a)
    if n == '0000' or n == '0001' or n == '0010' or n == '0011' or n == '0100' or n == '0101' or n == '0110' or n == '0111' or n == '1000' or n == '1001':
        return True
    return False


@pytest.mark.parametrize("a ,check", [(1000, True), (1111, False), (211213, False)])
# Press the green button in the gutter to run the script.
def test_fnc(a, check):
    assert check == check_BCD_number(a)
