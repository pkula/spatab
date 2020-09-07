import os
from spatab.main.options import Options
from spatab.exceptions import BadChooseException


def test_create_options():
    open('plik.txt', 'w')

    argv = ['-f', 'tabs', 'plik.txt']
    option = Options(argv)

    option._from == 'tabs'
    option.tab_chars == 4
    option.replace == False

    option.from_chars == '\t'
    option.to_chars == '    '
    option.filename == 'plik.txt'

    argv = ['-t', '7', '-f', 'spaces', 'plik.txt']
    option = Options(argv)

    option._from == 'tabs'
    option.tab_chars == 7
    option.replace == False

    option.from_chars == '    '
    option.to_chars == '\t'

    argv = ['-r', 'jf', '-t', 7, '-f', 'spaces', 'plik.txt']
    try:
        Options(argv)
        assert False
    except BadChooseException:
        pass

    argv = ['-r', '-t', 7, '-f', 'space', 'plik.txt']
    try:
        Options(argv)
        assert False
    except BadChooseException:
        pass

    argv = ['-r', '-t', 'jdkfj', '-f', 'spaces', 'plik.txt']
    try:
        Options(argv)
        assert False
    except ValueError:
        pass

    if os.path.isfile('plik.txt'):
        os.remove('plik.txt')
