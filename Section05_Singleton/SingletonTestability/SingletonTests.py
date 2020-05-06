import unittest

from Section05_Singleton.SingletonTestability.ConfigurableRecordFinder import ConfigurableRecordFinder
from Section05_Singleton.SingletonTestability.Database import Database
from Section05_Singleton.SingletonTestability.DummyDatabase import DummyDatabase
from Section05_Singleton.SingletonTestability.SingletonRecordFinder import SingletonRecordFinder


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db: Database = Database()
        db2: Database = Database()
        self.assertEqual(db, db2)

    def test_singleton_total_population(self):
        """ This tests on a live database :( """
        rf: SingletonRecordFinder = SingletonRecordFinder()
        names = ['Seoul', 'Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(tp, 17500000 + 17400000)  # what if these change?

    ddb: DummyDatabase = DummyDatabase()

    def test_dependent_total_population(self):
        crf: ConfigurableRecordFinder = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(
            crf.total_population(['alpha', 'beta']),
            3
        )
