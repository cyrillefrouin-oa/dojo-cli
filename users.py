import click

@click.command()
def list():
    click.echo('users.list')

@click.command()
def search():
    click.echo('users.search')

@click.command()
def get():
    click.echo('users.get')

@click.command()
def add():
    click.echo('users.add')

@click.command()
def update():
    click.echo('users.update')

@click.command()
def delete():
    click.echo('users.delete')

def init_commands(cli):
    @cli.group()
    def users():
        pass

    users.add_command(list)
    users.add_command(search)
    users.add_command(get)
    users.add_command(add)
    users.add_command(update)
    users.add_command(delete)
