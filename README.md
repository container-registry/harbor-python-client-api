# Harbor Python Client
These APIs provide services for manipulating Harbor Container Registry Version >2.2.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0
- Package version: 2.2
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/container-registry/harbor-python-client-api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import harbor_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import harbor_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import harbor_client
from pprint import pprint
from harbor_client.api import chart_repository_api
from harbor_client.model.label import Label
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = chart_repository_api.ChartRepositoryApi(api_client)
    repo = "repo_example" # str | The project name
name = "name_example" # str | The chart name
version = "version_example" # str | The chart version

    try:
        # Return the attahced labels of chart.
        api_instance.chartrepo_repo_charts_name_version_labels_get(repo, name, version)
    except harbor_client.ApiException as e:
        print("Exception when calling ChartRepositoryApi->chartrepo_repo_charts_name_version_labels_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api/v2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChartRepositoryApi* | [**chartrepo_repo_charts_name_version_labels_get**](docs/ChartRepositoryApi.md#chartrepo_repo_charts_name_version_labels_get) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
*ChartRepositoryApi* | [**chartrepo_repo_charts_name_version_labels_id_delete**](docs/ChartRepositoryApi.md#chartrepo_repo_charts_name_version_labels_id_delete) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.
*ChartRepositoryApi* | [**chartrepo_repo_charts_name_version_labels_post**](docs/ChartRepositoryApi.md#chartrepo_repo_charts_name_version_labels_post) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.
*LabelApi* | [**chartrepo_repo_charts_name_version_labels_get**](docs/LabelApi.md#chartrepo_repo_charts_name_version_labels_get) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
*LabelApi* | [**chartrepo_repo_charts_name_version_labels_id_delete**](docs/LabelApi.md#chartrepo_repo_charts_name_version_labels_id_delete) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.
*LabelApi* | [**chartrepo_repo_charts_name_version_labels_post**](docs/LabelApi.md#chartrepo_repo_charts_name_version_labels_post) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.
*ProductsApi* | [**chartrepo_repo_charts_name_version_labels_get**](docs/ProductsApi.md#chartrepo_repo_charts_name_version_labels_get) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
*ProductsApi* | [**chartrepo_repo_charts_name_version_labels_id_delete**](docs/ProductsApi.md#chartrepo_repo_charts_name_version_labels_id_delete) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.
*ProductsApi* | [**chartrepo_repo_charts_name_version_labels_post**](docs/ProductsApi.md#chartrepo_repo_charts_name_version_labels_post) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.
*ProductsApi* | [**configurations_get**](docs/ProductsApi.md#configurations_get) | **GET** /configurations | Get system configurations.
*ProductsApi* | [**configurations_put**](docs/ProductsApi.md#configurations_put) | **PUT** /configurations | Modify system configurations.
*ProductsApi* | [**email_ping_post**](docs/ProductsApi.md#email_ping_post) | **POST** /email/ping | Test connection and authentication with email server.
*ProductsApi* | [**health_get**](docs/ProductsApi.md#health_get) | **GET** /health | Health check API
*ProductsApi* | [**labels_get**](docs/ProductsApi.md#labels_get) | **GET** /labels | List labels according to the query strings.
*ProductsApi* | [**labels_id_delete**](docs/ProductsApi.md#labels_id_delete) | **DELETE** /labels/{id} | Delete the label specified by ID.
*ProductsApi* | [**labels_id_get**](docs/ProductsApi.md#labels_id_get) | **GET** /labels/{id} | Get the label specified by ID.
*ProductsApi* | [**labels_id_put**](docs/ProductsApi.md#labels_id_put) | **PUT** /labels/{id} | Update the label properties.
*ProductsApi* | [**labels_post**](docs/ProductsApi.md#labels_post) | **POST** /labels | Post creates a label
*ProductsApi* | [**ldap_groups_search_get**](docs/ProductsApi.md#ldap_groups_search_get) | **GET** /ldap/groups/search | Search available ldap groups.
*ProductsApi* | [**ldap_ping_post**](docs/ProductsApi.md#ldap_ping_post) | **POST** /ldap/ping | Ping available ldap service.
*ProductsApi* | [**ldap_users_import_post**](docs/ProductsApi.md#ldap_users_import_post) | **POST** /ldap/users/import | Import selected available ldap users.
*ProductsApi* | [**ldap_users_search_get**](docs/ProductsApi.md#ldap_users_search_get) | **GET** /ldap/users/search | Search available ldap users.
*ProductsApi* | [**projects_project_id_immutabletagrules_get**](docs/ProductsApi.md#projects_project_id_immutabletagrules_get) | **GET** /projects/{project_id}/immutabletagrules | List all immutable tag rules of current project
*ProductsApi* | [**projects_project_id_immutabletagrules_id_delete**](docs/ProductsApi.md#projects_project_id_immutabletagrules_id_delete) | **DELETE** /projects/{project_id}/immutabletagrules/{id} | Delete the immutable tag rule.
*ProductsApi* | [**projects_project_id_immutabletagrules_id_put**](docs/ProductsApi.md#projects_project_id_immutabletagrules_id_put) | **PUT** /projects/{project_id}/immutabletagrules/{id} | Update the immutable tag rule or enable or disable the rule
*ProductsApi* | [**projects_project_id_immutabletagrules_post**](docs/ProductsApi.md#projects_project_id_immutabletagrules_post) | **POST** /projects/{project_id}/immutabletagrules | Add an immutable tag rule to current project
*ProductsApi* | [**projects_project_id_members_get**](docs/ProductsApi.md#projects_project_id_members_get) | **GET** /projects/{project_id}/members | Get all project member information
*ProductsApi* | [**projects_project_id_members_mid_delete**](docs/ProductsApi.md#projects_project_id_members_mid_delete) | **DELETE** /projects/{project_id}/members/{mid} | Delete project member
*ProductsApi* | [**projects_project_id_members_mid_get**](docs/ProductsApi.md#projects_project_id_members_mid_get) | **GET** /projects/{project_id}/members/{mid} | Get the project member information
*ProductsApi* | [**projects_project_id_members_mid_put**](docs/ProductsApi.md#projects_project_id_members_mid_put) | **PUT** /projects/{project_id}/members/{mid} | Update project member
*ProductsApi* | [**projects_project_id_members_post**](docs/ProductsApi.md#projects_project_id_members_post) | **POST** /projects/{project_id}/members | Create project member
*ProductsApi* | [**projects_project_id_metadatas_get**](docs/ProductsApi.md#projects_project_id_metadatas_get) | **GET** /projects/{project_id}/metadatas | Get project metadata.
*ProductsApi* | [**projects_project_id_metadatas_meta_name_delete**](docs/ProductsApi.md#projects_project_id_metadatas_meta_name_delete) | **DELETE** /projects/{project_id}/metadatas/{meta_name} | Delete metadata of a project
*ProductsApi* | [**projects_project_id_metadatas_meta_name_get**](docs/ProductsApi.md#projects_project_id_metadatas_meta_name_get) | **GET** /projects/{project_id}/metadatas/{meta_name} | Get project metadata
*ProductsApi* | [**projects_project_id_metadatas_meta_name_put**](docs/ProductsApi.md#projects_project_id_metadatas_meta_name_put) | **PUT** /projects/{project_id}/metadatas/{meta_name} | Update metadata of a project.
*ProductsApi* | [**projects_project_id_metadatas_post**](docs/ProductsApi.md#projects_project_id_metadatas_post) | **POST** /projects/{project_id}/metadatas | Add metadata for the project.
*ProductsApi* | [**projects_project_id_scanner_candidates_get**](docs/ProductsApi.md#projects_project_id_scanner_candidates_get) | **GET** /projects/{project_id}/scanner/candidates | Get scanner registration candidates for configurating project level scanner
*ProductsApi* | [**projects_project_id_scanner_get**](docs/ProductsApi.md#projects_project_id_scanner_get) | **GET** /projects/{project_id}/scanner | Get project level scanner
*ProductsApi* | [**projects_project_id_webhook_events_get**](docs/ProductsApi.md#projects_project_id_webhook_events_get) | **GET** /projects/{project_id}/webhook/events | Get supported event types and notify types.
*ProductsApi* | [**projects_project_id_webhook_jobs_get**](docs/ProductsApi.md#projects_project_id_webhook_jobs_get) | **GET** /projects/{project_id}/webhook/jobs | List project webhook jobs
*ProductsApi* | [**projects_project_id_webhook_lasttrigger_get**](docs/ProductsApi.md#projects_project_id_webhook_lasttrigger_get) | **GET** /projects/{project_id}/webhook/lasttrigger | Get project webhook policy last trigger info
*ProductsApi* | [**projects_project_id_webhook_policies_get**](docs/ProductsApi.md#projects_project_id_webhook_policies_get) | **GET** /projects/{project_id}/webhook/policies | List project webhook policies.
*ProductsApi* | [**projects_project_id_webhook_policies_policy_id_delete**](docs/ProductsApi.md#projects_project_id_webhook_policies_policy_id_delete) | **DELETE** /projects/{project_id}/webhook/policies/{policy_id} | Delete webhook policy of a project
*ProductsApi* | [**projects_project_id_webhook_policies_policy_id_get**](docs/ProductsApi.md#projects_project_id_webhook_policies_policy_id_get) | **GET** /projects/{project_id}/webhook/policies/{policy_id} | Get project webhook policy
*ProductsApi* | [**projects_project_id_webhook_policies_policy_id_put**](docs/ProductsApi.md#projects_project_id_webhook_policies_policy_id_put) | **PUT** /projects/{project_id}/webhook/policies/{policy_id} | Update webhook policy of a project.
*ProductsApi* | [**projects_project_id_webhook_policies_post**](docs/ProductsApi.md#projects_project_id_webhook_policies_post) | **POST** /projects/{project_id}/webhook/policies | Create project webhook policy.
*ProductsApi* | [**projects_project_id_webhook_policies_test_post**](docs/ProductsApi.md#projects_project_id_webhook_policies_test_post) | **POST** /projects/{project_id}/webhook/policies/test | Test project webhook connection
*ProductsApi* | [**quotas_get**](docs/ProductsApi.md#quotas_get) | **GET** /quotas | List quotas
*ProductsApi* | [**quotas_id_get**](docs/ProductsApi.md#quotas_id_get) | **GET** /quotas/{id} | Get the specified quota
*ProductsApi* | [**quotas_id_put**](docs/ProductsApi.md#quotas_id_put) | **PUT** /quotas/{id} | Update the specified quota
*ProductsApi* | [**registries_get**](docs/ProductsApi.md#registries_get) | **GET** /registries | List registries.
*ProductsApi* | [**registries_id_delete**](docs/ProductsApi.md#registries_id_delete) | **DELETE** /registries/{id} | Delete specific registry.
*ProductsApi* | [**registries_id_get**](docs/ProductsApi.md#registries_id_get) | **GET** /registries/{id} | Get registry.
*ProductsApi* | [**registries_id_info_get**](docs/ProductsApi.md#registries_id_info_get) | **GET** /registries/{id}/info | Get registry info.
*ProductsApi* | [**registries_id_namespace_get**](docs/ProductsApi.md#registries_id_namespace_get) | **GET** /registries/{id}/namespace | List namespaces of registry
*ProductsApi* | [**registries_id_put**](docs/ProductsApi.md#registries_id_put) | **PUT** /registries/{id} | Update a given registry.
*ProductsApi* | [**registries_ping_post**](docs/ProductsApi.md#registries_ping_post) | **POST** /registries/ping | Ping status of a registry.
*ProductsApi* | [**registries_post**](docs/ProductsApi.md#registries_post) | **POST** /registries | Create a new registry.
*ProductsApi* | [**replication_adapters_get**](docs/ProductsApi.md#replication_adapters_get) | **GET** /replication/adapters | List supported adapters.
*ProductsApi* | [**replication_policies_get**](docs/ProductsApi.md#replication_policies_get) | **GET** /replication/policies | List replication policies
*ProductsApi* | [**replication_policies_id_delete**](docs/ProductsApi.md#replication_policies_id_delete) | **DELETE** /replication/policies/{id} | Delete the replication policy specified by ID.
*ProductsApi* | [**replication_policies_id_get**](docs/ProductsApi.md#replication_policies_id_get) | **GET** /replication/policies/{id} | Get replication policy.
*ProductsApi* | [**replication_policies_id_put**](docs/ProductsApi.md#replication_policies_id_put) | **PUT** /replication/policies/{id} | Update the replication policy
*ProductsApi* | [**replication_policies_post**](docs/ProductsApi.md#replication_policies_post) | **POST** /replication/policies | Create a replication policy
*ProductsApi* | [**scanners_get**](docs/ProductsApi.md#scanners_get) | **GET** /scanners | List scanner registrations
*ProductsApi* | [**scanners_ping_post**](docs/ProductsApi.md#scanners_ping_post) | **POST** /scanners/ping | Tests scanner registration settings
*ProductsApi* | [**scanners_registration_id_get**](docs/ProductsApi.md#scanners_registration_id_get) | **GET** /scanners/{registration_id} | Get a scanner registration details
*ProductsApi* | [**scanners_registration_id_metadata_get**](docs/ProductsApi.md#scanners_registration_id_metadata_get) | **GET** /scanners/{registration_id}/metadata | Get the metadata of the specified scanner registration
*ProductsApi* | [**search_get**](docs/ProductsApi.md#search_get) | **GET** /search | Search for projects, repositories and helm charts
*ProductsApi* | [**statistics_get**](docs/ProductsApi.md#statistics_get) | **GET** /statistics | Get projects number and repositories number relevant to the user
*ProductsApi* | [**system_cve_allowlist_get**](docs/ProductsApi.md#system_cve_allowlist_get) | **GET** /system/CVEAllowlist | Get the system level allowlist of CVE.
*ProductsApi* | [**system_cve_allowlist_put**](docs/ProductsApi.md#system_cve_allowlist_put) | **PUT** /system/CVEAllowlist | Update the system level allowlist of CVE.
*ProductsApi* | [**system_oidc_ping_post**](docs/ProductsApi.md#system_oidc_ping_post) | **POST** /system/oidc/ping | Test the OIDC endpoint.
*ProductsApi* | [**usergroups_get**](docs/ProductsApi.md#usergroups_get) | **GET** /usergroups | Get all user groups information
*ProductsApi* | [**usergroups_group_id_delete**](docs/ProductsApi.md#usergroups_group_id_delete) | **DELETE** /usergroups/{group_id} | Delete user group
*ProductsApi* | [**usergroups_group_id_get**](docs/ProductsApi.md#usergroups_group_id_get) | **GET** /usergroups/{group_id} | Get user group information
*ProductsApi* | [**usergroups_group_id_put**](docs/ProductsApi.md#usergroups_group_id_put) | **PUT** /usergroups/{group_id} | Update group information
*ProductsApi* | [**usergroups_post**](docs/ProductsApi.md#usergroups_post) | **POST** /usergroups | Create user group
*ProductsApi* | [**users_current_get**](docs/ProductsApi.md#users_current_get) | **GET** /users/current | Get current user info.
*ProductsApi* | [**users_current_permissions_get**](docs/ProductsApi.md#users_current_permissions_get) | **GET** /users/current/permissions | Get current user permissions.
*ProductsApi* | [**users_get**](docs/ProductsApi.md#users_get) | **GET** /users | Get registered users of Harbor.
*ProductsApi* | [**users_post**](docs/ProductsApi.md#users_post) | **POST** /users | Creates a new user account.
*ProductsApi* | [**users_search_get**](docs/ProductsApi.md#users_search_get) | **GET** /users/search | Search users by username
*ProductsApi* | [**users_user_id_cli_secret_put**](docs/ProductsApi.md#users_user_id_cli_secret_put) | **PUT** /users/{user_id}/cli_secret | Set CLI secret for a user.
*ProductsApi* | [**users_user_id_delete**](docs/ProductsApi.md#users_user_id_delete) | **DELETE** /users/{user_id} | Mark a registered user as be removed.
*ProductsApi* | [**users_user_id_get**](docs/ProductsApi.md#users_user_id_get) | **GET** /users/{user_id} | Get a user&#39;s profile.
*ProductsApi* | [**users_user_id_password_put**](docs/ProductsApi.md#users_user_id_password_put) | **PUT** /users/{user_id}/password | Change the password on a user that already exists.
*ProductsApi* | [**users_user_id_put**](docs/ProductsApi.md#users_user_id_put) | **PUT** /users/{user_id} | Update a registered user to change his profile.
*ProductsApi* | [**users_user_id_sysadmin_put**](docs/ProductsApi.md#users_user_id_sysadmin_put) | **PUT** /users/{user_id}/sysadmin | Update a registered user to change to be an administrator of Harbor.
*QuotaApi* | [**quotas_id_get**](docs/QuotaApi.md#quotas_id_get) | **GET** /quotas/{id} | Get the specified quota
*QuotaApi* | [**quotas_id_put**](docs/QuotaApi.md#quotas_id_put) | **PUT** /quotas/{id} | Update the specified quota
*ScannersApi* | [**projects_project_id_scanner_candidates_get**](docs/ScannersApi.md#projects_project_id_scanner_candidates_get) | **GET** /projects/{project_id}/scanner/candidates | Get scanner registration candidates for configurating project level scanner
*ScannersApi* | [**projects_project_id_scanner_get**](docs/ScannersApi.md#projects_project_id_scanner_get) | **GET** /projects/{project_id}/scanner | Get project level scanner
*ScannersApi* | [**projects_project_id_scanner_put**](docs/ScannersApi.md#projects_project_id_scanner_put) | **PUT** /projects/{project_id}/scanner | Configure scanner for the specified project
*ScannersApi* | [**scanners_get**](docs/ScannersApi.md#scanners_get) | **GET** /scanners | List scanner registrations
*ScannersApi* | [**scanners_ping_post**](docs/ScannersApi.md#scanners_ping_post) | **POST** /scanners/ping | Tests scanner registration settings
*ScannersApi* | [**scanners_post**](docs/ScannersApi.md#scanners_post) | **POST** /scanners | Create a scanner registration
*ScannersApi* | [**scanners_registration_id_delete**](docs/ScannersApi.md#scanners_registration_id_delete) | **DELETE** /scanners/{registration_id} | Delete a scanner registration
*ScannersApi* | [**scanners_registration_id_get**](docs/ScannersApi.md#scanners_registration_id_get) | **GET** /scanners/{registration_id} | Get a scanner registration details
*ScannersApi* | [**scanners_registration_id_metadata_get**](docs/ScannersApi.md#scanners_registration_id_metadata_get) | **GET** /scanners/{registration_id}/metadata | Get the metadata of the specified scanner registration
*ScannersApi* | [**scanners_registration_id_patch**](docs/ScannersApi.md#scanners_registration_id_patch) | **PATCH** /scanners/{registration_id} | Set system default scanner registration
*ScannersApi* | [**scanners_registration_id_put**](docs/ScannersApi.md#scanners_registration_id_put) | **PUT** /scanners/{registration_id} | Update a scanner registration
*SystemApi* | [**system_cve_allowlist_get**](docs/SystemApi.md#system_cve_allowlist_get) | **GET** /system/CVEAllowlist | Get the system level allowlist of CVE.
*SystemApi* | [**system_cve_allowlist_put**](docs/SystemApi.md#system_cve_allowlist_put) | **PUT** /system/CVEAllowlist | Update the system level allowlist of CVE.
*SystemApi* | [**system_oidc_ping_post**](docs/SystemApi.md#system_oidc_ping_post) | **POST** /system/oidc/ping | Test the OIDC endpoint.


## Documentation For Models

 - [BadRequestFormatedError](docs/BadRequestFormatedError.md)
 - [BoolConfigItem](docs/BoolConfigItem.md)
 - [CVEAllowlist](docs/CVEAllowlist.md)
 - [CVEAllowlistItem](docs/CVEAllowlistItem.md)
 - [ChartAPIError](docs/ChartAPIError.md)
 - [ChartMetadata](docs/ChartMetadata.md)
 - [ChartVersion](docs/ChartVersion.md)
 - [ChartVersionAllOf](docs/ChartVersionAllOf.md)
 - [ComponentHealthStatus](docs/ComponentHealthStatus.md)
 - [ComponentOverviewEntry](docs/ComponentOverviewEntry.md)
 - [Configurations](docs/Configurations.md)
 - [ConfigurationsResponse](docs/ConfigurationsResponse.md)
 - [ConfigurationsResponseScanAllPolicy](docs/ConfigurationsResponseScanAllPolicy.md)
 - [ConfigurationsResponseScanAllPolicyParameter](docs/ConfigurationsResponseScanAllPolicyParameter.md)
 - [ConflictFormatedError](docs/ConflictFormatedError.md)
 - [EmailServerSetting](docs/EmailServerSetting.md)
 - [FilterStyle](docs/FilterStyle.md)
 - [ForbiddenChartAPIError](docs/ForbiddenChartAPIError.md)
 - [ImmutableRule](docs/ImmutableRule.md)
 - [ImmutableSelector](docs/ImmutableSelector.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InsufficientStorageChartAPIError](docs/InsufficientStorageChartAPIError.md)
 - [IntegerConfigItem](docs/IntegerConfigItem.md)
 - [InternalChartAPIError](docs/InternalChartAPIError.md)
 - [IsDefault](docs/IsDefault.md)
 - [Label](docs/Label.md)
 - [Labels](docs/Labels.md)
 - [LdapConf](docs/LdapConf.md)
 - [LdapFailedImportUsers](docs/LdapFailedImportUsers.md)
 - [LdapImportUsers](docs/LdapImportUsers.md)
 - [LdapUsers](docs/LdapUsers.md)
 - [Namespace](docs/Namespace.md)
 - [NotFoundChartAPIError](docs/NotFoundChartAPIError.md)
 - [OverallHealthStatus](docs/OverallHealthStatus.md)
 - [Password](docs/Password.md)
 - [Permission](docs/Permission.md)
 - [PingRegistry](docs/PingRegistry.md)
 - [Project](docs/Project.md)
 - [ProjectMember](docs/ProjectMember.md)
 - [ProjectMemberEntity](docs/ProjectMemberEntity.md)
 - [ProjectMetadata](docs/ProjectMetadata.md)
 - [ProjectReq](docs/ProjectReq.md)
 - [ProjectScanner](docs/ProjectScanner.md)
 - [ProjectSummary](docs/ProjectSummary.md)
 - [ProjectSummaryQuota](docs/ProjectSummaryQuota.md)
 - [PutRegistry](docs/PutRegistry.md)
 - [Quota](docs/Quota.md)
 - [QuotaRefObject](docs/QuotaRefObject.md)
 - [QuotaSwitcher](docs/QuotaSwitcher.md)
 - [QuotaUpdateReq](docs/QuotaUpdateReq.md)
 - [Registry](docs/Registry.md)
 - [RegistryCredential](docs/RegistryCredential.md)
 - [RegistryInfo](docs/RegistryInfo.md)
 - [ReplicationFilter](docs/ReplicationFilter.md)
 - [ReplicationPolicy](docs/ReplicationPolicy.md)
 - [ReplicationTrigger](docs/ReplicationTrigger.md)
 - [ResourceList](docs/ResourceList.md)
 - [Role](docs/Role.md)
 - [RoleParam](docs/RoleParam.md)
 - [RoleRequest](docs/RoleRequest.md)
 - [Scanner](docs/Scanner.md)
 - [ScannerAdapterMetadata](docs/ScannerAdapterMetadata.md)
 - [ScannerCapability](docs/ScannerCapability.md)
 - [ScannerRegistration](docs/ScannerRegistration.md)
 - [ScannerRegistrationReq](docs/ScannerRegistrationReq.md)
 - [ScannerRegistrationSettings](docs/ScannerRegistrationSettings.md)
 - [Search](docs/Search.md)
 - [SearchRepository](docs/SearchRepository.md)
 - [SearchResult](docs/SearchResult.md)
 - [StatisticMap](docs/StatisticMap.md)
 - [StringConfigItem](docs/StringConfigItem.md)
 - [SupportedWebhookEventTypes](docs/SupportedWebhookEventTypes.md)
 - [SysAdminFlag](docs/SysAdminFlag.md)
 - [TriggerSettings](docs/TriggerSettings.md)
 - [UnauthorizedChartAPIError](docs/UnauthorizedChartAPIError.md)
 - [User](docs/User.md)
 - [UserEntity](docs/UserEntity.md)
 - [UserGroup](docs/UserGroup.md)
 - [UserProfile](docs/UserProfile.md)
 - [UserSearch](docs/UserSearch.md)
 - [WebhookJob](docs/WebhookJob.md)
 - [WebhookLastTrigger](docs/WebhookLastTrigger.md)
 - [WebhookPolicy](docs/WebhookPolicy.md)
 - [WebhookTargetObject](docs/WebhookTargetObject.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in harbor_client.apis and harbor_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from harbor_client.api.default_api import DefaultApi`
- `from harbor_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import harbor_client
from harbor_client.apis import *
from harbor_client.models import *
```

