import uuid
import dvc.api
import argo_workflows
from argo_workflows.api import workflow_service_api


params = dvc.api.params_show()['argo']
argo_host = params['host']
argo_bearer_token = params['bearer_token']
argo_namespace = params['namespace']

hucs = params['hucs'].split(",")

configuration = argo_workflows.Configuration(host=argo_host)
configuration.api_key['BearerToken'] = argo_bearer_token

api_client = argo_workflows.ApiClient(configuration)
api_instance = workflow_service_api.WorkflowServiceApi(api_client)

def parameters(hucs: list, workflow_name = str(uuid.uuid4())):
    template_name = "parflow-subset-v1-by-huc-minio"
    return {
        "resourceKind": "WorkflowTemplate",
        "resourceName": template_name,
        "submitOptions": {
            "name": workflow_name,
            "parameters":[f"job-id={workflow_name}", "hucs=" + ",".join(hucs)],
        }
    }


if __name__ == "__main__":  # pragma: no cover
    api_instance.submit_workflow(namespace=argo_namespace, body=parameters(hucs), _preload_content=False)
