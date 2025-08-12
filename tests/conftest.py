import pytest

from tests.dataclass import ChorusDomains


@pytest.fixture
def get_e2e_params(request):
    e2e_env = request.config.getoption("e2e_env")
    yield {
        "e2e_env": e2e_env,
    }


@pytest.fixture()
def domains(request: pytest.FixtureRequest, get_e2e_params) -> ChorusDomains:
    e2e_env = get_e2e_params["e2e_env"]
    match e2e_env:
        case "dev":
            return ChorusDomains(
                chorus_fe_url="https://chorusdev.cogninelabs.com/",
            )
        case "qa":
            return ChorusDomains(
                chorus_fe_url="https://chorusqa.cogninelabs.com/",
            )
        case _:
            raise ValueError(f"not configured for {e2e_env}")


def pytest_addoption(parser):
    parser.addoption("--e2e", action="store_true", default=False, help="Run end-to-end tests")
    parser.addoption("--e2e-env",action="store",default="qa",help="Environment for e2e tests")


def pytest_collection_modifyitems(config, items):
    skip_e2e = pytest.mark.skip(reason="only running e2e tests")
    e2e_run = config.getoption("--e2e")
    if e2e_run:
        for item in items:
            if "e2e" not in item.keywords:
                item.add_marker(skip_e2e)
