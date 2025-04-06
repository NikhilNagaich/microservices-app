import unittest
from worker import handle_task

class WorkerTestCase(unittest.TestCase):
    def test_handle_task(self):
        try:
            handle_task({"test": "data"})
        except Exception as e:
            self.fail(f"handle_task raised exception: {e}")

if __name__ == '__main__':
    unittest.main()
