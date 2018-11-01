'use strict';
var fs = require('fs');
// Using request instead of Onshape because the authorization headers throw a 406
const request = require('request');

// Update the default opts arg with the user-specified opts.
const defaults = {
    api_data_file_path: './api_data/apiData.json',
    target: 'prod',
    api_keys: require('./apikey'),
    language: 'Python',
    includeInternalString: 'both',
    data: [],
    optionalParentDirectory: './generated'
};


module.exports = function (grunt) {
    grunt.initConfig({
        task: {}
    });
    grunt.registerTask('downloadApiDefinition', function () {
        // Update the default opts arg with the user-specified opts.
        let opts = flagsToFields(defaults);
        const apiKey = opts.api_keys[opts.target];
        const client = require('@onshape/apikey/lib/app')(apiKey);
        const done = this.async();

        function getEndpointsPromise(opts) {
            return new Promise(function (resolve, reject) {
                if (!(opts.target in opts.api_keys)) {
                    reject(Error("The target, " + opts.target + " doesn't exist in the passed in apikeys."));
                }
                client.getEndpoints(function (data) {
                    console.log("Endpoint data received, first 100 chars of endpoint definition: " + data.slice(0,100));
                    request('https://cad.onshape.com/api/build', {json: true}, (err, res, version) => {
                        if (err) {
                            return console.log(err);
                        }
                        console.log("Version data recieved, implementation version is: " + version["Implementation-Version"]);
                        const d = {groups: JSON.parse(data), version: version}
                        fs.writeFile(opts.api_data_file_path, JSON.stringify(d), function (err) {
                            if (err) {
                                return console.log(err);
                            }
                            console.log("The file was saved!");
                            resolve(d);
                        });
                    });
                    // client.onshape.get({path: "/api/build"}, function (version) {
                    //     console.log(version);
                    //     fs.writeFile(opts.api_data_file_path, {data: data, version: version}, function (err) {
                    //         if (err) {
                    //             return console.log(err);
                    //         }
                    //         console.log("The file was saved!");
                    //         resolve(data);
                    //     });
                    // });
                });
            })
        }

        getEndpointsPromise(opts).then(done);
    });
    grunt.registerTask('generateApiWrapper',
        'Generates a wrapper library around Onshape\'s API for the specified language', function () {
            // Get defaults and modify as needed from the grunt options flags.
            let opts = flagsToFields(defaults);
            // Use done in order to let grunt wait for everything to finish.
            const done = this.async();

            // Call the generator
            const buildWrapper = require('./generateApiWrapper').buildWrapper;
            buildWrapper(opts).catch(function (data) {
                console.log(data)
            });
        }
    );
    grunt.registerTask('downloadAndGenerateApiWrapper', ['downloadApiDefinition', 'generateApiWrapper']);

    function flagsToFields(defaults) {
        // For converting grunt flags to keys of a dictionary
        let userOpts = {};
        let flags = [];
        let x;
        for (x in grunt.option.flags()) {
            flags.push(grunt.option.flags()[x].split(/[-=]+/)[1]);
        }
        let i;
        for (i in flags) {
            userOpts[flags[i]] = grunt.option(flags[i]);
        }
        return {
            ...defaults,
            ...userOpts
        };
    }
};


