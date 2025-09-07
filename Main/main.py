import typer
app= typer.Typer()

@app.command()
def sayhello_direct():
    return "hello"
