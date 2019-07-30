import os


class Journal:
    """
    The Journal class keeps track of any unsaved journal entries. Methods
    exists to save to and load from a data file.
    """

    def __init__(self, entries: list):
        """
        Creates a new Journal object from a list of journal entries.

        :param entries: list of entries to include in the journal.
        """
        self.entries = entries

    @classmethod
    def load(cls, basename: str) -> 'Journal':
        """
        Loads a data file into an object of this class. If the data file
        doesn't exist or can't be read, an empty list is used instead.

        :param basename: The base name of the file to load from

        :returns: An object of this class with the contents of the data file.

        :raises FileNotFoundError: If the data file doesn't exist
        :raises OSError:           If the data file can't be opened for reading
        """

        # Construct the full path to the data file.
        full_path = os.path.abspath(os.path.join(".", basename))

        # Initialize an empty list to fill with text from the data file.
        entries = []

        # Try to open the data file for reading.
        try:
            with open(full_path, 'r', encoding="utf-8") as fin:
                entries = fin.readlines()
                print("... loaded journal from {} ...".format(full_path))
                print("... loaded {} entries ...".format(len(entries)))
        except FileNotFoundError:
            print("... {} doesn't exist; starting an empty journal instead ..."
                  .format(full_path))
        except OSError:
            print("... could not open {} for reading; starting an empty " +
                  "journal instead ...".format(full_path))
        print()

        return Journal(entries)

    def save(self, basename: str):
        """
        Saves the list of journal entries to a data file.

        :param basename: The base name of the file to save to

        :raises FileNotFoundError: If the data file doesn't exist
        :raises OSError:           If the data file can't be opened for writing
        """

        # Construct the full path to the data file.
        full_path = os.path.abspath(os.path.join(".", basename))

        # Try to open the data file for writing.
        try:
            with open(full_path, 'w', encoding="utf-8") as fout:
                print("... saving to journal from {} ...".format(full_path))
                fout.writelines(self.entries)
                print("... save complete ...")
        except FileNotFoundError:
            print("... {} doesn't exist; nothing is saved ..."
                  .format(full_path))
        except OSError:
            print("... could not open {} for writing; nothing is saved ..."
                  .format(full_path))

    def add_entry(self, entry):
        """
        Adds the entry to the end of the journal.

        :param entry: a journal entry
        """
        self.entries.append(entry)
