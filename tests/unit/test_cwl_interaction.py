"""
Test Cloud Watch Log
"""
import os
import unittest
from unittest.mock import MagicMock
from datacoco_cloud import UNIT_TEST_KEY
from datacoco_cloud.cwl_interaction import CWLInteraction


class TestCWLInteraction(unittest.TestCase):
    def setUp(self):
        os.environ[UNIT_TEST_KEY] = "True"
        self.testCls = CWLInteraction(
            region="", aws_secret_key="", aws_access_key=""
        )

    def test_parse_and_print_events(self):
        self.testCls.client = MagicMock()
        self.testCls.parse_and_print_events(events="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_log_events(self):
        self.testCls.client = MagicMock()
        self.testCls.client.get_log_events.return_value = {
            "ResponseMetadata": {"HTTPStatusCode": 200},
            "events": [],
        }
        self.testCls.get_log_events(log_group="", log_stream="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_get_log_events_http_error(self):
        self.testCls.client = MagicMock()
        self.testCls.client.get_log_events.return_value = {
            "ResponseMetadata": {"HTTPStatusCode": 500},
            "events": [],
        }
        try:
            self.testCls.get_log_events(log_group="", log_stream="")
            self.assertTrue(False)
        except ValueError as v:
            self.assertTrue(True)  # Assert value error did happen


