"""
Test S3 Interaction
"""
import unittest
import os
from unittest.mock import MagicMock
from datacoco_cloud import UNIT_TEST_KEY
from datacoco_cloud.s3_interaction import S3Interaction


class TestS3Interaction(unittest.TestCase):
    def setUp(self):
        os.environ[UNIT_TEST_KEY] = "True"
        self.testCls = S3Interaction(
            aws_access_key="", aws_secret_key=""
        )  # nosec

    def test_get_bucket(self):
        self.testCls.client = MagicMock()
        self.testCls.s3 = MagicMock()
        self.testCls.get_bucket(bucket_name="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_save_file_locally(self):
        self.testCls.client = MagicMock()
        self.testCls.s3 = MagicMock()
        self.testCls.save_file_locally(
            bucket="bucket", key="key", local_filename="/tmp/test"
        )
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_s3_objects(self):
        self.testCls.client = MagicMock()
        self.testCls.s3 = MagicMock()
        self.testCls.get_s3_objects(bucket="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_s3_keys(self):
        self.testCls.client = MagicMock()
        self.testCls.s3 = MagicMock()
        self.testCls.get_s3_keys(bucket="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_put_file_to_s3_from_string(self):
        self.testCls.client = MagicMock()
        self.testCls.s3 = MagicMock()
        self.testCls.put_file_to_s3_from_string(
            bucket="", key="", string_data="test_data"
        )
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_put_file_to_s3(self):
        self.testCls.client = MagicMock()
        self.testCls.s3 = MagicMock()
        self.testCls.put_file_to_s3(
            bucket="bucket", key="key", local_filename="/tmp/test"  # nosec
        )
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_put_fileobj_to_s3(self):
        self.testCls.client = MagicMock()
        self.testCls.s3 = MagicMock()
        self.testCls.put_fileobj_to_s3(bucket="", key="", fileobj={})
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_delete_key(self):
        self.testCls.client = MagicMock()
        self.testCls.s3 = MagicMock()
        self.testCls.delete_key(bucket="", key="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_key_exists(self):
        self.testCls.client = MagicMock()
        self.testCls.s3 = MagicMock()
        self.testCls.key_exists(bucket="", key="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_move_key(self):
        self.testCls.client = MagicMock()
        self.testCls.s3 = MagicMock()
        self.testCls.move_key(
            src_bucket="", src_key="", dst_bucket="", dst_key=""
        )
        self.assertTrue(True)  # Assert that this line is reached without error
