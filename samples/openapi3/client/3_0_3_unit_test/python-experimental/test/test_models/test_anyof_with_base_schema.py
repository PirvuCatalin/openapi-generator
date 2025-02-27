# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.model.anyof_with_base_schema import AnyofWithBaseSchema
from unit_test_api import configuration


class TestAnyofWithBaseSchema(unittest.TestCase):
    """AnyofWithBaseSchema unit test stubs"""
    _configuration = configuration.Configuration()

    def test_one_anyof_valid_passes(self):
        # one anyOf valid
        AnyofWithBaseSchema._from_openapi_data(
            "foobar",
            _configuration=self._configuration
        )

    def test_both_anyof_invalid_fails(self):
        # both anyOf invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AnyofWithBaseSchema._from_openapi_data(
                "foo",
                _configuration=self._configuration
            )

    def test_mismatch_base_schema_fails(self):
        # mismatch base schema
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AnyofWithBaseSchema._from_openapi_data(
                3,
                _configuration=self._configuration
            )


if __name__ == '__main__':
    unittest.main()
