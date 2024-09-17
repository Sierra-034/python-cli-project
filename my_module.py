import click

@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.argument('name')
def hello(count, name):
    for _ in range(count):
        click.echo(f'Hello {name}!')
