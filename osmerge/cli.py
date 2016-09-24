import logging

import click


log = logging.getLogger(__name__)


@click.group()
def main():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('yorm').setLevel(logging.WARNING)


@main.command()
def new():
    # TODO: this logic is only temporary to test the Config model
    from .models import Config
    Config.generate_example()


if __name__ == '__main__':
    main()
