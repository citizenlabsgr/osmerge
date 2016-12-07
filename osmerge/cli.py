import logging

import click

from . import VERSION
from .models import Project, Config, Data


log = logging.getLogger(__name__)


@click.group()
@click.version_option(message=VERSION)
def main():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('yorm').setLevel(logging.WARNING)


@main.command()
def new():
    Project.generate()
    Config.generate_example()
    Data.generate_example()


if __name__ == '__main__':
    main()
