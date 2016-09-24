# pylint: disable=unused-variable,expression-not-assigned

from expecter import expect
from click.testing import CliRunner

from osmerge.cli import main


def describe_cli():

    def it_can_be_called_without_a_command():
        runner = CliRunner()

        result = runner.invoke(main)

        expect(result.exit_code) == 0
