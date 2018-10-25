# Body10

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | The id of the content document containing the parts or assemblies to be           inserted. | 
**element_id** | **str** | The id of the element containing the part(s), feature or assemblies to be           inserted. | 
**version_id** | **str** | The document versionId from which the parts or assembly to be inserted will           be taken. If documentId references a different document than did, this must be set to a valid version. | 
**microversion_id** | **str** | The document microversionId in which the elementId and partId will be           resolved. This is valid only if no versionId is specified. When a versionId is specified, the partId           must be obtained from the specified version. | 
**is_assembly** | **bool** | If true then the source element must be an assembly and whole assembly is           inserted. | 
**is_whole_part_studio** | **bool** | If true then the source element must be a partStudio and all parts           are inserted. | 
**part_id** | **str** | If isAssembly and isWholePartStudio are false, then this is the id of the part           or surface to be inserted. Must be left blank if featureId is set. | 
**feature_id** | **str** | If isAssembly and isWholePartStudio are false, then this is the id of the           feature to be inserted. Currently, only sketch features are valid. Must be left blank if partId is set. | 
**configuration** | **str** | Configuration of the source element, valid only if the           referenced element is a Part Studio. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

