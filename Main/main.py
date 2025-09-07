import typer
app= typer.Typer()

@app.command()
def sayhello():
    return "hello"

def cls(output_wgt):
    output_wgt.clear()
    return ""


    


