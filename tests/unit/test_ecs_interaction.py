"""
Test ECS Interaction
"""
import unittest
from unittest.mock import MagicMock

import os
from datacoco_cloud import UNIT_TEST_KEY
from datacoco_cloud.ecs_interaction import ECSInteraction


class TestECSInteraction(unittest.TestCase):
    def setUp(self):
        os.environ[UNIT_TEST_KEY] = "True"
        self.testCls = ECSInteraction(aws_access_key="", aws_secret_key="")

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

    def test_get_task_status(self):
        self.testCls.conn = MagicMock()
        self.testCls.conn.describe_tasks.return_value = {
            "failures": [],
            "tasks": [
                {"lastStatus": "STOPPED", "containers": [{"exitCode": 0}]}
            ],
        }
        self.testCls.get_task_status()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_task_status_runtime_error(self):
        self.testCls.conn = MagicMock()
        self.testCls.conn.describe_tasks.return_value = {
            "failures": [],
            "tasks": None,
        }
        try:
            self.testCls.get_task_status()
            self.assertTrue(False)
        except RuntimeError as r:
            self.assertTrue(str(r).startswith("Could not find completed task"))

    def test_get_task_status_has_failures(self):
        self.testCls.conn = MagicMock()
        self.testCls.conn.describe_tasks.return_value = {
            "failures": [0],
            "tasks": [
                {"lastStatus": "STOPPED", "containers": [{"exitCode": 0}]}
            ],
        }
        try:
            self.testCls.get_task_status()
            self.assertTrue(False)
        except Exception as r:
            self.assertTrue(str(r).startswith("There were failures"))

    def test_get_task_status_not_all_stopped(self):
        self.testCls.conn = MagicMock()
        self.testCls.conn.describe_tasks.return_value = {
            "failures": [],
            "tasks": [
                {"lastStatus": "RUNNING", "containers": [{"exitCode": 0}]}
            ],
        }
        try:
            self.testCls.get_task_status()
            self.assertTrue(False)
        except Exception as e:
            self.assertTrue(str(e).startswith("Not all tasks finished"))

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

    def test_run_task(self):
        self.testCls.conn = MagicMock()
        self.testCls.conn.describe_tasks.return_value = {
            "failures": [],
            "tasks": [
                {"lastStatus": "STOPPED", "containers": [{"exitCode": 0}]}
            ],
        }
        self.testCls.conn.run_task.return_value = {
            "failures": None,
            "tasks": [{"taskArn": "any"}],
        }
        self.testCls.run_task(cluster="", task_definition="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_run_task_more_parameters(self):
        self.testCls.conn = MagicMock()
        self.testCls.conn.describe_tasks.return_value = {
            "failures": [],
            "tasks": [
                {"lastStatus": "STOPPED", "containers": [{"exitCode": 0}]}
            ],
        }
        self.testCls.conn.run_task.return_value = {
            "failures": None,
            "tasks": [{"taskArn": "any"}],
        }
        self.testCls.run_task(
            cluster="",
            task_definition="",
            command="test command",
            environment="test environment",
            cpu="test cpu",
            memory="test memory",
            memory_reservation="test memory reservation",
            launch_type="FARGATE",
            subnets="123,123",
            security_groups="sec1,sec2",
        )
        self.assertTrue(True)  # Assert that this line is reached without error
