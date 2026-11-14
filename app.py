from __future__ import annotations

import random
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path

APP_NAME = "TRIAD"
VERSION = "2.0.0"

BG = "#10121b"
PANEL = "#191d2b"
PANEL_2 = "#22283a"
EDGE = "#30384d"
TEXT = "#f3f1ff"
MUTED = "#a5abc0"
PINK = "#ff83b7"
YELLOW = "#ffd36e"
BLUE = "#79c9ff"
GREEN = "#8fe0bd"
PURPLE = "#b7a0ff"

INGREDIENTS = [
    {"name": "Cheddar", "taste": "Savory", "crunch": 2, "note": "Bold, cheesy, dependable", "color": "#f5a623", "emoji": "🧀"},
    {"name": "BBQ Wavy", "taste": "Smoky", "crunch": 5, "note": "Smoky waves, serious crunch", "color": "#c47b45", "emoji": "〰"},
    {"name": "Sour Cream & Onion", "taste": "Creamy", "crunch": 3, "note": "Cool, tangy, classic", "color": "#a8c88a", "emoji": "✿"},
    {"name": "Cool Ranch", "taste": "Tangy", "crunch": 4, "note": "Zesty with a satisfying snap", "color": "#75b7d9", "emoji": "✦"},
    {"name": "Salt & Vinegar", "taste": "Sharp", "crunch": 4, "note": "A punchy, tangy layer", "color": "#c9d4dc", "emoji": "◈"},
    {"name": "Nacho Cheese", "taste": "Savory", "crunch": 3, "note": "Extra cheesy energy", "color": "#e7a93b", "emoji": "★"},
    {"name": "Jalapeño", "taste": "Spicy", "crunch": 3, "note": "A lively little kick", "color": "#72bd79", "emoji": "✧"},
    {"name": "Honey Mustard", "taste": "Sweet", "crunch": 2, "note": "Sweet with a mustard twist", "color": "#e6c35e", "emoji": "☼"},
    {"name": "Sea Salt", "taste": "Salty", "crunch": 4, "note": "Simple, crisp, reliable", "color": "#d2d6df", "emoji": "◇"},
    {"name": "Pickle", "taste": "Sharp", "crunch": 3, "note": "Bright, briny, unexpected", "color": "#8ab66b", "emoji": "❋"},
    {"name": "Sweet Chili", "taste": "Sweet", "crunch": 4, "note": "Sweet heat in every bite", "color": "#df806b", "emoji": "✹"},
    {"name": "Original", "taste": "Savory", "crunch": 3, "note": "The timeless classic", "color": "#d6b78a", "emoji": "○"},
    {"name": "Pizza", "taste": "Savory", "crunch": 3, "note": "A tiny pizza adventure", "color": "#d97c66", "emoji": "✦"},
    {"name": "Dill", "taste": "Tangy", "crunch": 2, "note": "Fresh, herby, bright", "color": "#83bd91", "emoji": "❀"},
    {"name": "Maple", "taste": "Sweet", "crunch": 2, "note": "A curious sweet finish", "color": "#c58a55", "emoji": "✧"},
]
NAMES = [item["name"] for item in INGREDIENTS]
SIGNATURE = ["Cheddar", "BBQ Wavy", "Sour Cream & Onion"]
LAYERS = [("TOP", PINK), ("MIDDLE", YELLOW), ("BASE", BLUE)]


def item_for(name: str) -> dict:
    return next(item for item in INGREDIENTS if item["name"] == name)


def score_stack(stack: list[str]) -> tuple[int, str, str]:
    tastes = len({item_for(name)["taste"] for name in stack})
    crunch = sum(item_for(name)["crunch"] for name in stack)
    score = min(100, 38 + tastes * 12 + crunch * 2)
    if tastes == 3:
        flavour = "Three distinct flavour profiles"
    elif tastes == 2:
        flavour = "A complementary flavour pairing"
    else:
        flavour = "A focused flavour theme"
    crunch_label = "MAXIMUM CRUNCH" if crunch >= 12 else "CRUNCH BALANCED" if crunch >= 8 else "SOFT & SUBTLE"
    return score, flavour, crunch_label


class TriadApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(f"{APP_NAME} — Snack Stack Studio")
        self.root.geometry("1120x780")
        self.root.minsize(900, 650)
        self.root.configure(bg=BG)
        self.stack = SIGNATURE.copy()
        self.active_layer = 0
        self.page = "studio"
        self._setup_style()
        self._build_shell()
        self.render()

    def _setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Triad.TCombobox", fieldbackground=PANEL_2, background=PANEL_2,
                        foreground=TEXT, arrowcolor=TEXT, bordercolor=EDGE, lightcolor=EDGE,
                        darkcolor=EDGE, padding=9)
        style.map("Triad.TCombobox", fieldbackground=[("readonly", PANEL_2)],
                  foreground=[("readonly", TEXT)], selectbackground=[("readonly", PANEL_2)],
                  selectforeground=[("readonly", TEXT)])

    def _build_shell(self):
        self.shell = tk.Frame(self.root, bg=BG)
        self.shell.pack(fill="both", expand=True, padx=24, pady=20)
        self.header = tk.Frame(self.shell, bg=BG)
        self.header.pack(fill="x")
        logo = tk.Canvas(self.header, width=48, height=48, bg=BG, highlightthickness=0)
        logo.pack(side="left")
        logo.create_oval(5, 5, 43, 43, fill="#302849", outline=PURPLE, width=2)
        logo.create_text(24, 24, text="3", fill=TEXT, font=("Segoe UI", 20, "bold"))
        brand = tk.Frame(self.header, bg=BG)
        brand.pack(side="left", padx=(10, 0))
        tk.Label(brand, text="TRIAD", bg=BG, fg=TEXT, font=("Segoe UI", 19, "bold")).pack(anchor="w")
        tk.Label(brand, text="SNACK STACK STUDIO", bg=BG, fg=MUTED,
                 font=("Segoe UI", 8, "bold")).pack(anchor="w")
        self.version_label = tk.Label(self.header, text=f"DESKTOP EDITION  •  v{VERSION}",
                                      bg=BG, fg=MUTED, font=("Segoe UI", 8, "bold"))
        self.version_label.pack(side="right", pady=14)

        self.nav = tk.Frame(self.shell, bg=BG)
        self.nav.pack(fill="x", pady=(22, 16))
        self.nav_buttons = {}
        for key, label in [("studio", "✦  STACK STUDIO"), ("catalogue", "▦  INGREDIENTS")]:
            btn = tk.Button(self.nav, text=label, command=lambda k=key: self.set_page(k),
                            bg=PANEL_2 if key == "studio" else BG, fg=TEXT if key == "studio" else MUTED,
                            activebackground=PANEL_2, activeforeground=TEXT, relief="flat",
                            bd=0, padx=16, pady=10, font=("Segoe UI", 9, "bold"), cursor="hand2")
            btn.pack(side="left", padx=(0, 8))
            self.nav_buttons[key] = btn

        self.content = tk.Frame(self.shell, bg=BG)
        self.content.pack(fill="both", expand=True)
        self.footer = tk.Frame(self.shell, bg=BG)
        self.footer.pack(fill="x", pady=(12, 0))
        tk.Label(self.footer, text="MADE FOR EXPERIMENTS, SILLY DISCOVERIES & MAXIMUM CRUNCH",
                 bg=BG, fg="#727a93", font=("Segoe UI", 8, "bold")).pack(side="left")
        tk.Label(self.footer, text="OFFLINE • NO ACCOUNTS • NO EXTRA PACKAGES",
                 bg=BG, fg="#727a93", font=("Segoe UI", 8, "bold")).pack(side="right")

    def set_page(self, page: str):
        self.page = page
        self.render()

    def _clear_content(self):
        for child in self.content.winfo_children():
            child.destroy()

    def _card(self, parent, padx=18, pady=16):
        frame = tk.Frame(parent, bg=PANEL, highlightbackground=EDGE, highlightthickness=1)
        frame.pack_propagate(False)
        return frame

    def _label(self, parent, text, color=TEXT, size=10, weight="normal", **kwargs):
        return tk.Label(parent, text=text, bg=kwargs.pop("bg", PANEL), fg=color,
                        font=("Segoe UI", size, weight), **kwargs)

    def _button(self, parent, text, command, primary=False, color=None):
        bg = color or (PURPLE if primary else PANEL_2)
        fg = "#171321" if primary or color else TEXT
        return tk.Button(parent, text=text, command=command, bg=bg, fg=fg,
                         activebackground=bg, activeforeground=fg, relief="flat",
                         bd=0, padx=14, pady=10, font=("Segoe UI", 9, "bold"),
                         cursor="hand2", highlightthickness=0)

    def render(self):
        self._clear_content()
        for key, btn in self.nav_buttons.items():
            selected = key == self.page
            btn.configure(bg=PANEL_2 if selected else BG, fg=TEXT if selected else MUTED)
        if self.page == "catalogue":
            self._render_catalogue()
        else:
            self._render_studio()

    def _render_studio(self):
        title_row = tk.Frame(self.content, bg=BG)
        title_row.pack(fill="x", pady=(0, 14))
        tk.Label(title_row, text="Build your next legendary stack.", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(anchor="w")
        tk.Label(title_row, text="Pick three layers. Mix it up. Give your taste buds a plot twist.",
                 bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 0))

        body = tk.Frame(self.content, bg=BG)
        body.pack(fill="both", expand=True)
        left = tk.Frame(body, bg=BG)
        left.pack(side="left", fill="both", expand=True, padx=(0, 14))
        right = tk.Frame(body, bg=PANEL, highlightbackground=EDGE, highlightthickness=1, width=340)
        right.pack(side="right", fill="y")
        right.pack_propagate(False)

        picker = tk.Frame(left, bg=PANEL, highlightbackground=EDGE, highlightthickness=1)
        picker.pack(fill="both", expand=True)
        tk.Label(picker, text="LAYER SELECTOR", bg=PANEL, fg=PURPLE,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(17, 4))
        tk.Label(picker, text="Choose a layer to customize", bg=PANEL, fg=TEXT,
                 font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=18)

        layer_row = tk.Frame(picker, bg=PANEL)
        layer_row.pack(fill="x", padx=14, pady=(16, 10))
        self.layer_buttons = []
        for index, (name, accent) in enumerate(LAYERS):
            box = tk.Frame(layer_row, bg=PANEL_2, highlightbackground=accent if index == self.active_layer else EDGE,
                           highlightthickness=2 if index == self.active_layer else 1)
            box.pack(side="left", fill="x", expand=True, padx=4)
            b = tk.Button(box, text=f"{index + 1:02d}  {name}", command=lambda i=index: self.select_layer(i),
                          bg=PANEL_2, fg=accent, activebackground=PANEL_2, activeforeground=accent,
                          relief="flat", bd=0, pady=12, font=("Segoe UI", 9, "bold"), cursor="hand2")
            b.pack(fill="x")
            self.layer_buttons.append(box)

        current = self.stack[self.active_layer]
        info = item_for(current)
        detail = tk.Frame(picker, bg=PANEL_2)
        detail.pack(fill="x", padx=18, pady=(4, 12))
        tk.Label(detail, text=f"CURRENT {LAYERS[self.active_layer][0]} LAYER",
                 bg=PANEL_2, fg=LAYERS[self.active_layer][1],
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=14, pady=(12, 3))
        tk.Label(detail, text=current, bg=PANEL_2, fg=TEXT,
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=14)
        tk.Label(detail, text=info["note"], bg=PANEL_2, fg=MUTED,
                 font=("Segoe UI", 9)).pack(anchor="w", padx=14, pady=(2, 12))

        tk.Label(picker, text="INGREDIENTS", bg=PANEL, fg=MUTED,
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=18, pady=(3, 7))
        grid = tk.Frame(picker, bg=PANEL)
        grid.pack(fill="both", expand=True, padx=14, pady=(0, 14))
        for i, item in enumerate(INGREDIENTS):
            row, col = divmod(i, 3)
            selected = item["name"] == current
            b = tk.Button(grid, text=f'{item["emoji"]}  {item["name"]}',
                          command=lambda name=item["name"]: self.choose_ingredient(name),
                          bg="#34304a" if selected else PANEL_2,
                          fg=TEXT if selected else "#d5d7e4",
                          activebackground="#34304a", activeforeground=TEXT,
                          relief="flat", bd=0, padx=8, pady=9,
                          font=("Segoe UI", 8, "bold"), cursor="hand2")
            b.grid(row=row, column=col, sticky="ew", padx=4, pady=4)
        for col in range(3):
            grid.grid_columnconfigure(col, weight=1)

        tk.Label(right, text="STACK PREVIEW", bg=PANEL, fg=PURPLE,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(17, 4))
        tk.Label(right, text="Your three-layer creation", bg=PANEL, fg=MUTED,
                 font=("Segoe UI", 9)).pack(anchor="w", padx=18)
        self.preview = tk.Canvas(right, width=300, height=260, bg=PANEL, highlightthickness=0)
        self.preview.pack(fill="x", padx=16, pady=(8, 0))
        self._draw_stack()
        score, flavour, crunch = score_stack(self.stack)
        metrics = tk.Frame(right, bg=PANEL_2)
        metrics.pack(fill="x", padx=16, pady=(4, 12))
        tk.Label(metrics, text="STACK SCORE", bg=PANEL_2, fg=MUTED,
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=12, pady=(10, 0))
        tk.Label(metrics, text=f"{score} / 100", bg=PANEL_2, fg=YELLOW,
                 font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=12)
        tk.Label(metrics, text=flavour, bg=PANEL_2, fg=TEXT,
                 font=("Segoe UI", 8)).pack(anchor="w", padx=12, pady=(1, 0))
        tk.Label(metrics, text=crunch, bg=PANEL_2, fg=GREEN,
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=12, pady=(4, 10))
        actions = tk.Frame(right, bg=PANEL)
        actions.pack(fill="x", padx=16, pady=(0, 16))
        self._button(actions, "✦  Surprise me", self.randomize, primary=True).pack(fill="x", pady=(0, 7))
        row = tk.Frame(actions, bg=PANEL)
        row.pack(fill="x")
        self._button(row, "Signature", self.signature).pack(side="left", fill="x", expand=True, padx=(0, 4))
        self._button(row, "Save .txt", self.save_stack).pack(side="left", fill="x", expand=True, padx=(4, 0))

    def _draw_stack(self):
        c = self.preview
        c.delete("all")
        c.create_oval(28, 215, 272, 249, fill="#0d0f17", outline="")
        widths = [205, 225, 245]
        for i, (layer, accent) in enumerate(LAYERS):
            y = 25 + i * 65
            name = self.stack[i]
            data = item_for(name)
            w = widths[i]
            x1, x2 = 150 - w // 2, 150 + w // 2
            c.create_rectangle(x1, y + 15, x2, y + 48, fill=data["color"], outline="")
            c.create_oval(x1, y, x2, y + 30, fill=data["color"], outline="#ffffff", width=1)
            c.create_arc(x1, y + 10, x2, y + 48, start=180, extent=180,
                         style="arc", outline="#ffffff", width=1)
            c.create_text(150, y + 17, text=name, fill="#241b18",
                          font=("Segoe UI", 9, "bold"))
            c.create_text(150, y + 55, text=layer, fill=accent,
                          font=("Segoe UI", 8, "bold"))

    def select_layer(self, index: int):
        self.active_layer = index
        self.render()

    def choose_ingredient(self, name: str):
        self.stack[self.active_layer] = name
        self.render()

    def randomize(self):
        self.stack = random.sample(NAMES, 3)
        self.active_layer = 0
        self.render()

    def signature(self):
        self.stack = SIGNATURE.copy()
        self.active_layer = 0
        self.render()

    def save_stack(self):
        score, flavour, crunch = score_stack(self.stack)
        content = (
            "TRIAD — SNACK STACK STUDIO\n"
            "==========================\n\n"
            f"TOP:    {self.stack[0]}\n"
            f"MIDDLE: {self.stack[1]}\n"
            f"BASE:   {self.stack[2]}\n\n"
            f"STACK SCORE: {score}/100\n{flavour}\n{crunch}\n"
        )
        path = filedialog.asksaveasfilename(
            title="Save your TRIAD stack", defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if path:
            Path(path).write_text(content, encoding="utf-8")
            messagebox.showinfo("Stack saved", "Your stack recipe has been saved.")

    def _render_catalogue(self):
        tk.Label(self.content, text="The ingredient catalogue", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(anchor="w")
        tk.Label(self.content, text="Fifteen flavours. Endless questionable combinations.",
                 bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 16))
        outer = tk.Frame(self.content, bg=BG)
        outer.pack(fill="both", expand=True)
        for i, item in enumerate(INGREDIENTS):
            row, col = divmod(i, 3)
            card = tk.Frame(outer, bg=PANEL, highlightbackground=EDGE, highlightthickness=1)
            card.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            icon = tk.Canvas(card, width=42, height=42, bg=PANEL, highlightthickness=0)
            icon.pack(side="left", padx=(12, 5), pady=9)
            icon.create_oval(3, 3, 39, 39, fill=item["color"], outline="")
            icon.create_text(21, 21, text=item["emoji"], fill="#211d24",
                             font=("Segoe UI", 13, "bold"))
            details = tk.Frame(card, bg=PANEL)
            details.pack(side="left", fill="both", expand=True, pady=9)
            tk.Label(details, text=item["name"], bg=PANEL, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w")
            tk.Label(details, text=f'{item["taste"]}  •  Crunch {item["crunch"]}/5',
                     bg=PANEL, fg=MUTED, font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(details, text=item["note"], bg=PANEL, fg="#8d94aa",
                     font=("Segoe UI", 8)).pack(anchor="w")
            self._button(card, "USE", lambda name=item["name"]: self.use_from_catalogue(name),
                         color=item["color"]).pack(side="right", padx=10)
            outer.grid_columnconfigure(col, weight=1, uniform="catalogue")
        for row in range(5):
            outer.grid_rowconfigure(row, weight=1)

    def use_from_catalogue(self, name: str):
        self.stack[self.active_layer] = name
        self.page = "studio"
        self.render()


def main():
    root = tk.Tk()
    TriadApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
