import pytest
from jsonschema import validate
from commons.jsonOpen import open_schema
from conftest import EnvironmentVars
from apis.api_clockify import get_project


class TestGetTokenEndpoint:

    @pytest.fixture
    def project(self):
        return get_project()

    @pytest.mark.academy
    def test_get_project(self, project):
        response = project
        assert response.status_code == 200
        expected_name = 'ProyectoEjemplo'
        assert response.json()['name'] == expected_name
        response_data = response.json()
        validate(response_data, open_schema('proyecto'))
