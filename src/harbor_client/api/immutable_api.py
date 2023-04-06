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


class ImmutableApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_immu_rule(self, project_name_or_id, immutable_rule, **kwargs):  # noqa: E501
        """Add an immutable tag rule to current project  # noqa: E501

        This endpoint add an immutable tag rule to the project   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_immu_rule(project_name_or_id, immutable_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param ImmutableRule immutable_rule: (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_immu_rule_with_http_info(
                project_name_or_id, immutable_rule, **kwargs
            )  # noqa: E501
        else:
            (data) = self.create_immu_rule_with_http_info(
                project_name_or_id, immutable_rule, **kwargs
            )  # noqa: E501
            return data

    def create_immu_rule_with_http_info(
        self, project_name_or_id, immutable_rule, **kwargs
    ):  # noqa: E501
        """Add an immutable tag rule to current project  # noqa: E501

        This endpoint add an immutable tag rule to the project   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_immu_rule_with_http_info(project_name_or_id, immutable_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param ImmutableRule immutable_rule: (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "project_name_or_id",
            "immutable_rule",
            "x_request_id",
            "x_is_resource_name",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method create_immu_rule" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and (
            "project_name_or_id" not in params or params["project_name_or_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `project_name_or_id` when calling `create_immu_rule`"
            )  # noqa: E501
        # verify the required parameter 'immutable_rule' is set
        if self.api_client.client_side_validation and (
            "immutable_rule" not in params or params["immutable_rule"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `immutable_rule` when calling `create_immu_rule`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `create_immu_rule`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "project_name_or_id" in params:
            path_params["project_name_or_id"] = params["project_name_or_id"]  # noqa: E501

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501
        if "x_is_resource_name" in params:
            header_params["X-Is-Resource-Name"] = params["x_is_resource_name"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if "immutable_rule" in params:
            body_params = params["immutable_rule"]
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
            "/projects/{project_name_or_id}/immutabletagrules",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_immu_rule(self, project_name_or_id, immutable_rule_id, **kwargs):  # noqa: E501
        """Delete the immutable tag rule.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_immu_rule(project_name_or_id, immutable_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param int immutable_rule_id: The ID of the immutable rule (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_immu_rule_with_http_info(
                project_name_or_id, immutable_rule_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_immu_rule_with_http_info(
                project_name_or_id, immutable_rule_id, **kwargs
            )  # noqa: E501
            return data

    def delete_immu_rule_with_http_info(
        self, project_name_or_id, immutable_rule_id, **kwargs
    ):  # noqa: E501
        """Delete the immutable tag rule.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_immu_rule_with_http_info(project_name_or_id, immutable_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param int immutable_rule_id: The ID of the immutable rule (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "project_name_or_id",
            "immutable_rule_id",
            "x_request_id",
            "x_is_resource_name",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method delete_immu_rule" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and (
            "project_name_or_id" not in params or params["project_name_or_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `project_name_or_id` when calling `delete_immu_rule`"
            )  # noqa: E501
        # verify the required parameter 'immutable_rule_id' is set
        if self.api_client.client_side_validation and (
            "immutable_rule_id" not in params or params["immutable_rule_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `immutable_rule_id` when calling `delete_immu_rule`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `delete_immu_rule`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "project_name_or_id" in params:
            path_params["project_name_or_id"] = params["project_name_or_id"]  # noqa: E501
        if "immutable_rule_id" in params:
            path_params["immutable_rule_id"] = params["immutable_rule_id"]  # noqa: E501

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501
        if "x_is_resource_name" in params:
            header_params["X-Is-Resource-Name"] = params["x_is_resource_name"]  # noqa: E501

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
            "/projects/{project_name_or_id}/immutabletagrules/{immutable_rule_id}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_immu_rules(self, project_name_or_id, **kwargs):  # noqa: E501
        """List all immutable tag rules of current project  # noqa: E501

        This endpoint returns the immutable tag rules of a project   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_immu_rules(project_name_or_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :param int page: The page number
        :param int page_size: The size of per page
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param str sort: Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\"
        :return: list[ImmutableRule]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_immu_rules_with_http_info(project_name_or_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_immu_rules_with_http_info(project_name_or_id, **kwargs)  # noqa: E501
            return data

    def list_immu_rules_with_http_info(self, project_name_or_id, **kwargs):  # noqa: E501
        """List all immutable tag rules of current project  # noqa: E501

        This endpoint returns the immutable tag rules of a project   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_immu_rules_with_http_info(project_name_or_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :param int page: The page number
        :param int page_size: The size of per page
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param str sort: Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\"
        :return: list[ImmutableRule]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "project_name_or_id",
            "x_request_id",
            "x_is_resource_name",
            "page",
            "page_size",
            "q",
            "sort",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method list_immu_rules" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and (
            "project_name_or_id" not in params or params["project_name_or_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `project_name_or_id` when calling `list_immu_rules`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `list_immu_rules`, length must be greater than or equal to `1`"
            )  # noqa: E501
        if self.api_client.client_side_validation and (
            "page_size" in params and params["page_size"] > 100
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for parameter `page_size` when calling `list_immu_rules`, must be a value less than or equal to `100`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "project_name_or_id" in params:
            path_params["project_name_or_id"] = params["project_name_or_id"]  # noqa: E501

        query_params = []
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("page_size", params["page_size"]))  # noqa: E501
        if "q" in params:
            query_params.append(("q", params["q"]))  # noqa: E501
        if "sort" in params:
            query_params.append(("sort", params["sort"]))  # noqa: E501

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501
        if "x_is_resource_name" in params:
            header_params["X-Is-Resource-Name"] = params["x_is_resource_name"]  # noqa: E501

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
            "/projects/{project_name_or_id}/immutabletagrules",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ImmutableRule]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_immu_rule(
        self, project_name_or_id, immutable_rule_id, immutable_rule, **kwargs
    ):  # noqa: E501
        """Update the immutable tag rule or enable or disable the rule  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_immu_rule(project_name_or_id, immutable_rule_id, immutable_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param int immutable_rule_id: The ID of the immutable rule (required)
        :param ImmutableRule immutable_rule: (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_immu_rule_with_http_info(
                project_name_or_id, immutable_rule_id, immutable_rule, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_immu_rule_with_http_info(
                project_name_or_id, immutable_rule_id, immutable_rule, **kwargs
            )  # noqa: E501
            return data

    def update_immu_rule_with_http_info(
        self, project_name_or_id, immutable_rule_id, immutable_rule, **kwargs
    ):  # noqa: E501
        """Update the immutable tag rule or enable or disable the rule  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_immu_rule_with_http_info(project_name_or_id, immutable_rule_id, immutable_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param int immutable_rule_id: The ID of the immutable rule (required)
        :param ImmutableRule immutable_rule: (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "project_name_or_id",
            "immutable_rule_id",
            "immutable_rule",
            "x_request_id",
            "x_is_resource_name",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method update_immu_rule" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and (
            "project_name_or_id" not in params or params["project_name_or_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `project_name_or_id` when calling `update_immu_rule`"
            )  # noqa: E501
        # verify the required parameter 'immutable_rule_id' is set
        if self.api_client.client_side_validation and (
            "immutable_rule_id" not in params or params["immutable_rule_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `immutable_rule_id` when calling `update_immu_rule`"
            )  # noqa: E501
        # verify the required parameter 'immutable_rule' is set
        if self.api_client.client_side_validation and (
            "immutable_rule" not in params or params["immutable_rule"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `immutable_rule` when calling `update_immu_rule`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `update_immu_rule`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "project_name_or_id" in params:
            path_params["project_name_or_id"] = params["project_name_or_id"]  # noqa: E501
        if "immutable_rule_id" in params:
            path_params["immutable_rule_id"] = params["immutable_rule_id"]  # noqa: E501

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501
        if "x_is_resource_name" in params:
            header_params["X-Is-Resource-Name"] = params["x_is_resource_name"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if "immutable_rule" in params:
            body_params = params["immutable_rule"]
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
            "/projects/{project_name_or_id}/immutabletagrules/{immutable_rule_id}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
