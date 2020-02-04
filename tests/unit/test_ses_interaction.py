"""
Test SES Interaction
"""
import unittest
from unittest.mock import MagicMock
import os
from datacoco_cloud import UNIT_TEST_KEY
from datacoco_cloud.ses_interaction import SESInteraction


class TestSESInteraction(unittest.TestCase):
    def setUp(self):
        os.environ[UNIT_TEST_KEY] = "True"
        self.testCls = SESInteraction(
            to="", subject="", sender="", aws_secret_key="", aws_access_key=""
        )  # nosec

    def test_html(self):
        self.testCls.connection = MagicMock()
        self.testCls.html(html="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_text(self):
        self.testCls.connection = MagicMock()
        self.testCls.text(text="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_send(self):
        self.testCls.connection = MagicMock()
        self.testCls.text(text="test")
        self.testCls.send()
        self.assertTrue(True)  # Assert that this line is reached without error
