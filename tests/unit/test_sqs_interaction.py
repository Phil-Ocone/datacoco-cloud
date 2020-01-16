"""
Test SQS Interaction
"""
import unittest
from unittest.mock import MagicMock

from datacoco_cloud import SQSInteraction


class TestSQSInteraction(unittest.TestCase):
    def setUp(self):
        self.testCls = SQSInteraction(aws_access_key="", aws_secret_key="", queue_name="") # nosec

    def test_init_sqs(self):
        self.testCls.sqs = MagicMock()
        self.testCls.init_sqs()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_create_queue(self):
        self.testCls.sqs = MagicMock()
        self.testCls.create_queue(queue_name="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_queue_attribs(self):
        self.testCls.sqs = MagicMock()
        self.testCls.get_queue_attribs()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_set_policy(self):
        self.testCls.sqs = MagicMock()
        self.testCls.set_policy(policy="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_queue_url(self):
        self.testCls.sqs = MagicMock()
        self.testCls.get_queue_url()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_queue_count(self):
        self.testCls.sqs = MagicMock()
        self.testCls.get_queue_count()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_create_subscriber(self):
        self. testCls.sqs = MagicMock()
        self.testCls.create_subscriber()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_send_message(self):
        self.testCls.sqs = MagicMock()
        self.testCls.send_message(message_body="")
        self.assertTrue(True)  # Assert that this line is reached without error


if __name__ == "__main__":
    unittest.main()
