import getopt
import os

from spatab.const import TAB, SPACE
from spatab.exceptions import BadChooseException

OPTIONS = [
    'from=',
    'replace',
    'tab-chars=',
]


class Options:
    """Options:
            _from - spaces or tabs - if don't exist find
            replace - if exist don't save copy
            tab_chars - how many spaces have one tab
            filename
            from_chars - like '   '
            to_chars - like '\t'
    """

    def __init__(self, argv):
        """argv without scriptname = argv[1:]"""
        opts, args = getopt.getopt(argv, 'f:rt:', OPTIONS)

        self._from = None
        self.replace = False
        self.tab_chars = 4

        if len(args) != 1:
            raise BadChooseException
        self.filename = args[0]
        if not os.path.isfile(self.filename):
            raise FileNotFoundError

        for o, a in opts:
            if o in ('-f', '--from'):
                self._from = a
            elif o in ('-r', '--replace'):
                self.replace = True
                if a:
                    raise BadChooseException
            elif o in ('-t', '--tab-chars'):
                self.tab_chars = int(a)

        if self._from and self._from == "spaces":
            self.from_chars = SPACE * self.tab_chars
            self.to_chars = TAB
        elif self._from and self._from == "tabs":
            self.from_chars = TAB
            self.to_chars = SPACE * self.tab_chars
        elif self._from:
            raise BadChooseException
        else:
            self.from_chars = None
            self.to_chars = None

    def __str__(self):
        """Format option message."""
        message_replace = "You replaced file and didn't create copy" if self.replace else "You replaced file and created copy"
        return f"Your options:\nfrom: {self._from}\ntab_chars: {self.tab_chars}\n{message_replace}"
