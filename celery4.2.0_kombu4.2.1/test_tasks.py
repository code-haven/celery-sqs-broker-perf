from unittest import TestCase

from celery import group

from tasks import echo


class TestCeleryTask(TestCase):
    def test_300_tasks(self):
        tasks = [echo.s(i) for i in range(100)]
        job = group(tasks)
        result = job.apply_async()
        output = result.get()
        expected_output = [i for i in range(100)]
        self.assertEqual(sorted(output), sorted(expected_output))
