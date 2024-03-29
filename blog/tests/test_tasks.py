from django.test import TestCase
from blog.tasks import example_task 

# Define a test case class for testing Celery tasks
class CeleryTasksTestCase(TestCase):
    def test_example_task(self):
        # Execute the example_task asynchronously with a delay of 2 seconds
        result = example_task.delay(2)
        
        # Assert that the task execution was successful
        self.assertTrue(result.successful())
        
        # Assert that the result returned by the task is as expected
        self.assertEqual(result.get(), "Task completed after 2 seconds")
