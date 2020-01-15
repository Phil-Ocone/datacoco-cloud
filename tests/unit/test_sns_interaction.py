import unittest
from unittest.mock import MagicMock

from datacoco_cloud import SNSInteraction


class TestSNSInteraction(unittest.TestCase):
    def test_create_topic(self):
        testCls = SNSInteraction(aws_access_key="", aws_secret_key="", topic="")

        testCls.client = MagicMock()
        testCls.create_topic()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_create_publisher(self):
        testCls = SNSInteraction(aws_access_key="", aws_secret_key="", topic="test")

        testCls.client = MagicMock()
        testCls.client.list_topics.return_value = {"Topics": [{"TopicArn": "test"}]}
        testCls.create_publisher()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_create_subscriber(self):
        testCls = SNSInteraction(aws_access_key="", aws_secret_key="", topic="test")

        testCls.client = MagicMock()
        testCls.client.list_topics.return_value = {"Topics": [{"TopicArn": "test"}]}
        testCls.create_subscriber(sqs_interaction=MagicMock())
        self.assertTrue(True)  # Assert that this line is reached without error


if __name__ == "__main__":
    unittest.main()
