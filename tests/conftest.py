import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

_ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(copy.deepcopy(_ORIGINAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(_ORIGINAL_ACTIVITIES))
