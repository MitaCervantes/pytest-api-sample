import requests

from conftest import EnvironmentVars


def get_project():
    workspaceId = "Ingresar Workspace Id"
    projectId = "Ingresar Project Id"
    baseUrl = "https://api.clockify.me/api/v1"
    endpoint = "/workspaces/" + workspaceId + "/projects/" + projectId
    url = baseUrl + endpoint
    headers = {'X-Api-Key':'Ingresar Api Key'}
    response = requests.get(url, headers=headers)

    return response
