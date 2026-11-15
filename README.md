# TRIAD — Snack Stack Studio

A graphical three-layer snack-stack playground built with **Python + Tkinter**.

## What you can do

- Build a stack by choosing its TOP, MIDDLE, and BASE layers.
- Preview your stack in a custom-drawn visual stack illustration.
- Pick from 82 Pringles-inspired flavours, each with its own colour and flavour profile.
- Generate a surprise combination or restore the signature stack.
- See a playful flavour/crunch score.
- Save your creation as a plain-text recipe.
- Search flavours instantly in both the stack builder and the scrollable catalogue.
- Browse the full flavour catalogue, including regional, limited-edition, collaboration, and historical entries.

## Requirements

- Python 3.10+
- Tkinter (included with most standard Windows Python installations)
- Cubes Archive runtime
- No third-party Python packages

The EPA archive contains the complete app. The Python installation used to run it must include Tkinter; the archive does not bundle a Python interpreter.

## Build an EPA

Install Cubes Archive from the [CubesEPA repository](https://github.com/CubeHub-studio/CubesEPA), clone this repository, and run these commands from its root:

```powershell
py -m py_compile main.py app.py
cubes create . -o "$HOME\TRIAD.epa" --name "TRIAD - Snack Stack Studio" --publisher "Cubes, Studio." --app-version 2.1.0 --description "A graphical three-layer snack stack builder made with Tkinter." --allowsuperfullscreen
cubes verify "$HOME\TRIAD.epa"
cubes run "$HOME\TRIAD.epa"
```

## Notes

TRIAD runs locally. It does not need an account, network access, or extra packages. Press F11 to toggle fullscreen in EPA builds created with `--allowsuperfullscreen`.

The flavour catalogue combines official Pringles product listings with regional and historical entries recorded by an unofficial fan archive. Availability varies by country and date; some entries are discontinued, limited-edition, or collaboration flavours. Its visual elements are drawn with Tkinter Canvas, so there are no external image assets to install.

EPA files contain executable Python code and run with the permissions of the current user. Only run archives from sources you trust.

## License

MIT. See [LICENSE](LICENSE).
