# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from harbor_client.api_client import ApiClient


class IconApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_icon(self, digest, **kwargs):  # noqa: E501
        """Get artifact icon  # noqa: E501

        Get the artifact icon with the specified digest. As the original icon image is resized and encoded before returning, the parameter \"digest\" in the path doesn't match the hash of the returned content  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_icon(digest, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str digest: The digest of the resource (required)
        :param str x_request_id: An unique ID for the request
        :return: Icon
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_icon_with_http_info(digest, **kwargs)  # noqa: E501
        else:
            (data) = self.get_icon_with_http_info(digest, **kwargs)  # noqa: E501
            return data

    def get_icon_with_http_info(self, digest, **kwargs):  # noqa: E501
        """Get artifact icon  # noqa: E501

        Get the artifact icon with the specified digest. As the original icon image is resized and encoded before returning, the parameter \"digest\" in the path doesn't match the hash of the returned content  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_icon_with_http_info(digest, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str digest: The digest of the resource (required)
        :param str x_request_id: An unique ID for the request
        :return: Icon
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["digest", "x_request_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method get_icon" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'digest' is set
        if self.api_client.client_side_validation and (
            "digest" not in params or params["digest"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `digest` when calling `get_icon`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `get_icon`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "digest" in params:
            path_params["digest"] = params["digest"]  # noqa: E501

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basic"]  # noqa: E501

        return self.api_client.call_api(
            "/icons/{digest}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Icon",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
