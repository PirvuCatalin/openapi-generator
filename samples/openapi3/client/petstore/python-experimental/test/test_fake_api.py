# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.api.fake_api import FakeApi  # noqa: E501
from petstore_api import configuration, schemas, api_client

from . import ApiTestMixin


class TestFakeApi(ApiTestMixin, unittest.TestCase):
    """FakeApi unit test stubs"""
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = FakeApi(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_additional_properties_with_array_of_enums(self):
        """Test case for additional_properties_with_array_of_enums

        Additional Properties with Array of Enums  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import additional_properties_with_array_of_enums as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_array_model(self):
        """Test case for array_model

        """
        from petstore_api.api.fake_api_endpoints import array_model as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_array_of_enums(self):
        """Test case for array_of_enums

        Array of Enums  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import array_of_enums as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_body_with_file_schema(self):
        """Test case for body_with_file_schema

        """
        from petstore_api.api.fake_api_endpoints import body_with_file_schema as endpoint_module
        response_status = 200
        response_body = ''
        content_type = 'application/json'



    def test_body_with_query_params(self):
        """Test case for body_with_query_params

        """
        from petstore_api.api.fake_api_endpoints import body_with_query_params as endpoint_module
        response_status = 200
        response_body = ''
        content_type = 'application/json'



    def test_boolean(self):
        """Test case for boolean

        """
        from petstore_api.api.fake_api_endpoints import boolean as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_case_sensitive_params(self):
        """Test case for case_sensitive_params

        """
        from petstore_api.api.fake_api_endpoints import case_sensitive_params as endpoint_module
        response_status = 200
        response_body = ''
        pass

    def test_client_model(self):
        """Test case for client_model

        To test \"client\" model  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import client_model as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'



        content_type = 'application/json'



    def test_composed_one_of_different_types(self):
        """Test case for composed_one_of_different_types

        """
        from petstore_api.api.fake_api_endpoints import composed_one_of_different_types as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_delete_coffee(self):
        """Test case for delete_coffee

        Delete coffee  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import delete_coffee as endpoint_module
        response_status = 200
        response_body = ''
        pass

    def test_endpoint_parameters(self):
        """Test case for endpoint_parameters

        Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트   # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import endpoint_parameters as endpoint_module
        response_status = 400
        response_body = ''

    def test_enum_parameters(self):
        """Test case for enum_parameters

        To test enum parameters  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import enum_parameters as endpoint_module
        response_status = 400
        response_body = ''

    def test_fake_health_get(self):
        """Test case for fake_health_get

        Health check endpoint  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import fake_health_get as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'



        pass

    def test_group_parameters(self):
        """Test case for group_parameters

        Fake endpoint to test group parameters (optional)  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import group_parameters as endpoint_module
        response_status = 400
        response_body = ''
        pass

    def test_inline_additional_properties(self):
        """Test case for inline_additional_properties

        test inline additionalProperties  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import inline_additional_properties as endpoint_module
        response_status = 200
        response_body = ''
        content_type = 'application/json'



    def test_inline_composition(self):
        """Test case for inline_composition

        testing composed schemas at inline locations  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import inline_composition as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'



        accept_content_type = 'multipart/form-data'




    def test_json_form_data(self):
        """Test case for json_form_data

        test json serialization of form data  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import json_form_data as endpoint_module
        response_status = 200
        response_body = ''

    def test_json_with_charset(self):
        """Test case for json_with_charset

        json with charset tx and rx  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import json_with_charset as endpoint_module
        response_status = 200
        accept_content_type = 'application/json; charset=utf-8'




    def test_mammal(self):
        """Test case for mammal

        """
        from petstore_api.api.fake_api_endpoints import mammal as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'



        content_type = 'application/json'



    def test_number_with_validations(self):
        """Test case for number_with_validations

        """
        from petstore_api.api.fake_api_endpoints import number_with_validations as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_object_in_query(self):
        """Test case for object_in_query

        user list  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import object_in_query as endpoint_module
        response_status = 200
        response_body = ''
        pass

    def test_object_model_with_ref_props(self):
        """Test case for object_model_with_ref_props

        """
        from petstore_api.api.fake_api_endpoints import object_model_with_ref_props as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_parameter_collisions(self):
        """Test case for parameter_collisions

        parameter collision case  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import parameter_collisions as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_query_parameter_collection_format(self):
        """Test case for query_parameter_collection_format

        """
        from petstore_api.api.fake_api_endpoints import query_parameter_collection_format as endpoint_module
        response_status = 200
        response_body = ''
        pass

    def test_ref_object_in_query(self):
        """Test case for ref_object_in_query

        user list  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import ref_object_in_query as endpoint_module
        response_status = 200
        response_body = ''
        pass

    def test_response_without_schema(self):
        """Test case for response_without_schema

        receives a response without schema  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import response_without_schema as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'



        accept_content_type = 'application/xml'



        pass

    def test_string(self):
        """Test case for string

        """
        from petstore_api.api.fake_api_endpoints import string as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_string_enum(self):
        """Test case for string_enum

        """
        from petstore_api.api.fake_api_endpoints import string_enum as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_upload_download_file(self):
        """Test case for upload_download_file

        uploads a file and downloads a file using application/octet-stream  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import upload_download_file as endpoint_module
        response_status = 200
        accept_content_type = 'application/octet-stream'



        content_type = 'application/octet-stream'



    def test_upload_file(self):
        """Test case for upload_file

        uploads a file using multipart/form-data  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import upload_file as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'




    def test_upload_files(self):
        """Test case for upload_files

        uploads files using multipart/form-data  # noqa: E501
        """
        from petstore_api.api.fake_api_endpoints import upload_files as endpoint_module
        response_status = 200
        accept_content_type = 'application/json'





if __name__ == '__main__':
    unittest.main()
