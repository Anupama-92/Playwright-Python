import os
import platform
import subprocess

import pytest

from tests.dataclass import ChorusDomains


@pytest.fixture(scope="session")
def get_e2e_params(request):
    e2e_env = request.config.getoption("e2e_env")
    yield {
        "e2e_env": e2e_env,
    }


@pytest.fixture(scope="session")
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


# Allure Report
def get_playwright_version() -> str:
    try:
        result = subprocess.run(["playwright", "--version"], capture_output=True, text=True)
        return result.stdout.strip().split()[-1]
    except Exception:
        return "Unknown"


def infer_env_from_url(url: str) -> str:
    if "qa" in url:
        return "QA"
    elif "staging" in url:
        return "STAGING"
    elif "prod" in url or "production" in url:
        return "PRODUCTION"
    elif "localhost" in url:
        return "LOCAL"
    else:
        return "UNKNOWN"


@pytest.fixture(scope="session", autouse=True)
def generate_allure_environment(domains: ChorusDomains):
    results_dir = os.path.abspath("allure-results")
    os.makedirs(results_dir, exist_ok=True)

    chorus_fe_url = domains.chorus_fe_url
    environment = infer_env_from_url(chorus_fe_url)
    platform_info = f"{platform.system()} {platform.release()}"
    playwright_version = get_playwright_version()

    env_file_path = os.path.join(results_dir, "environment.properties")
    with open(env_file_path, "w") as f:
        f.write(f"Environment={environment}\n")
        f.write(f"Frontend.URL={chorus_fe_url}\n")
        f.write("Browser=Chrome\n")  # You can update this if reading browser from config
        f.write(f"Platform={platform_info}\n")
        f.write(f"Playwright Version={playwright_version}\n")
