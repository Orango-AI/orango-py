import pytest
from dotenv import load_dotenv

from orango import OrangoExecutionResult, Sandbox

load_dotenv()


def test_orango_execution():
    sandbox = Sandbox()
    sandbox.exec('x = 1')

    execution = sandbox.exec('x += 1; x')
    assert isinstance(execution, OrangoExecutionResult)
    assert execution.result == 2

    sandbox.close()
