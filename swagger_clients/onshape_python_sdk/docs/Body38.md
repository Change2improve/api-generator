# Body38

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rollback_index** | **float** | The index at which the rollback index should be placed. Features   with entry index (0-based) higher than or equal to this value are rolled back.  The value -1 is treated   as an alias for \&quot;end of feature list\&quot;.  Otherwise the value must be in the range 0 to the number of   entries in the feature list | 
**serialization_version** | **str** | The version of the serialization protocol for features | 
**source_microversion** | **str** | The document microversion from which the features were extracted | 
**reject_microversion_skew** | **bool** | If set to true and the element has changed since     sourceMicroversion, return an HTTP Conflict status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


