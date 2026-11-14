# TRIAD — Snack Stack Studio

A tiny, colourful terminal playground for inventing imaginary three-layer snack stacks.

## Features

- Build a custom stack, choosing its top, middle, and base layers.
- Generate a surprise combination.
- Browse a 15-item ingredient catalogue.
- Get a playful stack score based on flavour variety and crunch.
- Discover the signature stack: Cheddar + BBQ Wavy + Sour Cream & Onion.

## Requirements

- Python 3.10+
- Cubes Archive runtime
- No third-party Python packages

## Build an EPA

Install Cubes Archive from the [CubesEPA repository](https://github.com/CubeHub-studio/CubesEPA), then run this from the root of this repository:

\`\`\`powershell
cubes create . -o TRIAD.epa --name "TRIAD - Snack Stack Studio" --publisher "Cubes, Studio." --app-version 1.0.0 --description "A playful three-layer snack stack builder and randomizer."
\`\`\`

Verify and launch:

\`\`\`powershell
cubes verify .\\TRIAD.epa
cubes run .\\TRIAD.epa
\`\`\`

## Notes

TRIAD is an offline terminal application. It does not require an account, network access, or extra packages.

EPA files contain executable Python code and run with the permissions of the current user. Only run archives from sources you trust.

## License

MIT. See [LICENSE](LICENSE).
