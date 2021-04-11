# harbor_client
These APIs provide services for manipulating Harbor project.

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
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
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

# Configure HTTP basic authorization: basic
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
        api_instance.list_attahced_labels_of_chart(repo, name, version)
    except harbor_client.ApiException as e:
        print("Exception when calling ChartRepositoryApi->list_attahced_labels_of_chart: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api/v2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChartRepositoryApi* | [**list_attahced_labels_of_chart**](docs/ChartRepositoryApi.md#list_attahced_labels_of_chart) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
*ChartRepositoryApi* | [**mark_label_to_chart**](docs/ChartRepositoryApi.md#mark_label_to_chart) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.
*ChartRepositoryApi* | [**remove_label_from_chart**](docs/ChartRepositoryApi.md#remove_label_from_chart) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.
*LabelApi* | [**list_attahced_labels_of_chart**](docs/LabelApi.md#list_attahced_labels_of_chart) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
*LabelApi* | [**mark_label_to_chart**](docs/LabelApi.md#mark_label_to_chart) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.
*LabelApi* | [**remove_label_from_chart**](docs/LabelApi.md#remove_label_from_chart) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.
*LdapApi* | [**import_ldap_user**](docs/LdapApi.md#import_ldap_user) | **POST** /ldap/users/import | Import selected available ldap users.
*LdapApi* | [**ping_ldap**](docs/LdapApi.md#ping_ldap) | **POST** /ldap/ping | Ping available ldap service.
*LdapApi* | [**search_ldap_group**](docs/LdapApi.md#search_ldap_group) | **GET** /ldap/groups/search | Search available ldap groups.
*LdapApi* | [**search_ldap_user**](docs/LdapApi.md#search_ldap_user) | **GET** /ldap/users/search | Search available ldap users.
*ProductsApi* | [**all_project_members**](docs/ProductsApi.md#all_project_members) | **GET** /projects/{project_id}/members | Get all project member information
*ProductsApi* | [**change_password**](docs/ProductsApi.md#change_password) | **PUT** /users/{user_id}/password | Change the password on a user that already exists.
*ProductsApi* | [**create_label**](docs/ProductsApi.md#create_label) | **POST** /labels | Post creates a label
*ProductsApi* | [**create_project_member_relationship**](docs/ProductsApi.md#create_project_member_relationship) | **POST** /projects/{project_id}/members | Create project member
*ProductsApi* | [**create_user**](docs/ProductsApi.md#create_user) | **POST** /users | Creates a new user account.
*ProductsApi* | [**create_usergroup**](docs/ProductsApi.md#create_usergroup) | **POST** /usergroups | Create user group
*ProductsApi* | [**current_user**](docs/ProductsApi.md#current_user) | **GET** /users/current | Get current user info.
*ProductsApi* | [**current_user_permissions**](docs/ProductsApi.md#current_user_permissions) | **GET** /users/current/permissions | Get current user permissions.
*ProductsApi* | [**delete_project_member**](docs/ProductsApi.md#delete_project_member) | **DELETE** /projects/{project_id}/members/{mid} | Delete project member
*ProductsApi* | [**delete_usergroup**](docs/ProductsApi.md#delete_usergroup) | **DELETE** /usergroups/{group_id} | Delete user group
*ProductsApi* | [**email_ping**](docs/ProductsApi.md#email_ping) | **POST** /email/ping | Test connection and authentication with email server.
*ProductsApi* | [**health**](docs/ProductsApi.md#health) | **GET** /health | Health check API
*ProductsApi* | [**label**](docs/ProductsApi.md#label) | **GET** /labels/{id} | Get the label specified by ID.
*ProductsApi* | [**list_attahced_labels_of_chart**](docs/ProductsApi.md#list_attahced_labels_of_chart) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
*ProductsApi* | [**list_label**](docs/ProductsApi.md#list_label) | **GET** /labels | List labels according to the query strings.
*ProductsApi* | [**list_user_groups**](docs/ProductsApi.md#list_user_groups) | **GET** /usergroups | Get all user groups information
*ProductsApi* | [**make_admin**](docs/ProductsApi.md#make_admin) | **PUT** /users/{user_id}/sysadmin | Update a registered user to change to be an administrator of Harbor.
*ProductsApi* | [**mark_label_to_chart**](docs/ProductsApi.md#mark_label_to_chart) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.
*ProductsApi* | [**project_member**](docs/ProductsApi.md#project_member) | **GET** /projects/{project_id}/members/{mid} | Get the project member information
*ProductsApi* | [**project_metadata**](docs/ProductsApi.md#project_metadata) | **GET** /projects/{project_id}/metadatas | Get project metadata.
*ProductsApi* | [**remove_label_by_id**](docs/ProductsApi.md#remove_label_by_id) | **DELETE** /labels/{id} | Delete the label specified by ID.
*ProductsApi* | [**remove_label_from_chart**](docs/ProductsApi.md#remove_label_from_chart) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.
*ProductsApi* | [**remove_project_metadata**](docs/ProductsApi.md#remove_project_metadata) | **DELETE** /projects/{project_id}/metadatas/{meta_name} | Delete metadata of a project
*ProductsApi* | [**remove_user**](docs/ProductsApi.md#remove_user) | **DELETE** /users/{user_id} | Mark a registered user as be removed.
*ProductsApi* | [**search_user**](docs/ProductsApi.md#search_user) | **GET** /users/search | Search users by username
*ProductsApi* | [**set_cli_secret**](docs/ProductsApi.md#set_cli_secret) | **PUT** /users/{user_id}/cli_secret | Set CLI secret for a user.
*ProductsApi* | [**set_project_member**](docs/ProductsApi.md#set_project_member) | **PUT** /projects/{project_id}/members/{mid} | Update project member
*ProductsApi* | [**set_project_metadata**](docs/ProductsApi.md#set_project_metadata) | **POST** /projects/{project_id}/metadatas | Add metadata for the project.
*ProductsApi* | [**specified_project_metadata**](docs/ProductsApi.md#specified_project_metadata) | **GET** /projects/{project_id}/metadatas/{meta_name} | Get project metadata
*ProductsApi* | [**statistics**](docs/ProductsApi.md#statistics) | **GET** /statistics | Get projects number and repositories number relevant to the user
*ProductsApi* | [**system_configuration**](docs/ProductsApi.md#system_configuration) | **GET** /configurations | Get system configurations.
*ProductsApi* | [**update_label**](docs/ProductsApi.md#update_label) | **PUT** /labels/{id} | Update the label properties.
*ProductsApi* | [**update_project_metadata**](docs/ProductsApi.md#update_project_metadata) | **PUT** /projects/{project_id}/metadatas/{meta_name} | Update metadata of a project.
*ProductsApi* | [**update_system_configuration**](docs/ProductsApi.md#update_system_configuration) | **PUT** /configurations | Modify system configurations.
*ProductsApi* | [**update_user**](docs/ProductsApi.md#update_user) | **PUT** /users/{user_id} | Update a registered user to change his profile.
*ProductsApi* | [**update_usergroup**](docs/ProductsApi.md#update_usergroup) | **PUT** /usergroups/{group_id} | Update group information
*ProductsApi* | [**user**](docs/ProductsApi.md#user) | **GET** /users/{user_id} | Get a user&#39;s profile.
*ProductsApi* | [**usergroup**](docs/ProductsApi.md#usergroup) | **GET** /usergroups/{group_id} | Get user group information
*ProductsApi* | [**users**](docs/ProductsApi.md#users) | **GET** /users | Get registered users of Harbor.
*RetentionApi* | [**create_retention**](docs/RetentionApi.md#create_retention) | **POST** /retentions | Create Retention Policy
*RetentionApi* | [**get_rentenition_metadata**](docs/RetentionApi.md#get_rentenition_metadata) | **GET** /retentions/metadatas | Get Retention Metadatas
*RetentionApi* | [**get_retention**](docs/RetentionApi.md#get_retention) | **GET** /retentions/{id} | Get Retention Policy
*RetentionApi* | [**get_retention_task_log**](docs/RetentionApi.md#get_retention_task_log) | **GET** /retentions/{id}/executions/{eid}/tasks/{tid} | Get Retention job task log
*RetentionApi* | [**list_retention_executions**](docs/RetentionApi.md#list_retention_executions) | **GET** /retentions/{id}/executions | Get Retention executions
*RetentionApi* | [**list_retention_tasks**](docs/RetentionApi.md#list_retention_tasks) | **GET** /retentions/{id}/executions/{eid}/tasks | Get Retention tasks
*RetentionApi* | [**operate_retention_execution**](docs/RetentionApi.md#operate_retention_execution) | **PATCH** /retentions/{id}/executions/{eid} | Stop a Retention execution
*RetentionApi* | [**trigger_retention_execution**](docs/RetentionApi.md#trigger_retention_execution) | **POST** /retentions/{id}/executions | Trigger a Retention Execution
*RetentionApi* | [**update_retention**](docs/RetentionApi.md#update_retention) | **PUT** /retentions/{id} | Update Retention Policy
*SystemCVEAllowlistApi* | [**get_system_cve_allowlist**](docs/SystemCVEAllowlistApi.md#get_system_cve_allowlist) | **GET** /system/CVEAllowlist | Get the system level allowlist of CVE.
*SystemCVEAllowlistApi* | [**put_system_cve_allowlist**](docs/SystemCVEAllowlistApi.md#put_system_cve_allowlist) | **PUT** /system/CVEAllowlist | Update the system level allowlist of CVE.
*ArtifactApi* | [**add_label**](docs/ArtifactApi.md#add_label) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/labels | Add label to artifact
*ArtifactApi* | [**copy_artifact**](docs/ArtifactApi.md#copy_artifact) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts | Copy artifact
*ArtifactApi* | [**create_tag**](docs/ArtifactApi.md#create_tag) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags | Create tag
*ArtifactApi* | [**delete_artifact**](docs/ArtifactApi.md#delete_artifact) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference} | Delete the specific artifact
*ArtifactApi* | [**delete_tag**](docs/ArtifactApi.md#delete_tag) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags/{tag_name} | Delete tag
*ArtifactApi* | [**get_addition**](docs/ArtifactApi.md#get_addition) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/additions/{addition} | Get the addition of the specific artifact
*ArtifactApi* | [**get_artifact**](docs/ArtifactApi.md#get_artifact) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference} | Get the specific artifact
*ArtifactApi* | [**get_vulnerabilities_addition**](docs/ArtifactApi.md#get_vulnerabilities_addition) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/additions/vulnerabilities | Get the vulnerabilities addition of the specific artifact
*ArtifactApi* | [**list_artifacts**](docs/ArtifactApi.md#list_artifacts) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts | List artifacts
*ArtifactApi* | [**list_tags**](docs/ArtifactApi.md#list_tags) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags | List tags
*ArtifactApi* | [**remove_label**](docs/ArtifactApi.md#remove_label) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/labels/{label_id} | Remove label from artifact
*AuditlogApi* | [**list_audit_logs**](docs/AuditlogApi.md#list_audit_logs) | **GET** /audit-logs | Get recent logs of the projects which the user is a member of
*GcApi* | [**create_gc_schedule**](docs/GcApi.md#create_gc_schedule) | **POST** /system/gc/schedule | Create a gc schedule.
*GcApi* | [**get_gc**](docs/GcApi.md#get_gc) | **GET** /system/gc/{gc_id} | Get gc status.
*GcApi* | [**get_gc_history**](docs/GcApi.md#get_gc_history) | **GET** /system/gc | Get gc results.
*GcApi* | [**get_gc_log**](docs/GcApi.md#get_gc_log) | **GET** /system/gc/{gc_id}/log | Get gc job log.
*GcApi* | [**get_gc_schedule**](docs/GcApi.md#get_gc_schedule) | **GET** /system/gc/schedule | Get gc&#39;s schedule.
*GcApi* | [**update_gc_schedule**](docs/GcApi.md#update_gc_schedule) | **PUT** /system/gc/schedule | Update gc&#39;s schedule.
*IconApi* | [**get_icon**](docs/IconApi.md#get_icon) | **GET** /icons/{digest} | Get artifact icon
*ImmutableApi* | [**create_immu_rule**](docs/ImmutableApi.md#create_immu_rule) | **POST** /projects/{project_name_or_id}/immutabletagrules | Add an immutable tag rule to current project
*ImmutableApi* | [**delete_immu_rule**](docs/ImmutableApi.md#delete_immu_rule) | **DELETE** /projects/{project_name_or_id}/immutabletagrules/{immutable_rule_id} | Delete the immutable tag rule.
*ImmutableApi* | [**list_immu_rules**](docs/ImmutableApi.md#list_immu_rules) | **GET** /projects/{project_name_or_id}/immutabletagrules | List all immutable tag rules of current project
*ImmutableApi* | [**update_immu_rule**](docs/ImmutableApi.md#update_immu_rule) | **PUT** /projects/{project_name_or_id}/immutabletagrules/{immutable_rule_id} | Update the immutable tag rule or enable or disable the rule
*OidcApi* | [**ping_oidc**](docs/OidcApi.md#ping_oidc) | **POST** /system/oidc/ping | Test the OIDC endpoint.
*PingApi* | [**ping**](docs/PingApi.md#ping) | **GET** /ping | Ping Harbor to check if it&#39;s alive.
*PreheatApi* | [**create_instance**](docs/PreheatApi.md#create_instance) | **POST** /p2p/preheat/instances | Create p2p provider instances
*PreheatApi* | [**create_policy**](docs/PreheatApi.md#create_policy) | **POST** /projects/{project_name}/preheat/policies | Create a preheat policy under a project
*PreheatApi* | [**delete_instance**](docs/PreheatApi.md#delete_instance) | **DELETE** /p2p/preheat/instances/{preheat_instance_name} | Delete the specified P2P provider instance
*PreheatApi* | [**delete_policy**](docs/PreheatApi.md#delete_policy) | **DELETE** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Delete a preheat policy
*PreheatApi* | [**get_execution**](docs/PreheatApi.md#get_execution) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id} | Get a execution detail by id
*PreheatApi* | [**get_instance**](docs/PreheatApi.md#get_instance) | **GET** /p2p/preheat/instances/{preheat_instance_name} | Get a P2P provider instance
*PreheatApi* | [**get_policy**](docs/PreheatApi.md#get_policy) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Get a preheat policy
*PreheatApi* | [**get_preheat_log**](docs/PreheatApi.md#get_preheat_log) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id}/tasks/{task_id}/logs | Get the log text stream of the specified task for the given execution
*PreheatApi* | [**list_executions**](docs/PreheatApi.md#list_executions) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions | List executions for the given policy
*PreheatApi* | [**list_instances**](docs/PreheatApi.md#list_instances) | **GET** /p2p/preheat/instances | List P2P provider instances
*PreheatApi* | [**list_policies**](docs/PreheatApi.md#list_policies) | **GET** /projects/{project_name}/preheat/policies | List preheat policies
*PreheatApi* | [**list_providers**](docs/PreheatApi.md#list_providers) | **GET** /p2p/preheat/providers | List P2P providers
*PreheatApi* | [**list_providers_under_project**](docs/PreheatApi.md#list_providers_under_project) | **GET** /projects/{project_name}/preheat/providers | Get all providers at project level
*PreheatApi* | [**list_tasks**](docs/PreheatApi.md#list_tasks) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id}/tasks | List all the related tasks for the given execution
*PreheatApi* | [**manual_preheat**](docs/PreheatApi.md#manual_preheat) | **POST** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Manual preheat
*PreheatApi* | [**ping_instances**](docs/PreheatApi.md#ping_instances) | **POST** /p2p/preheat/instances/ping | Ping status of a instance.
*PreheatApi* | [**stop_execution**](docs/PreheatApi.md#stop_execution) | **PATCH** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id} | Stop a execution
*PreheatApi* | [**update_instance**](docs/PreheatApi.md#update_instance) | **PUT** /p2p/preheat/instances/{preheat_instance_name} | Update the specified P2P provider instance
*PreheatApi* | [**update_policy**](docs/PreheatApi.md#update_policy) | **PUT** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Update preheat policy
*ProjectApi* | [**create_project**](docs/ProjectApi.md#create_project) | **POST** /projects | Create a new project.
*ProjectApi* | [**delete_project**](docs/ProjectApi.md#delete_project) | **DELETE** /projects/{project_name_or_id} | Delete project by projectID
*ProjectApi* | [**get_logs**](docs/ProjectApi.md#get_logs) | **GET** /projects/{project_name}/logs | Get recent logs of the projects
*ProjectApi* | [**get_project**](docs/ProjectApi.md#get_project) | **GET** /projects/{project_name_or_id} | Return specific project detail information
*ProjectApi* | [**get_project_deletable**](docs/ProjectApi.md#get_project_deletable) | **GET** /projects/{project_name_or_id}/_deletable | Get the deletable status of the project
*ProjectApi* | [**get_project_summary**](docs/ProjectApi.md#get_project_summary) | **GET** /projects/{project_name_or_id}/summary | Get summary of the project.
*ProjectApi* | [**get_scanner_of_project**](docs/ProjectApi.md#get_scanner_of_project) | **GET** /projects/{project_name_or_id}/scanner | Get project level scanner
*ProjectApi* | [**head_project**](docs/ProjectApi.md#head_project) | **HEAD** /projects | Check if the project name user provided already exists.
*ProjectApi* | [**list_projects**](docs/ProjectApi.md#list_projects) | **GET** /projects | List projects
*ProjectApi* | [**list_scanner_candidates_of_project**](docs/ProjectApi.md#list_scanner_candidates_of_project) | **GET** /projects/{project_name_or_id}/scanner/candidates | Get scanner registration candidates for configurating project level scanner
*ProjectApi* | [**set_scanner_of_project**](docs/ProjectApi.md#set_scanner_of_project) | **PUT** /projects/{project_name_or_id}/scanner | Configure scanner for the specified project
*ProjectApi* | [**update_project**](docs/ProjectApi.md#update_project) | **PUT** /projects/{project_name_or_id} | Update properties for a selected project.
*QuotaApi* | [**get_quota**](docs/QuotaApi.md#get_quota) | **GET** /quotas/{id} | Get the specified quota
*QuotaApi* | [**list_quotas**](docs/QuotaApi.md#list_quotas) | **GET** /quotas | List quotas
*QuotaApi* | [**update_quota**](docs/QuotaApi.md#update_quota) | **PUT** /quotas/{id} | Update the specified quota
*RegistryApi* | [**create_registry**](docs/RegistryApi.md#create_registry) | **POST** /registries | Create a registry
*RegistryApi* | [**delete_registry**](docs/RegistryApi.md#delete_registry) | **DELETE** /registries/{id} | Delete the specific registry
*RegistryApi* | [**get_registry**](docs/RegistryApi.md#get_registry) | **GET** /registries/{id} | Get the specific registry
*RegistryApi* | [**get_registry_info**](docs/RegistryApi.md#get_registry_info) | **GET** /registries/{id}/info | Get the registry info
*RegistryApi* | [**list_registries**](docs/RegistryApi.md#list_registries) | **GET** /registries | List the registries
*RegistryApi* | [**list_registry_provider_infos**](docs/RegistryApi.md#list_registry_provider_infos) | **GET** /replication/adapterinfos | List all registered registry provider information
*RegistryApi* | [**list_registry_provider_types**](docs/RegistryApi.md#list_registry_provider_types) | **GET** /replication/adapters | List registry adapters
*RegistryApi* | [**ping_registry**](docs/RegistryApi.md#ping_registry) | **POST** /registries/ping | Check status of a registry
*RegistryApi* | [**update_registry**](docs/RegistryApi.md#update_registry) | **PUT** /registries/{id} | Update the registry
*ReplicationApi* | [**create_replication_policy**](docs/ReplicationApi.md#create_replication_policy) | **POST** /replication/policies | Create a replication policy
*ReplicationApi* | [**delete_replication_policy**](docs/ReplicationApi.md#delete_replication_policy) | **DELETE** /replication/policies/{id} | Delete the specific replication policy
*ReplicationApi* | [**get_replication_execution**](docs/ReplicationApi.md#get_replication_execution) | **GET** /replication/executions/{id} | Get the specific replication execution
*ReplicationApi* | [**get_replication_log**](docs/ReplicationApi.md#get_replication_log) | **GET** /replication/executions/{id}/tasks/{task_id}/log | Get the log of the specific replication task
*ReplicationApi* | [**get_replication_policy**](docs/ReplicationApi.md#get_replication_policy) | **GET** /replication/policies/{id} | Get the specific replication policy
*ReplicationApi* | [**list_replication_executions**](docs/ReplicationApi.md#list_replication_executions) | **GET** /replication/executions | List replication executions
*ReplicationApi* | [**list_replication_policies**](docs/ReplicationApi.md#list_replication_policies) | **GET** /replication/policies | List replication policies
*ReplicationApi* | [**list_replication_tasks**](docs/ReplicationApi.md#list_replication_tasks) | **GET** /replication/executions/{id}/tasks | List replication tasks for a specific execution
*ReplicationApi* | [**start_replication**](docs/ReplicationApi.md#start_replication) | **POST** /replication/executions | Start one replication execution
*ReplicationApi* | [**stop_replication**](docs/ReplicationApi.md#stop_replication) | **PUT** /replication/executions/{id} | Stop the specific replication execution
*ReplicationApi* | [**update_replication_policy**](docs/ReplicationApi.md#update_replication_policy) | **PUT** /replication/policies/{id} | Update the replication policy
*RepositoryApi* | [**delete_repository**](docs/RepositoryApi.md#delete_repository) | **DELETE** /projects/{project_name}/repositories/{repository_name} | Delete repository
*RepositoryApi* | [**get_repository**](docs/RepositoryApi.md#get_repository) | **GET** /projects/{project_name}/repositories/{repository_name} | Get repository
*RepositoryApi* | [**list_repositories**](docs/RepositoryApi.md#list_repositories) | **GET** /projects/{project_name}/repositories | List repositories
*RepositoryApi* | [**update_repository**](docs/RepositoryApi.md#update_repository) | **PUT** /projects/{project_name}/repositories/{repository_name} | Update repository
*RobotApi* | [**create_robot**](docs/RobotApi.md#create_robot) | **POST** /robots | Create a robot account
*RobotApi* | [**delete_robot**](docs/RobotApi.md#delete_robot) | **DELETE** /robots/{robot_id} | Delete a robot account
*RobotApi* | [**get_robot_by_id**](docs/RobotApi.md#get_robot_by_id) | **GET** /robots/{robot_id} | Get a robot account
*RobotApi* | [**list_robot**](docs/RobotApi.md#list_robot) | **GET** /robots | Get robot account
*RobotApi* | [**refresh_sec**](docs/RobotApi.md#refresh_sec) | **PATCH** /robots/{robot_id} | Refresh the robot secret
*RobotApi* | [**update_robot**](docs/RobotApi.md#update_robot) | **PUT** /robots/{robot_id} | Update a robot account
*Robotv1Api* | [**create_robot_v1**](docs/Robotv1Api.md#create_robot_v1) | **POST** /projects/{project_name_or_id}/robots | Create a robot account
*Robotv1Api* | [**delete_robot_v1**](docs/Robotv1Api.md#delete_robot_v1) | **DELETE** /projects/{project_name_or_id}/robots/{robot_id} | Delete a robot account
*Robotv1Api* | [**get_robot_by_idv1**](docs/Robotv1Api.md#get_robot_by_idv1) | **GET** /projects/{project_name_or_id}/robots/{robot_id} | Get a robot account
*Robotv1Api* | [**list_robot_v1**](docs/Robotv1Api.md#list_robot_v1) | **GET** /projects/{project_name_or_id}/robots | Get all robot accounts of specified project
*Robotv1Api* | [**update_robot_v1**](docs/Robotv1Api.md#update_robot_v1) | **PUT** /projects/{project_name_or_id}/robots/{robot_id} | Update status of robot account.
*ScanApi* | [**get_report_log**](docs/ScanApi.md#get_report_log) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan/{report_id}/log | Get the log of the scan report
*ScanApi* | [**scan_artifact**](docs/ScanApi.md#scan_artifact) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan | Scan the artifact
*ScanAllApi* | [**create_scan_all_schedule**](docs/ScanAllApi.md#create_scan_all_schedule) | **POST** /system/scanAll/schedule | Create a schedule or a manual trigger for the scan all job.
*ScanAllApi* | [**get_latest_scan_all_metrics**](docs/ScanAllApi.md#get_latest_scan_all_metrics) | **GET** /scans/all/metrics | Get the metrics of the latest scan all process
*ScanAllApi* | [**get_latest_scheduled_scan_all_metrics**](docs/ScanAllApi.md#get_latest_scheduled_scan_all_metrics) | **GET** /scans/schedule/metrics | Get the metrics of the latest scheduled scan all process
*ScanAllApi* | [**get_scan_all_schedule**](docs/ScanAllApi.md#get_scan_all_schedule) | **GET** /system/scanAll/schedule | Get scan all&#39;s schedule.
*ScanAllApi* | [**update_scan_all_schedule**](docs/ScanAllApi.md#update_scan_all_schedule) | **PUT** /system/scanAll/schedule | Update scan all&#39;s schedule.
*ScannerApi* | [**create_scanner**](docs/ScannerApi.md#create_scanner) | **POST** /scanners | Create a scanner registration
*ScannerApi* | [**delete_scanner**](docs/ScannerApi.md#delete_scanner) | **DELETE** /scanners/{registration_id} | Delete a scanner registration
*ScannerApi* | [**get_scanner**](docs/ScannerApi.md#get_scanner) | **GET** /scanners/{registration_id} | Get a scanner registration details
*ScannerApi* | [**get_scanner_metadata**](docs/ScannerApi.md#get_scanner_metadata) | **GET** /scanners/{registration_id}/metadata | Get the metadata of the specified scanner registration
*ScannerApi* | [**list_scanners**](docs/ScannerApi.md#list_scanners) | **GET** /scanners | List scanner registrations
*ScannerApi* | [**ping_scanner**](docs/ScannerApi.md#ping_scanner) | **POST** /scanners/ping | Tests scanner registration settings
*ScannerApi* | [**set_scanner_as_default**](docs/ScannerApi.md#set_scanner_as_default) | **PATCH** /scanners/{registration_id} | Set system default scanner registration
*ScannerApi* | [**update_scanner**](docs/ScannerApi.md#update_scanner) | **PUT** /scanners/{registration_id} | Update a scanner registration
*SearchApi* | [**search**](docs/SearchApi.md#search) | **GET** /search | Search for projects, repositories and helm charts
*SysteminfoApi* | [**systeminfo**](docs/SysteminfoApi.md#systeminfo) | **GET** /systeminfo | Get general system info
*SysteminfoApi* | [**systeminfo_cert**](docs/SysteminfoApi.md#systeminfo_cert) | **GET** /systeminfo/getcert | Get default root certificate.
*SysteminfoApi* | [**systeminfo_volumes**](docs/SysteminfoApi.md#systeminfo_volumes) | **GET** /systeminfo/volumes | Get system volume info (total/free size).
*WebhookApi* | [**create_webhook_policy_of_project**](docs/WebhookApi.md#create_webhook_policy_of_project) | **POST** /projects/{project_name_or_id}/webhook/policies | Create project webhook policy.
*WebhookApi* | [**delete_webhook_policy_of_project**](docs/WebhookApi.md#delete_webhook_policy_of_project) | **DELETE** /projects/{project_name_or_id}/webhook/policies/{webhook_policy_id} | Delete webhook policy of a project
*WebhookApi* | [**get_supported_event_types**](docs/WebhookApi.md#get_supported_event_types) | **GET** /projects/{project_name_or_id}/webhook/events | Get supported event types and notify types.
*WebhookApi* | [**get_webhook_policy_of_project**](docs/WebhookApi.md#get_webhook_policy_of_project) | **GET** /projects/{project_name_or_id}/webhook/policies/{webhook_policy_id} | Get project webhook policy
*WebhookApi* | [**last_trigger**](docs/WebhookApi.md#last_trigger) | **GET** /projects/{project_name_or_id}/webhook/lasttrigger | Get project webhook policy last trigger info
*WebhookApi* | [**list_webhook_policies_of_project**](docs/WebhookApi.md#list_webhook_policies_of_project) | **GET** /projects/{project_name_or_id}/webhook/policies | List project webhook policies.
*WebhookApi* | [**update_webhook_policy_of_project**](docs/WebhookApi.md#update_webhook_policy_of_project) | **PUT** /projects/{project_name_or_id}/webhook/policies/{webhook_policy_id} | Update webhook policy of a project.
*WebhookjobApi* | [**list_webhook_jobs**](docs/WebhookjobApi.md#list_webhook_jobs) | **GET** /projects/{project_name_or_id}/webhook/jobs | List project webhook jobs


## Documentation For Models

 - [Access](docs/Access.md)
 - [AdditionLink](docs/AdditionLink.md)
 - [AdditionLinks](docs/AdditionLinks.md)
 - [Annotations](docs/Annotations.md)
 - [Artifact](docs/Artifact.md)
 - [AuditLog](docs/AuditLog.md)
 - [AuthproxySetting](docs/AuthproxySetting.md)
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
 - [ConfigurationsScanAllPolicy](docs/ConfigurationsScanAllPolicy.md)
 - [ConfigurationsScanAllPolicyParameter](docs/ConfigurationsScanAllPolicyParameter.md)
 - [ConflictFormatedError](docs/ConflictFormatedError.md)
 - [EmailServerSetting](docs/EmailServerSetting.md)
 - [Error](docs/Error.md)
 - [Errors](docs/Errors.md)
 - [Execution](docs/Execution.md)
 - [ExtraAttrs](docs/ExtraAttrs.md)
 - [FilterStyle](docs/FilterStyle.md)
 - [ForbiddenChartAPIError](docs/ForbiddenChartAPIError.md)
 - [GCHistory](docs/GCHistory.md)
 - [GeneralInfo](docs/GeneralInfo.md)
 - [Icon](docs/Icon.md)
 - [ImmutableRule](docs/ImmutableRule.md)
 - [ImmutableSelector](docs/ImmutableSelector.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [Instance](docs/Instance.md)
 - [InsufficientStorageChartAPIError](docs/InsufficientStorageChartAPIError.md)
 - [IntegerConfigItem](docs/IntegerConfigItem.md)
 - [InternalChartAPIError](docs/InternalChartAPIError.md)
 - [IsDefault](docs/IsDefault.md)
 - [Label](docs/Label.md)
 - [Labels](docs/Labels.md)
 - [LdapConf](docs/LdapConf.md)
 - [LdapFailedImportUser](docs/LdapFailedImportUser.md)
 - [LdapFailedImportUsers](docs/LdapFailedImportUsers.md)
 - [LdapImportUsers](docs/LdapImportUsers.md)
 - [LdapPingResult](docs/LdapPingResult.md)
 - [LdapUser](docs/LdapUser.md)
 - [LdapUsers](docs/LdapUsers.md)
 - [Metadata](docs/Metadata.md)
 - [Metrics](docs/Metrics.md)
 - [Namespace](docs/Namespace.md)
 - [NativeReportSummary](docs/NativeReportSummary.md)
 - [NotFoundChartAPIError](docs/NotFoundChartAPIError.md)
 - [OverallHealthStatus](docs/OverallHealthStatus.md)
 - [Password](docs/Password.md)
 - [Permission](docs/Permission.md)
 - [Platform](docs/Platform.md)
 - [PreheatPolicy](docs/PreheatPolicy.md)
 - [Project](docs/Project.md)
 - [ProjectDeletable](docs/ProjectDeletable.md)
 - [ProjectMember](docs/ProjectMember.md)
 - [ProjectMemberEntity](docs/ProjectMemberEntity.md)
 - [ProjectMetadata](docs/ProjectMetadata.md)
 - [ProjectReq](docs/ProjectReq.md)
 - [ProjectScanner](docs/ProjectScanner.md)
 - [ProjectSummary](docs/ProjectSummary.md)
 - [ProjectSummaryQuota](docs/ProjectSummaryQuota.md)
 - [ProviderUnderProject](docs/ProviderUnderProject.md)
 - [Quota](docs/Quota.md)
 - [QuotaRefObject](docs/QuotaRefObject.md)
 - [QuotaSwitcher](docs/QuotaSwitcher.md)
 - [QuotaUpdateReq](docs/QuotaUpdateReq.md)
 - [Reference](docs/Reference.md)
 - [Registry](docs/Registry.md)
 - [RegistryCredential](docs/RegistryCredential.md)
 - [RegistryEndpoint](docs/RegistryEndpoint.md)
 - [RegistryInfo](docs/RegistryInfo.md)
 - [RegistryPing](docs/RegistryPing.md)
 - [RegistryProviderCredentialPattern](docs/RegistryProviderCredentialPattern.md)
 - [RegistryProviderEndpointPattern](docs/RegistryProviderEndpointPattern.md)
 - [RegistryProviderInfo](docs/RegistryProviderInfo.md)
 - [RegistryUpdate](docs/RegistryUpdate.md)
 - [ReplicationExecution](docs/ReplicationExecution.md)
 - [ReplicationFilter](docs/ReplicationFilter.md)
 - [ReplicationPolicy](docs/ReplicationPolicy.md)
 - [ReplicationTask](docs/ReplicationTask.md)
 - [ReplicationTrigger](docs/ReplicationTrigger.md)
 - [ReplicationTriggerSettings](docs/ReplicationTriggerSettings.md)
 - [Repository](docs/Repository.md)
 - [ResourceList](docs/ResourceList.md)
 - [RetentionExecution](docs/RetentionExecution.md)
 - [RetentionExecutionTask](docs/RetentionExecutionTask.md)
 - [RetentionMetadata](docs/RetentionMetadata.md)
 - [RetentionPolicy](docs/RetentionPolicy.md)
 - [RetentionPolicyScope](docs/RetentionPolicyScope.md)
 - [RetentionRule](docs/RetentionRule.md)
 - [RetentionRuleMetadata](docs/RetentionRuleMetadata.md)
 - [RetentionRuleParamMetadata](docs/RetentionRuleParamMetadata.md)
 - [RetentionRuleTrigger](docs/RetentionRuleTrigger.md)
 - [RetentionSelector](docs/RetentionSelector.md)
 - [RetentionSelectorMetadata](docs/RetentionSelectorMetadata.md)
 - [Robot](docs/Robot.md)
 - [RobotCreate](docs/RobotCreate.md)
 - [RobotCreateV1](docs/RobotCreateV1.md)
 - [RobotCreated](docs/RobotCreated.md)
 - [RobotPermission](docs/RobotPermission.md)
 - [RobotSec](docs/RobotSec.md)
 - [Role](docs/Role.md)
 - [RoleParam](docs/RoleParam.md)
 - [RoleRequest](docs/RoleRequest.md)
 - [ScanOverview](docs/ScanOverview.md)
 - [Scanner](docs/Scanner.md)
 - [ScannerAdapterMetadata](docs/ScannerAdapterMetadata.md)
 - [ScannerCapability](docs/ScannerCapability.md)
 - [ScannerRegistration](docs/ScannerRegistration.md)
 - [ScannerRegistrationReq](docs/ScannerRegistrationReq.md)
 - [ScannerRegistrationSettings](docs/ScannerRegistrationSettings.md)
 - [Schedule](docs/Schedule.md)
 - [ScheduleObj](docs/ScheduleObj.md)
 - [Search](docs/Search.md)
 - [SearchRepository](docs/SearchRepository.md)
 - [SearchResult](docs/SearchResult.md)
 - [StartReplicationExecution](docs/StartReplicationExecution.md)
 - [StatisticMap](docs/StatisticMap.md)
 - [Stats](docs/Stats.md)
 - [Storage](docs/Storage.md)
 - [StringConfigItem](docs/StringConfigItem.md)
 - [SupportedWebhookEventTypes](docs/SupportedWebhookEventTypes.md)
 - [SysAdminFlag](docs/SysAdminFlag.md)
 - [SystemInfo](docs/SystemInfo.md)
 - [Tag](docs/Tag.md)
 - [Task](docs/Task.md)
 - [UnauthorizedChartAPIError](docs/UnauthorizedChartAPIError.md)
 - [User](docs/User.md)
 - [UserEntity](docs/UserEntity.md)
 - [UserGroup](docs/UserGroup.md)
 - [UserProfile](docs/UserProfile.md)
 - [UserSearch](docs/UserSearch.md)
 - [VulnerabilitySummary](docs/VulnerabilitySummary.md)
 - [WebhookJob](docs/WebhookJob.md)
 - [WebhookLastTrigger](docs/WebhookLastTrigger.md)
 - [WebhookPolicy](docs/WebhookPolicy.md)
 - [WebhookTargetObject](docs/WebhookTargetObject.md)


## Documentation For Authorization


## basic

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

