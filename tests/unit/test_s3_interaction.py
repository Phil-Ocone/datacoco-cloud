import unittest
from unittest.mock import MagicMock

from datacoco_cloud import S3Interaction


class TestS3Interaction(unittest.TestCase):
    def test_get_bucket(self):
        testCls = S3Interaction(aws_access_key="", aws_secret_key="")

        testCls.client = MagicMock()
        testCls.s3 = MagicMock()
        testCls.get_bucket(bucket_name="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_save_file_locally(self):
        testCls = S3Interaction(aws_access_key="", aws_secret_key="")

        testCls.client = MagicMock()
        testCls.s3 = MagicMock()
        testCls.save_file_locally(
            bucket="bucket", key="key", local_filename="/tmp/test"
        )
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_s3_objects(self):
        testCls = S3Interaction(aws_access_key="", aws_secret_key="")

        testCls.client = MagicMock()
        testCls.s3 = MagicMock()
        testCls.get_s3_objects(bucket="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_s3_keys(self):
        testCls = S3Interaction(aws_access_key="", aws_secret_key="")

        testCls.client = MagicMock()
        testCls.s3 = MagicMock()
        testCls.get_s3_keys(bucket="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_put_file_to_s3_from_string(self):
        testCls = S3Interaction(aws_access_key="", aws_secret_key="")

        testCls.client = MagicMock()
        testCls.s3 = MagicMock()
        testCls.put_file_to_s3_from_string(bucket="", key="", string_data="test_data")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_put_file_to_s3(self):
        testCls = S3Interaction(aws_access_key="", aws_secret_key="")

        testCls.client = MagicMock()
        testCls.s3 = MagicMock()
        testCls.put_file_to_s3(bucket="bucket", key="key", local_filename="/tmp/test")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_put_file_to_s3(self):
        testCls = S3Interaction(aws_access_key="", aws_secret_key="")

        testCls.client = MagicMock()
        testCls.s3 = MagicMock()
        testCls.put_fileobj_to_s3(bucket="", key="", fileobj={})
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_delete_key(self):
        testCls = S3Interaction(aws_access_key="", aws_secret_key="")

        testCls.client = MagicMock()
        testCls.s3 = MagicMock()
        testCls.delete_key(bucket="", key="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_key_exists(self):
        testCls = S3Interaction(aws_access_key="", aws_secret_key="")

        testCls.client = MagicMock()
        testCls.s3 = MagicMock()
        testCls.key_exists(bucket="", key="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_move_key(self):
        testCls = S3Interaction(aws_access_key="", aws_secret_key="")

        testCls.client = MagicMock()
        testCls.s3 = MagicMock()
        testCls.move_key(src_bucket="", src_key="", dst_bucket="", dst_key="")
        self.assertTrue(True)  # Assert that this line is reached without error


if __name__ == "__main__":
    unittest.main()
