# api-generator
This repo is responsible for generating an OpenAPI specification for the Onshape API based on the JSON definition pulled from the Endpoints endpoint. During that process, it incorporates the various endpoint definitions hand written in OnshapeOpenApiSpecTemplate.yaml. 

The most up-to-date version of the spec can always be found [here](https://github.com/onshape-public/api-generator/releases/latest).

## Downloading a new API definition
To download the API definition, you'll have to use API keys. The gruntfile expects the API keys to be located within the apikey.js file in the root. Modify the apikey.example.js to include your keys, then rename it to apikey.js. 
The API definition should be downloaded with the downloadApiDefinition grunt task, which can be run with:
`grunt downloadApiDefinition`
By defualt, this will place the downloaded file in the api_data folder with the name "apiData.json".

## Running the converter
To run the parser, update and run "python api_parser/json_to_openapi_2_0.py". So far, this command doesn't take command line arguments and you will therefore need to change the hardcoded values under the 'if __name__=="__main__": ' section at the end. There are a number of possible  

## Validating the generated OpenAPI definition
To validate the generated OpenAPI definition, copy and paste the code [here](http://editor.swagger.io/).

## Adding a new auto-generating client
This repo is responsible for kicking off the auto-generation of all dependent repos. When a new version of Onshape is released, the following happens:

1. After a successful new API release, the api-generator grunt task 'downloadApiDefinition' is run internally to generate the relevant OpenAPI spec, and then the parser task is run to parse the API definition into a valid OpenAPI spec. 
2. The resulting OpenAPI spec is validated using the online validator [here](http://online.swagger.io/validator), and if valid, continue to step 3.
3. The spec is committed to multiple "subscribing" repos (such as the various client SDKs) under their master branch in the root and labeled as "onshape_openapi_spec.yaml"
4. Each 'subscribing' repo creates a client SDK as each sees fit, usually using a CI tool such as Travis to run swagger codegen and tag the result, as described in [Incorporating the client with CI tools](Incorporating-the-client-with-CI-tools)

Through this process, we can always see the spec used to generate the client directly within the client source code, and we can easily add new clients to be notified when a new release happens.

## Incorporating the client with CI tools
The file is uploaded to the master branch of each of the clients. Each is responsible for taking the file and using it to update the relevant client. In general, the Travis file should perform the following:
1. Load information from the api.yaml file into the environment
2. Use the loaded information to build the client with swagger_codegen
3. Perform additional massages as needed to make the client work (should be something like a short script with some regex)
4. Test the client against some static tests to ensure against regressions
5. If the tests pass, tag the current commit with the given API version number and push the tag
6. Now that it is tagged, skip earlier steps, and run the deploy task to publish the client to the relevant package repository (pip, npm, etc...)

 ## Adding new Endpoints and Replacing the JSON with OpenAPI definitions
This repo has built in mechanisms to aid with the incremental transition from the Onshape JSON API definition to a OpenAPI definition. Parser starts with a valid OpenAPI template located here: OnshapeOpenApiSpecTemplate.yaml (from now on referred to as 'the template'). The parser then injects various paths and models that aren't already defined into the template. Therefore, by including the path manually within the template, we can use the hand written model/path rather than the one generated by the parser. In general, this process looks like:

1. (If replacing an endpoint that already exists) Run the parser to copy the current autogenerated OpenAPI definition for the model/path to be replaced.
2. (If replacing an endpoint that already exists) Paste the generated model/path into the template
3. Paste the template into the [Swagger editor](http://editor.swagger.io/) and change the inserted model/path to your liking.
4. Use the template to generate the server side interfaces, stub methods and test methods. This can be done using Swagger codegen. 
5. Publish the new template and the new server code.
6. Congratulations! You've updated/added some endpoints! 

