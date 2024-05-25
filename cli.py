import os
import click
from cookiecutter.main import cookiecutter

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates')

@click.command()
@click.option('--prefix', prompt='Prefix', help='Prefix for the project.')
@click.option('--project_name', prompt='Project Name', help='Name of the project.')
@click.option('--module_name', prompt='Module Name', help='Name of the main module.')
def generate(prefix, project_name, module_name):
    """Generates a folder structure using Cookiecutter."""
    cookiecutter(TEMPLATE_PATH, extra_context={
        'prefix': prefix,
        'project_name': project_name,
        'module_name': module_name
    })

if __name__ == '__main__':
    generate()
