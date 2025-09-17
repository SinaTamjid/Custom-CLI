import typer
import subprocess
import os
app= typer.Typer()

@app.command()
def sayhello():
    return "hello"

def cls(output_wgt):
    output_wgt.clear()
    return ""

def vscode(exe_path: str, target_path: str = "."):
    if not exe_path or not os.path.exists(exe_path):
        return "VSCode executable Not Found."
    try:
        subprocess.Popen([exe_path], shell=True)
        return f"VSCode Launched"
    except Exception as e:
        return f"Error launching VSCode: {e}"


def git(exe_path:str, target_path:str="."):
    if not exe_path or not os.path.exists(exe_path):
        return" Git executable Not Found."
    try:
        subprocess.Popen([exe_path],shell=True)
        return f"Git Launched"
    except Exception as e:
        return f"Error Launching Git: {e}"



