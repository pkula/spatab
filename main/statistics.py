"""Statistic collection logic for spaTab."""


class Statistics:
    """Manager of aggregated statistics for a run of spaTab."""

    def __init__(self):
        self.num_modified_lines = 0

    @property
    def increment(self):  # type: () -> None
        """Increment the number of times we've seen bad line in file."""
        self.num_modified_lines += 1

    def __str__(self):
        return f"spaTab modified {self.num_modified_lines} lines"
