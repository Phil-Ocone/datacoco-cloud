"""
Test SES Interaction
"""
import unittest
from unittest.mock import MagicMock

from datacoco_cloud import SESInteraction


class TestSESInteraction(unittest.TestCase):
    def setUp(self):
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


if __name__ == "__main__":
    unittest.main()
