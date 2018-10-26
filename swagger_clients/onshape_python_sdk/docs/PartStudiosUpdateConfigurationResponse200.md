# PartStudiosUpdateConfigurationResponse200

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_parameters** | **list[object]** | List of configuration parameters, which define the             configurability of the Part Studio. | [optional] 
**serialization_version** | **str** | The version of the serialization protocol for the response | [optional] 
**source_microversion** | **str** | The document microversion from which the feature was extracted | [optional] 
**microversion_skew** | **bool** | Set to true if the part studio element had changed since the     sourceMicroversion specified on input.  Applicable only if rejectMicroversionSkew was not set to true | [optional] 
**current_configuration** | **list[object]** | List of parameter settings, which define the current             configuration Part Studio. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

