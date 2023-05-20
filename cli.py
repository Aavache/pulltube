import click


@click.command()
def cli():
    """Basic command"""
    click.echo('Hello World!')


if __name__ == '__main__':
    cli()
