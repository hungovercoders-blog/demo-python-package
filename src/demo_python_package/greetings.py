import typer
from typing_extensions import Annotated


def greet(
    name: Annotated[str, typer.Option(help="The name of the person to greet")] = "",
):
    greeting = f"Hello {name}!"
    print(greeting)
