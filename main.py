from logging import NOTSET
import os
from dotenv import load_dotenv
import click
from sty import bg, ef, fg, rs

load_dotenv("config.ini")

@click.command()
@click.argument('version', type=click.INT, nargs=1, metavar='<version>', required=True)
def main(version):
    """Be sure JAVA_HOME IS SET IN PATH, AND CONFIGURE YOUR PATHS IN .ENV FILE."""
    path : str = os.getenv(f"JAVA{version}")
    if path == None:
        click.echo(f"{fg.li_red}Java home path version not found in config.ini{rs.all}")
    else:
        cambiar_version(path, version)


def cambiar_version(path:str, version : int):
    click.echo(f"Java version {fg.li_green}{version}{rs.all} activated!")
    click.echo(f"JAVA_HOME = {fg.li_green}{path}{rs.all}")

if __name__ == '__main__':
    main()