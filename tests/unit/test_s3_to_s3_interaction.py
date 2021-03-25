"""
Test S3 to S3 Interaction
"""
import unittest
import os
from unittest.mock import MagicMock
from datacoco_cloud import UNIT_TEST_KEY
from datacoco_cloud.s3_to_s3_interaction import S3toS3Interaction


class TestS3ToS3Interaction(unittest.TestCase):
    def setUp(self):
        os.environ[UNIT_TEST_KEY] = "True"
        self.testCls = S3toS3Interaction(
            source_aws_key="",
            source_aws_secret="",
            target_aws_key="",
            target_aws_secret="") 

    def test_duplicate_objects(self):
        self.testCls.s3_client_source  = MagicMock()
        self.testCls.s3_client_target = MagicMock()
        self.testCls.duplicate_objects(
            source_bucket="",
            target_bucket="",
            source_bucket_prefix = "",
            target_path="")
        self.assertTrue(True)  # Assert that this line is reached without error


    def test_duplicate_objects_with_suffix(self):
        self.testCls.s3_client_source  = MagicMock()
        self.testCls.s3_client_target = MagicMock()
        self.testCls.duplicate_objects(
            source_bucket="",
            target_bucket="",
            source_bucket_prefix = "",
            target_path="",
            source_bucket_suffix="a")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_move_objects(self):
        self.testCls.s3_client_source  = MagicMock()
        self.testCls.s3_client_target = MagicMock()
        self.testCls.move_objects(
            source_bucket="",
            target_bucket="",
            source_bucket_prefix = "",
            target_path="")
        self.assertTrue(True)  # Assert that this line is reached without error


    def test_move_objects_with_suffix(self):
        self.testCls.s3_client_source  = MagicMock()
        self.testCls.s3_client_target = MagicMock()
        self.testCls.move_objects(
            source_bucket="",
            target_bucket="",
            source_bucket_prefix = "",
            target_path="",
            source_bucket_suffix="a")
        self.assertTrue(True)  # Assert that this line is reached without error
