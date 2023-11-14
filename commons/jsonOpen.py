import json
from pathlib import Path


def open_schema(name: str):
    """
    Abre y carga un archivo json 

    Args:
        name (str): El nombre del archivo que contiene el esquema.

    Returns:
        dict: El esquema json cargado.
    """
    schema_path = Path(__file__).resolve().parent.parent / 'tests' / 'schema' / f'{name}_schema.json'
    with open(schema_path) as f:
        schema = json.load(f)
    return schema
