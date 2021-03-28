"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from harbor-client.api_client import ApiClient, Endpoint as _Endpoint
from harbor-client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from harbor-client.model.audit_log import AuditLog
from harbor-client.model.errors import Errors


class AuditlogApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __list_audit_logs(
            self,
            **kwargs
        ):
            """Get recent logs of the projects which the user is a member of  # noqa: E501

            This endpoint let user see the recent operation logs of the projects which he is member of   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_audit_logs(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
                q (str): Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]. [optional]
                page (int): The page number. [optional] if omitted the server will use the default value of 1
                page_size (int): The size of per page. [optional] if omitted the server will use the default value of 10
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [AuditLog]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_audit_logs = _Endpoint(
            settings={
                'response_type': ([AuditLog],),
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/audit-logs',
                'operation_id': 'list_audit_logs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'q',
                    'page',
                    'page_size',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'q':
                        (str,),
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'x_request_id': 'X-Request-Id',
                    'q': 'q',
                    'page': 'page',
                    'page_size': 'page_size',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'q': 'query',
                    'page': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_audit_logs
        )
