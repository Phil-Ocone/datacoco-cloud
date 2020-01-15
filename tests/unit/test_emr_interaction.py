import unittest
from unittest.mock import MagicMock

from datacoco_cloud import EMRCluster


class TestEMRInteraction(unittest.TestCase):
    def test_create_cluster(self):
        testCls = EMRCluster(
            aws_access_key="",
            temp_bucket="",
            region_name="",
            aws_secret_access_key="",
            config_settings="",
            env="",
            SLEEP_TIME=1,
        )

        testCls.conn = MagicMock()
        testCls.create_cluster()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_list_clusters(self):
        testCls = EMRCluster(
            aws_access_key="",
            temp_bucket="",
            region_name="",
            aws_secret_access_key="",
            config_settings="",
            env="",
            SLEEP_TIME=1,
        )

        testCls.conn = MagicMock()
        testCls.list_clusters()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_step_script_submit(self):
        testCls = EMRCluster(
            aws_access_key="",
            temp_bucket="",
            region_name="",
            aws_secret_access_key="",
            config_settings="",
            env="",
            SLEEP_TIME=1,
        )

        testCls.conn = MagicMock()
        testCls.step_script_submit(cluster_id="", script_path="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_step_spark_submit(self):
        testCls = EMRCluster(
            aws_access_key="",
            temp_bucket="",
            region_name="",
            aws_secret_access_key="",
            config_settings="",
            env="",
            SLEEP_TIME=1,
        )

        testCls.conn = MagicMock()
        testCls.step_spark_submit(cluster_id="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_step_status(self):
        testCls = EMRCluster(
            aws_access_key="",
            temp_bucket="",
            region_name="",
            aws_secret_access_key="",
            config_settings="",
            env="",
            SLEEP_TIME=1,
        )

        testCls.conn = MagicMock()
        testCls.get_step_status(cluster_id="", step_id="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_kill_cluster(self):
        testCls = EMRCluster(
            aws_access_key="",
            temp_bucket="",
            region_name="",
            aws_secret_access_key="",
            config_settings="",
            env="",
            SLEEP_TIME=1,
        )

        testCls.conn = MagicMock()
        testCls.kill_cluster(cluster_id="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_kill_all_clusters(self):
        testCls = EMRCluster(
            aws_access_key="",
            temp_bucket="",
            region_name="",
            aws_secret_access_key="",
            config_settings="",
            env="",
            SLEEP_TIME=1,
        )

        testCls.conn = MagicMock()
        testCls.kill_all_clusters()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_create_run_kill(self):
        testCls = EMRCluster(
            aws_access_key="",
            temp_bucket="",
            region_name="",
            aws_secret_access_key="",
            config_settings="",
            env="",
            SLEEP_TIME=1,
        )

        testCls.conn = MagicMock()
        testCls.create_run_kill(script_path="")
        self.assertTrue(True)  # Assert that this line is reached without error


if __name__ == "__main__":
    unittest.main()
