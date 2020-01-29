"""
Test EMR Interaction
"""
import unittest
from unittest.mock import MagicMock

import os
from datacoco_cloud import UNIT_TEST_KEY
from datacoco_cloud.emr_interaction import EMRCluster


class TestEMRInteraction(unittest.TestCase):
    def setUp(self):
        os.environ[UNIT_TEST_KEY] = "True"
        self.testCls = EMRCluster(
            aws_access_key="",
            temp_bucket="",
            region_name="",
            aws_secret_access_key="",
            env="",
            SLEEP_TIME=1,
        )

    def test_create_cluster(self):
        self.testCls.conn = MagicMock()
        self.testCls.create_cluster()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_list_clusters(self):
        self.testCls.conn = MagicMock()
        self.testCls.list_clusters()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_step_script_submit(self):
        self.testCls.conn = MagicMock()
        self.testCls.step_script_submit(cluster_id="", script_path="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_step_spark_submit(self):
        self.testCls.conn = MagicMock()
        self.testCls.step_spark_submit(cluster_id="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_step_status(self):
        self.testCls.conn = MagicMock()
        self.testCls.get_step_status(cluster_id="", step_id="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_kill_cluster(self):
        self.testCls.conn = MagicMock()
        self.testCls.kill_cluster(cluster_id="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_kill_all_clusters(self):
        self.testCls.conn = MagicMock()
        self.testCls.kill_all_clusters()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_create_run_kill(self):
        self.testCls.conn = MagicMock()
        self.testCls.create_run_kill(script_path="")
        self.assertTrue(True)  # Assert that this line is reached without error
