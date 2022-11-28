import click

@click.command()
def list():
    click.echo('todos.list')

@click.command()
def search():
    click.echo('todos.search')

@click.command()
def get():
    click.echo('todos.get')

@click.command()
def add():
    click.echo('todos.add')

@click.command()
def update():
    click.echo('todos.update')

@click.command()
def delete():
    click.echo('todos.delete')

def init_commands(cli):
    @cli.group()
    def todos():
        pass

    todos.add_command(list)
    todos.add_command(search)
    todos.add_command(get)
    todos.add_command(add)
    todos.add_command(update)
    todos.add_command(delete)
