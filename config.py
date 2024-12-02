from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SPECIFICATIONS: dict = {
        "vc-data-model-2.0": "https://www.w3.org/TR/vc-data-model-2.0/",
        "vc-bitstring-status-list": "https://www.w3.org/TR/vc-bitstring-status-list/",
        "vc-data-integrity": "https://www.w3.org/TR/vc-data-integrity/",
        "vc-di-ecdsa": "https://www.w3.org/TR/vc-di-ecdsa/",
        "vc-di-eddsa": "https://www.w3.org/TR/vc-di-eddsa/",
        "vc-di-bbs": "https://www.w3.org/TR/vc-di-bbs/",
    }
    TEST_SUITES: dict = {
        "vc-data-model-2.0-test-suite": "https://w3c.github.io/vc-data-model-2.0-test-suite/",
        "vc-di-eddsa-test-suite": "https://w3c.github.io/vc-di-eddsa-test-suite/",
        "vc-di-ecdsa-test-suite": "https://w3c.github.io/vc-di-ecdsa-test-suite/",
        "vc-bitstring-status-list-test-suite": "https://w3c.github.io/vc-bitstring-status-list-test-suite/",
        "vc-di-bbs-test-suite": "https://w3c.github.io/vc-di-bbs-test-suite/",
    }
    SUITE_TO_SPEC_MAPPINGS: dict = {
        "vc-data-model-2.0-test-suite": ["vc-data-model-2.0"],
        "vc-bitstring-status-list-test-suite": ["vc-bitstring-status-list"],
        # "vc-di-ecdsa-test-suite": ["vc-di-ecdsa"],
        "vc-di-eddsa-test-suite": ["vc-di-eddsa"],
        # "vc-di-bbs-test-suite": ["vc-di-bbs"],
    }


settings = Settings()
