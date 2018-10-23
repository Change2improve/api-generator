# Body2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document ID (must match path parameter) | 
**workspace_id** | **str** | Workspace ID of a workspace where the version will be created if           fromHistory is false. If fromHistory is false and workspaceId is not set, the default workspace is           used. | [optional] 
**name** | **str** | Version name | 
**description** | **str** | Version description | [optional] 
**microversion_id** | **str** | Microversion ID at which to create the version if fromHistory is true | [optional] 
**from_history** | **bool** | Specifies whether to create a version at a specific microversion           (specified by microversionId) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


