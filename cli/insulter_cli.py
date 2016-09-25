import click
from insulter import Insulter, FileBasedInsulter


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('insult_filename', click.Path(exists=True), required=False)
def cli(insult_filename):
    "Prints an insult to the console"

    if insult_filename:
        insulter = FileBasedInsulter(insult_filename)
    else:
        insulter = Insulter()

    click.echo(insulter.random_insult())

