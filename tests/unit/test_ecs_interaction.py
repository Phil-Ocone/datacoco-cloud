"""
Test ECS Interaction
"""
import unittest
from unittest.mock import MagicMock

from datacoco_cloud import ECSInteraction


class TestECSInteraction(unittest.TestCase):
    def setUp(self):
        self.testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

    def test_wait_task(self):
        self.testCls.conn = MagicMock()
        self.testCls.wait_task(cluster="", tasks="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_wait_task(self):
        self.testCls.conn = MagicMock()
        self.testCls.wait_task(cluster="", tasks="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_task_definition(self):
        self.testCls.conn = MagicMock()
        self.testCls.get_task_definition(task="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_actual_describe_task(self):
        self.testCls.conn = MagicMock()
        self.testCls.actual_describe_task(cluster="", tasks="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_stop_task(self):
        self.testCls.conn = MagicMock()
        self.testCls.stop_task(cluster="", task="", reason="")
        self.assertTrue(True)  # Assert that this line is reached without error

    # FIXME this can have more tests
    def test_get_task_status(self):
        self.testCls.conn = MagicMock()
        self.testCls.conn.describe_tasks.return_value = {
            "failures": [],
            "tasks": [{"lastStatus": "STOPPED", "containers": [{"exitCode": 0}]}],
        }
        self.testCls.get_task_status()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_logs_info(self):
        self.testCls.conn = MagicMock()
        self.testCls.get_logs_info(
            {
                "taskDefinition": {
                    "containerDefinitions": [
                        {
                            "logConfiguration": {
                                "options": {
                                    "awslogs-stream-prefix": "any-prefix",
                                    "awslogs-group": "any-group",
                                }
                            }
                        }
                    ]
                }
            }
        )
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_list_tasks(self):
        self.testCls.conn = MagicMock()
        self.testCls.list_tasks(cluster="", desiredStatus="")
        self.assertTrue(True)  # Assert that this line is reached without error

    # FIXME this can have more tests
    def test_run_task(self):
        self.testCls.conn = MagicMock()
        self.testCls.conn.describe_tasks.return_value = {
            "failures": [],
            "tasks": [{"lastStatus": "STOPPED", "containers": [{"exitCode": 0}]}],
        }
        self.testCls.conn.run_task.return_value = {
            "failures": None,
            "tasks": [{"taskArn": "any",}],
        }
        self.testCls.run_task(cluster="", task_definition="")
        self.assertTrue(True)  # Assert that this line is reached without error


if __name__ == "__main__":
    unittest.main()
