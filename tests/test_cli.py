# pylint: disable=unused-variable,expression-not-assigned,redefined-outer-name

import sys

import pytest
import scripttest
from expecter import expect


@pytest.fixture
def env(tmpdir):
    path = str(tmpdir.join("test"))
    env = scripttest.TestFileEnvironment(path)
    return env


@pytest.fixture
def cli(env):
    prog = sys.executable, '-m', 'osmerge'
    return lambda *args: env.run(*prog, *args, expect_error=True)


def describe_cli():

    def it_displays_help_information(cli):
        cmd = cli('--help')

        expect(cmd.returncode) == 0
        expect(cmd.stdout).contains("Usage: ")

    def it_displays_version_information(cli):
        cmd = cli('--version')

        expect(cmd.returncode) == 0
        expect(cmd.stdout or cmd.stderr).contains("OSMerge v0.")

    def describe_new():

        def it_generates_a_sample_project(cli):
            cmd = cli('new')

            expect(cmd.returncode) == 0
            expect(sorted(cmd.files_created.keys())) == [
                ".gitignore",  # ignore /tmp
                "docs/index.html",  # example HTML file using `osmerge.geojson`
                "docs/osmerge.geojson",  # copied from `tmp/merged.geojson`
                "osmerge.csv",  # data set
                "osmerge.yml",  # config file
                "tmp/base.json",  # downloaded OSM data
                "tmp/filtered.json",  # reduced data based on config filters
                "tmp/merged.geojson "  # above file converted to GeoJSON
                "tmp/merged.json",  # above file with added fields
            ]
