"""
Test SNS Interaction
"""
import unittest
from unittest.mock import MagicMock

from datacoco_cloud import SNSInteraction


class TestSNSInteraction(unittest.TestCase):
    def setUp(self):
        self.testCls = SNSInteraction(aws_access_key="", aws_secret_key="", topic="")  # nosec

    def test_create_topic(self):
        self.testCls.client = MagicMock()
        self.testCls.create_topic()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_create_publisher(self):
        self.testCls.client = MagicMock()
        self.testCls.client.list_topics.return_value = {"Topics": [{"TopicArn": "test"}]}
        self.testCls.create_publisher()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_create_subscriber(self):
        self.testCls.client = MagicMock()
        self.testCls.client.list_topics.return_value = {"Topics": [{"TopicArn": "test"}]}
        self.testCls.create_subscriber(sqs_interaction=MagicMock())
        self.assertTrue(True)  # Assert that this line is reached without error


if __name__ == "__main__":
    unittest.main()
