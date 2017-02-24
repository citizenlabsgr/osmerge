#!/usr/bin/env python

import os
import logging
from pathlib import Path

import click

from . import VERSION
from .models import Project, Config, Data


log = logging.getLogger(__name__)


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(message=VERSION)
def main():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('yorm').setLevel(logging.WARNING)


@main.command()
@click.option('-r', '--root', type=Path, default=Path.cwd)
def new(root):
    _enter(root)
    Project.generate()
    Config.generate_example()
    Data.generate_example()


def _enter(path):
    """Create and enter the root directory."""
    path.mkdir(parents=True, exist_ok=True)
    os.chdir(str(path))


if __name__ == '__main__':
    main()
