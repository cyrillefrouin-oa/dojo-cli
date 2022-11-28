import click
import json
import logging
import requests
from authentication import get_token

logger = logging.getLogger(__name__)

@click.command()
def list():
    # List all products
    result = requests.get('https://dummyjson.com/products')
    products = result.json()["products"]
    print(json.dumps(products, indent=4))


@click.command()
@click.argument('search_term')
def search(search_term):
    # List products with a search term
    result = requests.get(
        'https://dummyjson.com/products?q=' + search_term
    )
    products = result.json()["products"]
    print(json.dumps(products, indent=4))


@click.command()
@click.argument('id')
def get(id):
    # Get a single product
    result = requests.get(
        'https://dummyjson.com/products/' + id
    )
    product = result.json()
    print(json.dumps(product, indent=4))

@click.command()
@click.argument('name')
@click.argument('description')
@click.argument('price')
def add(name, description, price):
    # Create a new product
    token = get_token()
    result = requests.post(
        'https://dummyjson.com/products/add',
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
        },
        json={
            'name': name,
            'description': description,
            'price': price,
        },
    )
    if (result.status_code != 200):
        raise Exception(result.json()["message"])
    product = result.json()
    print(json.dumps(product, indent=4))

@click.command()
def update():
    # Update a product
    click.echo('products.update')

@click.command()
def delete():
    # Delete a product
    click.echo('products.delete')

def init_commands(cli):
    # Initialize the products commands
    @cli.group()
    def products():
        pass

    products.add_command(list)
    products.add_command(search)
    products.add_command(get)
    products.add_command(add)
    products.add_command(update)
    products.add_command(delete)
