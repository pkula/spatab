import os
import pytest

from spatab.main.application import Application


@pytest.fixture()
def application():
    open('plik.txt', 'w')
    argv = ['-f', 'tabs', 'plik.txt']
    return Application(argv)


def test_change_line(application):
    line = "\t\tlorem ipsum"
    assert application.change_line(line) == "        lorem ipsum"

    argv = ['-f', 'spaces', 'plik.txt']
    application = Application(argv)

    line = "            lorem ipsum"
    assert application.change_line(line) == "\t\t\tlorem ipsum"

    line = "              lorem ipsum "
    assert application.change_line(line) == "\t\t\t  lorem ipsum "


def test_change(application):
    lines = [
        '\t\t lorem ipsum ',
        '\t nie lorem ipsum',
        'nie lorem ipsum',
        '\t lorem ipsum',
    ]
    new_lines = application.change(lines)
    data = [
        '         lorem ipsum ',
        '     nie lorem ipsum',
        'nie lorem ipsum',
        '     lorem ipsum',
    ]
    assert new_lines == data


def test_generate_second_filename(application):
    filename = 'test_file.py'
    open(filename, 'w')

    fil2 = application.generate_second_filename(filename)
    assert fil2 == f'{filename}(copy)'

    open(fil2, 'w')
    fil3 = application.generate_second_filename(filename)
    assert fil3 == f'{filename}(copy)(copy)'

    fil4 = application.generate_second_filename(fil2)
    assert fil4 == f'{filename}(copy)(copy)'

    if not os.path.isfile('ddddd'):
        assert 'ddddd' == application.generate_second_filename('ddddd')

    if os.path.isfile(filename):
        os.remove(filename)
    if os.path.isfile(fil2):
        os.remove(fil2)


def test_save(application):
    data1 = ['test_filename1', 'ljkdkfkdf']
    data2 = ['test_filename2', ['jkfdksdf', 'jfsdljkfdsljdsf']]
    data3 = ['test_filename3', ['jkdskdsfj\n', 'jfdkjfsdkjdsf\n']]

    application.save(data1, data2, data3)

    with open('test_filename1') as f:
        assert 'ljkdkfkdf' == f.readlines()[0]

    with open('test_filename2') as f:
        assert f.readlines()[0] == 'jkfdksdfjfsdljkfdsljdsf'

    with open('test_filename3') as f:
        raw = f.readlines()
        assert len(raw) == 2
        assert raw[0] == 'jkdskdsfj\n'
        assert raw[1] == 'jfdkjfsdkjdsf\n'

    if os.path.isfile('test_filename1'):
        os.remove('test_filename1')
    if os.path.isfile('test_filename2'):
        os.remove('test_filename2')
    if os.path.isfile('test_filename3'):
        os.remove('test_filename3')


def test_gues_intedance(application):
    data1 = ['test_filename1', ['    jkdskdsfj\n', '  jfdkjfsdkjdsf\n']]
    data2 = ['test_filename2', ['\t\tkdskdsfj\n', '\tjfdkjfsdkjdsf\n']]
    data3 = ['test_filename3', ['\t  kdskdsfj\n', '\tjfdkjfsdkjdsf\n']]
    application.save(data1, data2, data3)

    application.options.filename = 'test_filename1'
    assert application.gues_intedance() == 'spaces'

    application.options.filename = 'test_filename2'
    assert application.gues_intedance() == 'tabs'

    application.options.filename = 'test_filename3'
    assert application.gues_intedance() == 'unknown'

    if os.path.isfile('test_filename1'):
        os.remove('test_filename1')
    if os.path.isfile('test_filename2'):
        os.remove('test_filename2')
    if os.path.isfile('test_filename3'):
        os.remove('test_filename3')

def test_run(application):
    data = [
        '    ala ma kota\n',
        '        \n',
        '    lorem ipsum\n',
        '   ',
    ]
    application.save(["plik.txt", data])
    if os.path.isfile('plik.txt(copy)'):
        os.remove('plik.txt(copy)')
    argv = ['-f', 'tabs', 'plik.txt']
    application = Application(argv)
    assert os.path.isfile('plik.txt(copy)') == False
    application.run()
    with open('plik.txt', 'r') as reader:
        for i, line in enumerate(reader.readlines()):
            assert line == data[i]
    assert os.path.isfile('plik.txt(copy)') == True

    if os.path.isfile('plik.txt(copy)'):
        os.remove('plik.txt(copy)')

    argv = ['-f', 'spaces', '-r', 'plik.txt']
    application = Application(argv)
    assert os.path.isfile('plik.txt(copy)') == False
    application.run()
    assert os.path.isfile('plik.txt(copy)') == False
    data2 = [
        '\tala ma kota\n',
        '\t\t\n',
        '\tlorem ipsum\n',
        '   ',
    ]
    with open('plik.txt', 'r') as reader:
        for i, line in enumerate(reader.readlines()):
            assert line == data2[i]
    if os.path.isfile('plik.txt'):
        os.remove('plik.txt')
