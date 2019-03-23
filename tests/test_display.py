# test_display.py
import pytest
from src import display


@pytest.mark.skip
def test_header(capfd):
    """ Testing the header """
    # call the function
    display.header()

    # set the exected output
    # row1 = str('+' * 50).join('\n')
    # row2 = f'{"+"}{"TO-DO App":^47}{"+"}'.join('\n')
    # row3 = str('+' * 50).join('\n')
    # expected = f'{row1}{row2}{row3}'

    row1 = '++++++++++++++++++++++++++++++++++++++++++++++++++\n'
    row2 = f'{"+"}{"TO-DO App":^48}{"+"}\n'
    row3 = '++++++++++++++++++++++++++++++++++++++++++++++++++\n'
    expected = row1 + row2 + row3
    print(expected)

    # get the captured out and err
    out, err = capfd.readouterr()
    assert expected == out
