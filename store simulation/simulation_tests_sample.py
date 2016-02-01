import unittest
from simulation import GroceryStoreSimulation

class TestSimulation(unittest.TestCase):
    pass


def check_num(config, events, num_customers):
    def test(self):
        sim = GroceryStoreSimulation(config)
        stats = sim.run(events)
        self.assertEqual(stats['num_customers'], num_customers)
    return test


def check_total(config, events, total_time):
    def test(self):
        sim = GroceryStoreSimulation(config)
        stats = sim.run(events)
        self.assertEqual(stats['total_time'], total_time)
    return test


def check_wait(config, events, max_wait):
    def test(self):
        sim = GroceryStoreSimulation(config)
        stats = sim.run(events)
        self.assertEqual(stats['max_wait'], max_wait)
    return test


def make_test(config, events, num_customers, total_time, max_wait):
    """Helper for making tests.

    Since all of the tests have the same format, it's useful to use this
    helper function instead of repeating lots of code.
    """
    root = 'test_' + config.replace('.', '_') + '_' + events.replace('.', '_')
    setattr(TestSimulation,
            root + '__num_customers',
            check_num(config, events, num_customers))
    setattr(TestSimulation,
            root + '__total_time',
            check_total(config, events, total_time))
    setattr(TestSimulation,
            root + '__max_wait',
            check_wait(config, events, max_wait))

# Sample tests
make_test('input_files/config_100_10.json',
          'input_files/events_one.txt',
          1, 24, 14)
make_test('input_files/config_010_10.json',
          'input_files/events_one.txt',
          1, 21, 11)
make_test('input_files/config_001_10.json',
          'input_files/events_one.txt',
          1, 25, 15)
make_test('input_files/config_111_10.json',
          'input_files/events_one.txt',
          1, 24, 14)
make_test('input_files/config_100_10.json',
          'input_files/events_two.txt',
          2, 32, 22)
make_test('input_files/config_010_10.json',
          'input_files/events_two.txt',
          2, 26, 16)
make_test('input_files/config_001_10.json',
          'input_files/events_two.txt',
          2, 33, 23)
make_test('input_files/config_111_10.json',
          'input_files/events_two.txt',
          2, 21, 13)
make_test('input_files/config_111_10.json',
          'input_files/events_one_close.txt',
          4, 24, 21)


if __name__ == '__main__':
    unittest.main()
