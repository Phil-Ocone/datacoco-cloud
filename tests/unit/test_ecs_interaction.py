import unittest
from unittest.mock import MagicMock

from datacoco_cloud import ECSInteraction


class TestECSInteraction(unittest.TestCase):
    def test_wait_task(self):
        testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

        testCls.conn = MagicMock()
        testCls.wait_task(cluster="", tasks="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_wait_task(self):
        testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

        testCls.conn = MagicMock()
        testCls.wait_task(cluster="", tasks="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_task_definition(self):
        testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

        testCls.conn = MagicMock()
        testCls.get_task_definition(task="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_actual_describe_task(self):
        testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

        testCls.conn = MagicMock()
        testCls.actual_describe_task(cluster="", tasks="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_stop_task(self):
        testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

        testCls.conn = MagicMock()
        testCls.stop_task(cluster="", task="", reason="")
        self.assertTrue(True)  # Assert that this line is reached without error

    # FIXME this can have more tests
    def test_get_task_status(self):
        testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

        testCls.conn = MagicMock()
        testCls.conn.describe_tasks.return_value = {
            "failures": [],
            "tasks": [{"lastStatus": "STOPPED", "containers": [{"exitCode": 0}]}],
        }
        testCls.get_task_status()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_logs_info(self):
        testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

        testCls.conn = MagicMock()
        testCls.get_logs_info(
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
        testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

        testCls.conn = MagicMock()
        testCls.list_tasks(cluster="", desiredStatus="")
        self.assertTrue(True)  # Assert that this line is reached without error

    # FIXME this can have more tests
    def test_run_task(self):
        testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

        testCls.conn = MagicMock()
        testCls.conn.describe_tasks.return_value = {
            "failures": [],
            "tasks": [{"lastStatus": "STOPPED", "containers": [{"exitCode": 0}]}],
        }
        testCls.conn.run_task.return_value = {
            "failures": None,
            "tasks": [{"taskArn": "any",}],
        }
        testCls.run_task(cluster="", task_definition="")
        self.assertTrue(True)  # Assert that this line is reached without error


if __name__ == "__main__":
    unittest.main()
