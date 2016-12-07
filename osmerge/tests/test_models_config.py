# pylint: disable=unused-variable,expression-not-assigned

import pytest
from expecter import expect

from osmerge.models import Config


def describe_config():

    @pytest.fixture(autouse=True)
    def temporary_directory(tmpdir):
        tmpdir.chdir()

    def describe_generate_example():

        def it_includes_boundaries_and_filters():
            config = Config.generate_example()

            expect(len(config.boundaries)) == 1
            expect(len(config.filters.tags)) == 1
