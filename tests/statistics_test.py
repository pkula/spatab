from spatab.main.statistics import Statistics


def tests_statistic():
    statistics = Statistics()

    assert statistics.num_modified_lines == 0
    message = "spaTab modified 0 lines"
    assert str(statistics) == message

    statistics.increment

    assert statistics.num_modified_lines == 1
    message = "spaTab modified 1 lines"
    assert str(statistics) == message
