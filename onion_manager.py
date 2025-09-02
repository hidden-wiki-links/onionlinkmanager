import requests
import click
import yaml

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

@click.group()
def cli():
    pass

@cli.command()
@click.argument("url")
def validate(url):
    # Add .onion validation logic
    print(f"Validating {url}")

if __name__ == "__main__":
    cli()
