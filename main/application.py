"""Module containing the application logic for spaTab."""
import os
import tokenize

from spatab.main.options import Options
from spatab.main.statistics import Statistics


class Application:
    """Abstract our application into a class."""

    def __init__(self, argv):
        """Initialize our application. argv without scriptname = argv[1:]"""
        self.options = Options(argv)
        self.statistics = Statistics()

    def run(self):
        """This function is main function - return a table with new lines and update stats"""
        filename = self.options.filename
        with open(filename, 'rb') as f:
            encoding, _ = tokenize.detect_encoding(f.readline)

        with open(filename, encoding=encoding) as f:
            if not self.options._from:
                intendancy = self.gues_intedance()
                self.only_report_exit_message
                return
            else:
                lines = f.readlines()
                new_lines = self.change(lines)
                if self.options.replace == True:
                    self.save([self.options.filename, new_lines])
                else:
                    self.save([filename, new_lines], [self.generate_second_filename(filename), lines])
                self.exit_message

    def generate_second_filename(self, filename):
        while os.path.isfile(filename):
            filename += '(copy)'
        return filename

    def gues_intedance(self):
        with open(self.options.filename) as f:
            lines = f.readlines()
        n_tabs = 0
        n_spaces = 0
        for line in lines:
            while line[0] == ' ' or line[0] == '\t':
                if line[0] == ' ':
                    n_spaces += 1
                elif line[0] == '\t':
                    n_tabs += 1
                line = line[1:]

        if n_tabs > 0 and n_spaces == 0:
            return 'tabs'
        elif n_spaces > 0 and n_tabs == 0:
            return 'spaces'
        else:
            return 'unknown'

    def save(self, *data):
        """This function get a tables save([filename,table_data], [filename2, table_data2])
        table data to the file filename
        """
        for record in data:
            with open(record[0], 'w') as writer:
                for line in record[1]:
                    writer.write(line)

    def change(self, lines):
        """This function takes table and return table with changed line and update stats in change line"""
        new_lines = []
        for line in lines:
            new_lines.append(self.change_line(line))
        return new_lines

    def change_line(self, line):
        """This function change line if it have to changed and return line after changing"""
        n = 0
        copy_line = line
        while len(self.options.from_chars) <= len(copy_line) and copy_line[:len(
                self.options.from_chars)] == self.options.from_chars:
            copy_line = copy_line[len(self.options.from_chars):]
            n += 1
        if n > 0:
            self.statistics.increment
            return self.options.to_chars * n + copy_line
        return line

    @property
    def exit_message(self):
        print(f"spaTab finish job\n{'#' * 10}\n{self.statistics}\n{'#' * 10}\n{self.options}")

    @property
    def only_report_exit_message(self):
        print(f"spaTab finish job\n{'#' * 10}\nThe intedance: {self.gues_intedance()}\n{'#' * 10}")
