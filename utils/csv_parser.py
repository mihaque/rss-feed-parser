import csv
from .entry import Entry

class WriteIntoCSV():
    def __init__(self, file_name, fields):
        self._fields = fields
        self._file_name = file_name

    def __generate_rows(self, entries: list):
        rows = []
        for entry in entries:
            row = [entry.title, entry.link, entry.summary, entry.source, (',').join(entry.tags), entry.published]
            rows.append(row)
        return rows

    def write(self, entries):
        with open(self._file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # generate header
            csv_writer.writerow(self._fields)

            # generate rows
            rows = self.__generate_rows(entries)
            csv_writer.writerows(rows, )
