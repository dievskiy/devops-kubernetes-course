const k8s = require('@kubernetes/client-node')
const mustache = require('mustache')
const request = require('request')
const JSONStream = require('json-stream')
const fs = require('fs').promises

const kc = new k8s.KubeConfig();

process.env.NODE_ENV === 'development' ? kc.loadFromDefault() : kc.loadFromCluster()

const opts = {}
kc.applyToRequest(opts)

const client = kc.makeApiClient(k8s.CoreV1Api);

const sendRequestToApi = async (api, method = 'get', options = {}) => new Promise((resolve, reject) => request[method](`${kc.getCurrentCluster().server}${api}`, {...opts, ...options, headers: { ...options.headers, ...opts.headers }}, (err, res) => err ? reject(err) : resolve(JSON.parse(res.body))))

const fieldsFromDummysite = (object) => ({
    dummysite_name: object.metadata.name,
    namespace: object.metadata.namespace,
    website_url: object.spec.website_url
})

const getDeploymentYAML = async (fields) => {
    const deploymentTemplate = await fs.readFile("deployment.mustache", "utf-8")
    return mustache.render(deploymentTemplate, fields)
}

const createDeployment = async (fields) => {
    console.log('Scheduling new deployment for dummysite ', fields.dummysite_name, 'to namespace', fields.namespace)

    const yaml = await getDeploymentYAML(fields)

    return sendRequestToApi(`/apis/apps/v1/namespaces/${fields.namespace}/deployments`, 'post', {
        headers: {
            'Content-Type': 'application/yaml'
        },
        body: yaml
    })
}

const removeDeployment = async ({ namespace, deployment_name }) => {
    return sendRequestToApi(`/apis/apps/v1/namespaces/${namespace}/deployments/${deployment_name}`, 'delete')
}

const removeDummysite = ({ namespace, dummysite_name }) => sendRequestToApi(`/apis/stable.dwk/v1/namespaces/${namespace}/dummysites/${dummysite_name}`, 'delete')

const cleanupFordummysite = async ({ namespace, dummysite_name }) => {
    console.log(`Deleting resources for dummy site ${dummysite_name}`)
    await removeDeployment({ namespace, deployment_name: dummysite_name })
    await removeDummysite({ namespace, dummysite_name })
}

const maintainStatus = async () => {
    (await client.listPodForAllNamespaces()).body // A bug in the client(?) was fixed by sending a request and not caring about response

    /**
     * Watch dummysites
     */

    const dummysite_stream = new JSONStream()

    dummysite_stream.on('data', async ({ type, object }) => {
        const fields = fieldsFromDummysite(object)

        if (type === 'ADDED') {
            createDeployment(fields)
        }
        if (type === 'DELETED') cleanupFordummysite(fields)
    })

    request.get(`${kc.getCurrentCluster().server}/apis/stable.dwk/v1/dummysites?watch=true`, opts).pipe(dummysite_stream)

    /**
     * Watch Deployments
     */

    const deployment_stream = new JSONStream()

    deployment_stream.on('data', async ({ type, object }) => {
        if (!object?.metadata?.labels?.dummysite) return
        if (type === 'DELETED' || object.metadata.deletionTimestamp) return
        if (!object?.status?.succeeded) return
    })

    request.get(`${kc.getCurrentCluster().server}/apis/apps/v1/deployments?watch=true`, opts).pipe(deployment_stream)
}

maintainStatus()