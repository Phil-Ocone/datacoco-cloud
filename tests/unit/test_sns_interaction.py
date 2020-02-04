"""
Test SNS Interaction
"""
import unittest
from unittest.mock import MagicMock
import os
from datacoco_cloud import UNIT_TEST_KEY
from datacoco_cloud.sns_interaction import SNSInteraction


class TestSNSInteraction(unittest.TestCase):
    def setUp(self):
        os.environ[UNIT_TEST_KEY] = "True"
        self.testCls = SNSInteraction(
            aws_access_key="", aws_secret_key="", topic="any_topic"
        )  # nosec

    def test_create_topic(self):
        self.testCls.client = MagicMock()
        self.testCls.create_topic()
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_create_publisher_topic_does_not_exist(self):
        self.testCls.client = MagicMock()
        self.testCls.client.list_topics.return_value = {
            "Topics": [{"TopicArn": "test"}]
        }

        try:
            self.testCls.create_publisher()
            self.assertTrue(False)
        except ValueError as v:
            self.assertTrue(str(v).startswith("Topic does not exist"))

    def test_create_subscriber_topic_does_not_exist(self):
        self.testCls.client = MagicMock()
        self.testCls.client.list_topics.return_value = {
            "Topics": [{"TopicArn": "test"}]
        }
        try:
            self.testCls.create_subscriber(sqs_interaction=MagicMock())
            self.fail("There should be an error")
        except ValueError as v:
            self.assertTrue(str(v).startswith("Topic does not exist"))
