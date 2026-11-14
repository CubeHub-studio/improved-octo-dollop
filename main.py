"""EPA entrypoint for TRIAD Snack Stack Studio.

Cubes Archive expects main.py at the archive root. The Tkinter interface
lives in app.py so the UI can remain organized separately.
"""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("app.py")), run_name="__main__")
