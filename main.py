from __future__ import annotations

import os
import random
import sys
import textwrap

APP_NAME = "TRIAD"
VERSION = "1.0.0"

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
COLORS = {
    "pink": "\033[38;5;213m",
    "orange": "\033[38;5;208m",
    "yellow": "\033[38;5;220m",
    "green": "\033[38;5;120m",
    "blue": "\033[38;5;117m",
    "purple": "\033[38;5;183m",
    "white": "\033[97m",
}

INGREDIENTS = [
    {"name": "Cheddar", "taste": "savory", "crunch": 2, "note": "bold, cheesy, and dependable"},
    {"name": "BBQ Wavy", "taste": "smoky", "crunch": 5, "note": "smoky waves with serious crunch"},
    {"name": "Sour Cream & Onion", "taste": "creamy", "crunch": 3, "note": "cool, tangy, and classic"},
    {"name": "Cool Ranch", "taste": "tangy", "crunch": 4, "note": "zesty with a satisfying snap"},
    {"name": "Salt & Vinegar", "taste": "sharp", "crunch": 4, "note": "a punchy, tangy layer"},
    {"name": "Nacho Cheese", "taste": "savory", "crunch": 3, "note": "extra cheesy energy"},
    {"name": "Jalapeño", "taste": "spicy", "crunch": 3, "note": "a lively little kick"},
    {"name": "Honey Mustard", "taste": "sweet", "crunch": 2, "note": "sweet with a mustard twist"},
    {"name": "Sea Salt", "taste": "salty", "crunch": 4, "note": "simple, crisp, and reliable"},
    {"name": "Pickle", "taste": "sharp", "crunch": 3, "note": "bright, briny, and unexpected"},
    {"name": "Sweet Chili", "taste": "sweet", "crunch": 4, "note": "sweet heat in every bite"},
    {"name": "Original", "taste": "savory", "crunch": 3, "note": "the timeless classic"},
    {"name": "Pizza", "taste": "savory", "crunch": 3, "note": "a tiny pizza-flavoured adventure"},
    {"name": "Dill", "taste": "tangy", "crunch": 2, "note": "fresh, herby, and bright"},
    {"name": "Maple", "taste": "sweet", "crunch": 2, "note": "a curious sweet finish"},
]

LAYER_NAMES = ["TOP", "MIDDLE", "BASE"]
LAYER_COLORS = ["pink", "yellow", "blue"]
SIGNATURE = ["Cheddar", "BBQ Wavy", "Sour Cream & Onion"]


def paint(text: str, color: str = "white", bold: bool = False) -> str:
    if not sys.stdout.isatty() or os.environ.get("NO_COLOR"):
        return text
    prefix = COLORS.get(color, COLORS["white"])
    return f"{BOLD if bold else ''}{prefix}{text}{RESET}"


def clear() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def line(char: str = "─", width: int = 54) -> str:
    return char * width


def header() -> None:
    print(paint("╔" + line("═") + "╗", "purple"))
    print(paint("║" + " " * 17 + "T R I A D" + " " * 28 + "║", "pink", True))
    print(paint("║" + " " * 10 + "SNACK STACK STUDIO" + " " * 26 + "║", "yellow"))
    print(paint("╚" + line("═") + "╝", "purple"))
    print(paint("  Three layers. Infinite possibilities.", "white"))


def pause() -> None:
    input("\nPress Enter to continue...")


def choose(prompt: str, options: list[str]) -> int | None:
    print()
    for index, option in enumerate(options, 1):
        print(f"  {paint(str(index), 'yellow', True)}. {option}")
    print(f"  {paint('0', 'dim')}. Back")
    while True:
        answer = input(f"\n{prompt} ").strip()
        if answer == "0":
            return None
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer) - 1
        print(paint("Please enter one of the listed numbers.", "orange"))


def ingredient(name: str) -> dict:
    return next(item for item in INGREDIENTS if item["name"] == name)


def score_stack(stack: list[str]) -> tuple[int, list[str]]:
    profiles = {ingredient(name)["taste"] for name in stack}
    crunch = sum(ingredient(name)["crunch"] for name in stack)
    variety = len(profiles)
    score = min(100, 38 + variety * 12 + crunch * 2)
    notes = []
    if variety == 3:
        notes.append("Flavor variety: all three layers bring something different.")
    elif variety == 2:
        notes.append("Flavor variety: two flavor profiles work together.")
    else:
        notes.append("Flavor variety: a focused, same-theme stack.")
    if crunch >= 12:
        notes.append("Crunch rating: maximum crunch energy.")
    elif crunch >= 8:
        notes.append("Crunch rating: nicely balanced texture.")
    else:
        notes.append("Crunch rating: a softer, calmer stack.")
    if len(set(stack)) == 3:
        notes.append("No repeats: every layer gets its own spotlight.")
    else:
        notes.append("Repeats: doubling down on a favourite is allowed.")
    return score, notes


def show_stack(stack: list[str], title: str = "YOUR STACK") -> None:
    print()
    print(paint("  " + title, "purple", True))
    print(paint("  ┌" + line("─", 36) + "┐", "purple"))
    for index, name in enumerate(stack):
        layer = LAYER_NAMES[index]
        color = LAYER_COLORS[index]
        note = ingredient(name)["note"]
        print(paint(f"  │ {layer:<7} {name:<26} │", color, True))
        print(paint(f"  │         {note:<26} │", "white"))
        if index < 2:
            print(paint("  ├" + line("·", 36) + "┤", "purple"))
    print(paint("  └" + line("─", 36) + "┘", "purple"))
    score, notes = score_stack(stack)
    print(f"\n  Stack score: {paint(str(score) + '/100', 'yellow', True)}")
    for note in notes:
        print("  • " + note)


def build_stack() -> None:
    stack = []
    for index, layer in enumerate(LAYER_NAMES):
        clear()
        header()
        print(paint(f"\n  BUILD MODE / {layer} LAYER", LAYER_COLORS[index], True))
        selected = choose(
            f"Choose your {layer.lower()} layer:",
            [item["name"] for item in INGREDIENTS],
        )
        if selected is None:
            return
        stack.append(INGREDIENTS[selected]["name"])
    clear()
    header()
    show_stack(stack, "STACK COMPLETE")
    if stack == SIGNATURE:
        print(paint("\n  ✦ THE LEGENDARY THREE-LAYER DIP STACK! ✦", "yellow", True))
    pause()


def surprise_stack() -> None:
    stack = random.sample(INGREDIENTS, 3)
    names = [item["name"] for item in stack]
    clear()
    header()
    print(paint("\n  SURPRISE GENERATOR", "pink", True))
    show_stack(names, "THE RANDOMIZED STACK")
    if names == SIGNATURE:
        print(paint("\n  THE LEGENDARY STACK HAS RETURNED.", "yellow", True))
    else:
        print(paint("\n  A one-of-a-kind combination. What a discovery.", "green"))
    pause()


def stack_lab() -> None:
    while True:
        clear()
        header()
        print(paint("\n  STACK LAB", "yellow", True))
        choice = choose("What would you like to do?", [
            "Build a stack layer by layer",
            "Surprise me with a random stack",
            "Show the legendary signature stack",
            "Browse the ingredient catalogue",
        ])
        if choice is None:
            return
        if choice == 0:
            build_stack()
        elif choice == 1:
            surprise_stack()
        elif choice == 2:
            clear()
            header()
            show_stack(SIGNATURE, "THE SIGNATURE STACK")
            print(paint("\n  Cheddar + BBQ Wavy + Sour Cream & Onion", "yellow", True))
            pause()
        elif choice == 3:
            clear()
            header()
            print(paint("\n  INGREDIENT CATALOGUE", "green", True))
            for item in INGREDIENTS:
                print(f"  • {item['name']:<22} {item['note']}")
            pause()


def about() -> None:
    clear()
    header()
    print("\n  TRIAD is a tiny creative playground for building")
    print("  imaginary three-layer snack combinations.")
    print("\n  Made for experimentation, silly discoveries,")
    print("  and the eternal question: what goes on top?")
    print(paint("\n  No accounts. No network. No extra packages.", "green"))
    print(paint("  Just Python and a suspicious amount of crunch.", "yellow"))
    pause()


def main() -> int:
    random.seed()
    while True:
        clear()
        header()
        print(paint("\n  WELCOME TO THE STACK LAB", "yellow", True))
        print("\n  Your next great combination is three layers away.")
        choice = choose("Select a destination:", [
            "Open Stack Lab",
            "Surprise me!",
            "About TRIAD",
            "Exit",
        ])
        if choice is None or choice == 3:
            print(paint("\n  Thanks for visiting TRIAD. Stay crunchy.", "pink", True))
            return 0
        if choice == 0:
            stack_lab()
        elif choice == 1:
            surprise_stack()
        elif choice == 2:
            about()


if __name__ == "__main__":
    raise SystemExit(main())
