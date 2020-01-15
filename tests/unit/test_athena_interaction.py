import unittest
from unittest.mock import MagicMock

from datacoco_cloud import AthenaInteraction


class TestAthenaInteraction(unittest.TestCase):
    def test_exec_sql(self):
        testCls = AthenaInteraction(aws_access_key="", aws_secret_key="", region="")

        testCls.client = MagicMock()
        testCls.store_query(name="", description="", db="", sql="")
        testCls.client.create_named_query.return_value = {}
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_search_queries_by_db_name(self):
        testCls = AthenaInteraction(aws_access_key="", aws_secret_key="", region="")

        testCls.client = MagicMock()
        testCls.search_queries_by_db_name(db_name="")
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_search_queries_by_db_name(self):
        testCls = AthenaInteraction(aws_access_key="", aws_secret_key="", region="")

        testCls.client = MagicMock()
        testCls.search_queries_by_db_name(db_name="")
        self.assertTrue(True)  # Assert that this line is reached without error

    # FIXME Not testable due to while loop in poll_for_results
    # def test_repair_table(self):
    #     testCls = AthenaInteraction(
    #         aws_access_key="", aws_secret_key="", region=""
    #     )
    #
    #     execution_details = {
    #         'QueryExecution': {
    #             'Status': {
    #                 'State': "SUCCEEDED"
    #             }
    #         }
    #     }
    #
    #     testCls.client = MagicMock()
    #     testCls.repair_table(db_name="", table="")
    #
    #     self.assertTrue(True)  # Assert that this line is reached without error

    def test_format_results(self):
        testCls = AthenaInteraction(aws_access_key="", aws_secret_key="", region="")

        testCls.client = MagicMock()
        result = testCls.format_results(
            results={"ResultSet": {"Rows": [{"Data": "test"}]}}, delimiter=","
        )
        print(result)
        self.assertTrue(True)  # Assert that this line is reached without error

    def test_results_formatter(self):
        testCls = AthenaInteraction(aws_access_key="", aws_secret_key="", region="")

        testCls.client = MagicMock()
        result = testCls.results_formatter(
            results={"ResultSet": {"Rows": [{"Data": "test"}]}}
        )
        print(result)
        self.assertTrue(True)  # Assert that this line is reached without error


if __name__ == "__main__":
    unittest.main()
