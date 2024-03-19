from django.test import TestCase
from blog.tasks import example_task

class CeleryTasksTestCase(TestCase):
    def test_example_task(self):
        result = example_task.delay(2)
        self.assertTrue(result.successful())
        self.assertEqual(result.get(), "Task completed after 2 seconds")