import unittest
from unittest.mock import MagicMock

from datacoco_cloud import SESInteraction


class TestSESInteraction(unittest.TestCase):
    def test_html(self):
        testCls = SESInteraction(
            to="", subject="", sender="", aws_secret_key="", aws_access_key=""
        )

        testCls.connection = MagicMock()
        testCls.html(html="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_text(self):
        testCls = SESInteraction(
            to="", subject="", sender="", aws_secret_key="", aws_access_key=""
        )

        testCls.connection = MagicMock()
        testCls.text(text="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_send(self):
        testCls = SESInteraction(
            to="", subject="", sender="", aws_secret_key="", aws_access_key=""
        )

        testCls.connection = MagicMock()
        testCls.text(text="test")
        testCls.send()
        self.assertTrue(True)  # Assert that this line is reached without error


if __name__ == "__main__":
    unittest.main()
