# InlineResponse20017Parts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document ID of the document containing the part | 
**document_microversion** | **str** | Document microversion ID of the document containing             the part | 
**document_version** | **str** | Version ID of document containing the part, if reached             through one or more version references | 
**element_id** | **str** | Element ID | 
**part_id** | **str** | Deterministic part ID. If the part cannot be resolved, the value             will be the empty string. This can happen if a change in the source part studio causes the part that             was originally referenced to be missing. | 
**configuration** | **str** | Configuration of the Part studio element. | 
**body_type** | **str** | Type of part body. Current values that are possible are solid,             sheet. Others may be added in the future. | 
**is_standard_content** | **bool** | Indicates whether the part is Standard Content. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


