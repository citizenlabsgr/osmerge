import logging

import click


log = logging.getLogger(__name__)


@click.command()
def main():
    logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    main()
