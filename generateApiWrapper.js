// Update the default opts arg with the user-specified opts.
const defaults = {
    target: 'prod',
    api_keys: require('./apikey'),
    language: 'Python',
    includeInternalString: 'both',
    data: [],
    optionalParentDirectory: './generated'
};

function getEndpointsPromise(opts) {
    return new Promise(function (resolve, reject) {
        opts.data = require("./api_data/apiData");
        resolve(opts);
    })
}

function optsCheck(opts) {
    return new Promise(function (resolve, reject) {
            // opts.language is one of: python, C#
            // opts.includeInternalString is one of: yes, no, both
            opts = {
                ...defaults,
                ...opts
            };

            opts.language = opts.language.toLowerCase();
            opts.includeInternalString = opts.includeInternalString.toLowerCase();
            if (!['yes', 'no', 'both'].includes(opts.includeInternalString)) {
                reject(Error('Include internal option invalid. It must be one of "yes", "no", "both".'));
            }
            resolve(opts);

        }
    );
}

function buildLanguageWrapper(opts) {
    return new Promise(function (resolve, reject) {
        switch (opts.language) {
            case 'python':
                const generatePythonWrapper = require('./python/generatePythonWrapper').generatePythonWrapper; // TODO: change this to the real absolute path
                const directory = './' + opts.language + '/generated';
                if (opts.includeInternalString === 'yes' || opts.includeInternalString === 'both') {
                    let privateDirectory = directory;
                    if (opts.includeInternalString === 'both') {
                        privateDirectory = directory + '-private';
                    }
                    generatePythonWrapper(opts.data, privateDirectory, true).then(resolve("Generated private Python SDK client."))
                }
                if (opts.includeInternalString === 'no' || opts.includeInternalString === 'both') {
                    generatePythonWrapper(opts.data, directory, false).then(resolve("Generated public Python SDK client."));
                }
                break;
            default:
                reject(Error('Invalid language argument passed.'));
        }
    });
}

function buildWrapper(opts) {
    return new Promise(function (resolve, reject) {
        optsCheck(opts).then(getEndpointsPromise).then(buildLanguageWrapper).then(resolve("success"));
    })
}

module.exports = {
    buildWrapper: buildWrapper,
    defaults: defaults
};

// buildWrapper(defaults).catch(function(data) {console.log(data)});