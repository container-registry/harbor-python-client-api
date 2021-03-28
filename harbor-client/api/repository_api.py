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
from harbor-client.model.errors import Errors
from harbor-client.model.repository import Repository


class RepositoryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __delete_repository(
            self,
            project_name,
            repository_name,
            **kwargs
        ):
            """Delete repository  # noqa: E501

            Delete the repository specified by name  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_repository(project_name, repository_name, async_req=True)
            >>> result = thread.get()

            Args:
                project_name (str): The name of the project
                repository_name (str): The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb

            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
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
                None
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
            kwargs['project_name'] = \
                project_name
            kwargs['repository_name'] = \
                repository_name
            return self.call_with_http_info(**kwargs)

        self.delete_repository = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/projects/{project_name}/repositories/{repository_name}',
                'operation_id': 'delete_repository',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_name',
                    'repository_name',
                    'x_request_id',
                ],
                'required': [
                    'project_name',
                    'repository_name',
                ],
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
                    'project_name':
                        (str,),
                    'repository_name':
                        (str,),
                    'x_request_id':
                        (str,),
                },
                'attribute_map': {
                    'project_name': 'project_name',
                    'repository_name': 'repository_name',
                    'x_request_id': 'X-Request-Id',
                },
                'location_map': {
                    'project_name': 'path',
                    'repository_name': 'path',
                    'x_request_id': 'header',
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
            callable=__delete_repository
        )

        def __get_repository(
            self,
            project_name,
            repository_name,
            **kwargs
        ):
            """Get repository  # noqa: E501

            Get the repository specified by name  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_repository(project_name, repository_name, async_req=True)
            >>> result = thread.get()

            Args:
                project_name (str): The name of the project
                repository_name (str): The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb

            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
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
                Repository
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
            kwargs['project_name'] = \
                project_name
            kwargs['repository_name'] = \
                repository_name
            return self.call_with_http_info(**kwargs)

        self.get_repository = _Endpoint(
            settings={
                'response_type': (Repository,),
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/projects/{project_name}/repositories/{repository_name}',
                'operation_id': 'get_repository',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_name',
                    'repository_name',
                    'x_request_id',
                ],
                'required': [
                    'project_name',
                    'repository_name',
                ],
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
                    'project_name':
                        (str,),
                    'repository_name':
                        (str,),
                    'x_request_id':
                        (str,),
                },
                'attribute_map': {
                    'project_name': 'project_name',
                    'repository_name': 'repository_name',
                    'x_request_id': 'X-Request-Id',
                },
                'location_map': {
                    'project_name': 'path',
                    'repository_name': 'path',
                    'x_request_id': 'header',
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
            callable=__get_repository
        )

        def __list_repositories(
            self,
            project_name,
            **kwargs
        ):
            """List repositories  # noqa: E501

            List repositories of the specified project  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_repositories(project_name, async_req=True)
            >>> result = thread.get()

            Args:
                project_name (str): The name of the project

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
                [Repository]
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
            kwargs['project_name'] = \
                project_name
            return self.call_with_http_info(**kwargs)

        self.list_repositories = _Endpoint(
            settings={
                'response_type': ([Repository],),
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/projects/{project_name}/repositories',
                'operation_id': 'list_repositories',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_name',
                    'x_request_id',
                    'q',
                    'page',
                    'page_size',
                ],
                'required': [
                    'project_name',
                ],
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
                    'project_name':
                        (str,),
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
                    'project_name': 'project_name',
                    'x_request_id': 'X-Request-Id',
                    'q': 'q',
                    'page': 'page',
                    'page_size': 'page_size',
                },
                'location_map': {
                    'project_name': 'path',
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
            callable=__list_repositories
        )

        def __update_repository(
            self,
            project_name,
            repository_name,
            repository,
            **kwargs
        ):
            """Update repository  # noqa: E501

            Update the repository specified by name  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_repository(project_name, repository_name, repository, async_req=True)
            >>> result = thread.get()

            Args:
                project_name (str): The name of the project
                repository_name (str): The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
                repository (Repository): The JSON object of repository.

            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
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
                None
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
            kwargs['project_name'] = \
                project_name
            kwargs['repository_name'] = \
                repository_name
            kwargs['repository'] = \
                repository
            return self.call_with_http_info(**kwargs)

        self.update_repository = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/projects/{project_name}/repositories/{repository_name}',
                'operation_id': 'update_repository',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_name',
                    'repository_name',
                    'repository',
                    'x_request_id',
                ],
                'required': [
                    'project_name',
                    'repository_name',
                    'repository',
                ],
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
                    'project_name':
                        (str,),
                    'repository_name':
                        (str,),
                    'repository':
                        (Repository,),
                    'x_request_id':
                        (str,),
                },
                'attribute_map': {
                    'project_name': 'project_name',
                    'repository_name': 'repository_name',
                    'x_request_id': 'X-Request-Id',
                },
                'location_map': {
                    'project_name': 'path',
                    'repository_name': 'path',
                    'repository': 'body',
                    'x_request_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_repository
        )
