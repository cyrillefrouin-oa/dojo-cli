import click
from click_loglevel import LogLevel
from colorama import just_fix_windows_console
import logging
import requests

from authentication import init_token, get_token
from products import init_commands as init_products_commands
from todos import init_commands as init_todos_commands
from users import init_commands as init_users_commands

logger = logging.getLogger()

# Fix windows console
just_fix_windows_console()

@click.group()
@click.option("-l", "--log-level", type=LogLevel(), default=logging.INFO)
def cli(log_level):
    logging.basicConfig(
        format="[%(levelname)-8s] %(message)s",
        level=log_level,
    )
    init_token()
    pass

init_products_commands(cli)
init_todos_commands(cli)
init_users_commands(cli)

if __name__ == '__main__':
    cli()
