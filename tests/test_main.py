import os

import pytest
from dotenv import load_dotenv

from orango import OrangoException, OrangoExecutionResult, Sandbox

load_dotenv()

@pytest.fixture(scope="module")
def sandbox():
    api_key = os.getenv('ORANGO_APIKEY')
    base_url = os.getenv('ORANGO_BASE_URL')
    sandbox = Sandbox.create(api_key=api_key, base_url=base_url)
    yield sandbox
    sandbox.close()

def test_execute_code(sandbox):
    sandbox.exec("x = 1")
    execution = sandbox.exec("x += 1; x")
    assert isinstance(execution, OrangoExecutionResult)
    assert execution.result == 2

def test_multiple_code_executions(sandbox):
    sandbox.exec("y = 5")
    execution1 = sandbox.exec("y *= 2; y")
    assert isinstance(execution1, OrangoExecutionResult)
    assert execution1.result == 10
    execution2 = sandbox.exec("y += 10; y")
    assert isinstance(execution2, OrangoExecutionResult)
    assert execution2.result == 20

def test_handle_errors_in_code_execution(sandbox):
    with pytest.raises(OrangoException) as excinfo:
        sandbox.exec("z += 1")
    assert "name 'z' is not defined" in excinfo.value.stderr
