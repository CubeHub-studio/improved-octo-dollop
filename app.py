from __future__ import annotations

import random
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path

APP_NAME = "TRIAD"
VERSION = "2.1.0"

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

# Regional, limited-edition, collaboration, and historical flavours are included too.
for _name, _taste, _crunch, _color in [["All Dressed","Tangy",4,"#8b9f58"],["Ketchup","Tangy",3,"#cf6258"],["Buffalo Ranch","Spicy",4,"#c66f53"],["Mexican Street Corn","Savory",4,"#e2b45d"],["Chile & Lime","Sharp",4,"#8ebc68"],["Street Taco","Savory",4,"#c78b5e"],["Masala","Spicy",4,"#c58b45"],["Spicy Hot Pot","Spicy",5,"#b9574c"],["Sweet Chili Sauce","Sweet",4,"#d77a62"],["Texas BBQ Brisket","Smoky",5,"#a96b4b"],["Sharp White Cheddar","Savory",3,"#e3c879"],["Smoky Bacon","Smoky",4,"#a87561"],["Smoky Mesquite BBQ","Smoky",5,"#98664b"],["Smoky Cheddar","Savory",4,"#d59a4f"],["Lightly Salted","Salty",3,"#d7d2bf"],["Reduced Fat Original","Savory",3,"#c9b58f"],["Spicy Loaded Nacho","Spicy",4,"#d78c3d"],["Loaded Potato Skins","Savory",4,"#b98a5d"],["Seven Layer Dip","Creamy",4,"#9d9c65"],["Dippers French Onion","Creamy",5,"#a6a77b"],["Dippers Bacon Cheddar","Savory",5,"#c78c52"],["Parmesan Garlic","Savory",4,"#d9c69b"],["Medium Buffalo","Spicy",5,"#c45c49"],["Asian Zing","Sweet",4,"#c76b4f"],["Los Calientes Rojo","Spicy",5,"#b94f45"],["Los Calientes Barbacoa","Smoky",5,"#a85e45"],["Los Calientes Verde","Spicy",4,"#79a66c"],["Texas BBQ Sauce","Smoky",5,"#a96d4c"],["Cheese & Onion","Savory",3,"#d7c16d"],["Hot & Spicy","Spicy",5,"#c95d49"],["Prawn Cocktail","Tangy",3,"#d68a83"],["Hot Smokin' BBQ Ribs","Smoky",5,"#9e6046"],["Hot Sweet Chilli","Sweet",5,"#d36b4e"],["Kickin' Sour Cream","Creamy",4,"#a9bd86"],["Mexican Chilli & Lime","Sharp",5,"#8caa5e"],["Cheese & Chilli","Spicy",4,"#d89b45"],["Italian Style Pepperoni Pizza","Savory",4,"#c96d58"],["New York Style Cheeseburger","Savory",4,"#b77b50"],["Spicy Chorizo","Spicy",4,"#b85b4a"],["Pigs in Blankets","Smoky",3,"#b77e67"],["Mint Choc","Sweet",2,"#82a88a"],["Sweet Cinnamon","Sweet",2,"#c58d62"],["10-Spice Ethnic Chicken","Savory",4,"#bd965d"],["Addictive Garlic Butter","Savory",3,"#d9c18b"],["Alter Ego Salsa","Tangy",4,"#c96f59"],["American Barbecue","Smoky",5,"#a76e4d"],["Crunchy Dill","Sharp",4,"#8baa68"],["Chicken Salt","Salty",3,"#d3b77b"],["Sweet Cheddar","Sweet",3,"#d9aa58"],["Caribbean Spiced Chicken","Spicy",4,"#c78a55"],["Japanese Sticky Teriyaki","Sweet",4,"#b77a53"],["Indian Chicken Tikka Masala","Spicy",4,"#c7794d"],["Chinese Style Sweet & Sticky Wings","Sweet",4,"#c47c52"],["Bacon Mac & Cheese","Savory",4,"#d4a35c"],["Malaysian Red Curry","Spicy",5,"#bd6348"],["Pickle Rick","Sharp",4,"#83b36e"],["Seaweed","Salty",3,"#668d6b"],["Chilli Lemon Crab","Sharp",4,"#c7a45f"],["Lime & Tart","Sharp",4,"#a6bf6b"],["Cucumber Sea Salt","Salty",3,"#9ab68a"],["Thirteen-Spices Crayfish","Spicy",5,"#b96c53"],["Spicy Strips","Spicy",5,"#bc5d49"],["Cheese Burger","Savory",4,"#c28b59"],["Yakitori","Smoky",4,"#a96f50"],["Prosecco & Pink Peppercorn","Sharp",3,"#c98d9c"],["Cheesy Cheese","Savory",3,"#e0b65a"],["Smokey Paprika & Almonds","Smoky",4,"#b77b52"]]:
    if _name not in {item['name'] for item in INGREDIENTS}:
        INGREDIENTS.append({'name': _name, 'taste': _taste, 'crunch': _crunch,
                            'note': 'Regional, limited-edition, or archive flavour',
                            'color': _color, 'emoji': '✦'})

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

        tk.Label(picker, text=f"INGREDIENTS  •  {len(INGREDIENTS)} FLAVOURS",
                 bg=PANEL, fg=MUTED, font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=18, pady=(3, 6))
        search_box = tk.Frame(picker, bg=PANEL_2)
        search_box.pack(fill="x", padx=14, pady=(0, 7))
        tk.Label(search_box, text="⌕", bg=PANEL_2, fg=PURPLE,
                 font=("Segoe UI", 13, "bold")).pack(side="left", padx=(9, 3))
        self.studio_search = tk.Entry(search_box, bg=PANEL_2, fg=TEXT,
                                      insertbackground=TEXT, relief="flat", bd=0,
                                      font=("Segoe UI", 9))
        self.studio_search.pack(side="left", fill="x", expand=True, padx=(2, 9), pady=9)
        self.studio_search.bind("<KeyRelease>", self._filter_studio_list)
        list_wrap = tk.Frame(picker, bg=PANEL)
        list_wrap.pack(fill="both", expand=True, padx=14, pady=(0, 12))
        self.studio_list = tk.Listbox(list_wrap, bg=PANEL_2, fg=TEXT,
                                      selectbackground="#51436f", selectforeground=TEXT,
                                      relief="flat", bd=0, highlightthickness=0,
                                      font=("Segoe UI", 9), activestyle="none")
        list_scroll = tk.Scrollbar(list_wrap, orient="vertical", command=self.studio_list.yview)
        self.studio_list.configure(yscrollcommand=list_scroll.set)
        self.studio_list.pack(side="left", fill="both", expand=True)
        list_scroll.pack(side="right", fill="y")
        self.studio_list.bind("<<ListboxSelect>>", self._choose_from_studio_list)
        self._filter_studio_list()

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

    def _filter_studio_list(self, _event=None):
        if not hasattr(self, "studio_list"):
            return
        query = self.studio_search.get().casefold()
        self.studio_list.delete(0, "end")
        self._studio_matches = [item for item in INGREDIENTS
                                if query in item["name"].casefold()
                                or query in item["taste"].casefold()]
        for item in self._studio_matches:
            self.studio_list.insert("end", item["name"])
        current = self.stack[self.active_layer]
        for index, item in enumerate(self._studio_matches):
            if item["name"] == current:
                self.studio_list.selection_set(index)
                self.studio_list.see(index)
                break

    def _choose_from_studio_list(self, _event=None):
        if not self.studio_list.curselection():
            return
        index = self.studio_list.curselection()[0]
        if index < len(self._studio_matches):
            self.choose_ingredient(self._studio_matches[index]["name"])

    def _render_catalogue(self):
        tk.Label(self.content, text="The flavour catalogue", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(anchor="w")
        tk.Label(self.content,
                 text=f"{len(INGREDIENTS)} flavours • search by name, profile, or edition type",
                 bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 10))
        search_box = tk.Frame(self.content, bg=PANEL_2)
        search_box.pack(fill="x", pady=(0, 10))
        tk.Label(search_box, text="⌕", bg=PANEL_2, fg=PURPLE,
                 font=("Segoe UI", 15, "bold")).pack(side="left", padx=(12, 4))
        self.catalogue_search = tk.Entry(search_box, bg=PANEL_2, fg=TEXT,
                                         insertbackground=TEXT, relief="flat", bd=0,
                                         font=("Segoe UI", 10))
        self.catalogue_search.pack(side="left", fill="x", expand=True, padx=(2, 12), pady=11)
        self.catalogue_search.bind("<KeyRelease>", self._filter_catalogue)

        scroll_shell = tk.Frame(self.content, bg=BG)
        scroll_shell.pack(fill="both", expand=True)
        canvas = tk.Canvas(scroll_shell, bg=BG, highlightthickness=0, bd=0)
        scrollbar = tk.Scrollbar(scroll_shell, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        self.catalogue_grid = tk.Frame(canvas, bg=BG)
        window_id = canvas.create_window((0, 0), window=self.catalogue_grid, anchor="nw")
        self.catalogue_grid.bind("<Configure>",
                                 lambda _event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>",
                    lambda event: canvas.itemconfigure(window_id, width=event.width))
        self._populate_catalogue("")

    def _filter_catalogue(self, _event=None):
        self._populate_catalogue(self.catalogue_search.get())

    def _populate_catalogue(self, query):
        for child in self.catalogue_grid.winfo_children():
            child.destroy()
        query = query.casefold()
        matches = [item for item in INGREDIENTS
                   if query in item["name"].casefold()
                   or query in item["taste"].casefold()
                   or query in item["note"].casefold()]
        if not matches:
            tk.Label(self.catalogue_grid, text="No matching flavours found.",
                     bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(anchor="w", padx=8, pady=18)
            return
        for i, item in enumerate(matches):
            row, col = divmod(i, 3)
            card = tk.Frame(self.catalogue_grid, bg=PANEL,
                            highlightbackground=EDGE, highlightthickness=1)
            card.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            icon = tk.Canvas(card, width=38, height=38, bg=PANEL, highlightthickness=0)
            icon.pack(side="left", padx=(9, 4), pady=8)
            icon.create_oval(3, 3, 35, 35, fill=item["color"], outline="")
            icon.create_text(19, 19, text=item["emoji"], fill="#211d24",
                             font=("Segoe UI", 12, "bold"))
            details = tk.Frame(card, bg=PANEL)
            details.pack(side="left", fill="both", expand=True, pady=8)
            tk.Label(details, text=item["name"], bg=PANEL, fg=TEXT,
                     font=("Segoe UI", 8, "bold"), wraplength=145,
                     justify="left").pack(anchor="w")
            tk.Label(details, text=f'{item["taste"]}  •  Crunch {item["crunch"]}/5',
                     bg=PANEL, fg=MUTED, font=("Segoe UI", 7)).pack(anchor="w")
            tk.Label(details, text=item["note"], bg=PANEL, fg="#8d94aa",
                     font=("Segoe UI", 7), wraplength=145,
                     justify="left").pack(anchor="w")
            self._button(card, "USE", lambda name=item["name"]: self.use_from_catalogue(name),
                         color=item["color"]).pack(side="right", padx=7)
        for col in range(3):
            self.catalogue_grid.grid_columnconfigure(col, weight=1)

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
