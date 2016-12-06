import sqlite3


class Synonyms:
    def __init__(self, database, intomemory=False):
        if intomemory:
            self.connection = sqlite3.connect(":memory:")
            self.__load_to_mem(database)
        else:
            self.connection = sqlite3.connect(database)

        self.cursor = self.connection.cursor()

    def get(self, word):
        """
        Returns synonyms list of the word
        :param word: any word from dictionary
        :return: list of synonyms
        """
        self.__exec('''
            SELECT synonym
            FROM ( Words JOIN Synonyms ON Words.id = Synonyms.word_id )
            WHERE Words.word = "{}"
        '''.format(word))

        synonyms = []
        for wrd in self.cursor.fetchall():
            synonyms.append(wrd[0])

        return synonyms

    def __exec(self, query):
        self.cursor.execute(query)

    def __load_to_mem(self, file):
        tmp_db_con = sqlite3.connect(file)
        query = "".join(line for line in tmp_db_con.iterdump())

        # Dump old database in the new one.
        self.connection.executescript(query)
