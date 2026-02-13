import matplotlib.pyplot as plt
from matplotlib.widgets import Button

ligen = ["Premier League", "La Liga", "Bundesliga", "Serie A"]

# Originalwerte
platzierung_raw = [5.67, 9.33, 11.67, 12.67]
punkte = [17.50, 14.67, 14.67, 13.67]
tordiff = [10.67, 6.33, 5.00, 4.00]

# Platzierung so transformieren, dass "höher = besser" gilt
# Idee: score = (max+1) - platzierung
max_pl = max(platzierung_raw)
platzierung_score = [(max_pl + 1) - x for x in platzierung_raw]

slides = [
    {
    "titel": "Platzierung (kleiner ist besser)",
    "y_label": "Ø Platzierung",
    "werte": platzierung_raw,
    "anzeigen": platzierung_raw,
    "format": "{:.2f}",
    "invert_y": False
},

    {
        "titel": "Punkte (höher ist besser)",
        "y_label": "Ø Punkte",
        "werte": punkte,
        "anzeigen": punkte,
        "format": "{:.2f}"
    },
    {
        "titel": "Tordifferenz (höher ist besser)",
        "y_label": "Ø Tordifferenz",
        "werte": tordiff,
        "anzeigen": tordiff,
        "format": "{:.2f}"
    }
]

index = 0

fig, ax = plt.subplots(figsize=(10, 6))

# Mehr Platz unten für Buttons + Labels
plt.subplots_adjust(bottom=0.30)

def zeichne(i):
    ax.clear()
    item = slides[i]

    bars = ax.bar(ligen, item["werte"])
    ax.set_title(f"Vergleich der Ligen: {item['titel']}", pad=12)
    ax.set_xlabel("Liga")
    ax.set_ylabel(item["y_label"])

    # Labels besser lesbar
    ax.tick_params(axis="x", rotation=20)

    # Werte über Balken: Bei Platzierung zeigen wir die echten Platzierungswerte
    for bar, v in zip(bars, item["anzeigen"]):
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            h,
            item["format"].format(v),
            ha="center",
            va="bottom"
        )

    # Extra Luft oben, damit Zahlen nicht am Rand kleben
    ax.margins(y=0.15)

    fig.canvas.draw_idle()

def next_slide(event):
    global index
    index = (index + 1) % len(slides)
    zeichne(index)

def prev_slide(event):
    global index
    index = (index - 1) % len(slides)
    zeichne(index)

# Buttons deutlich tiefer platzieren
ax_prev = plt.axes([0.25, 0.07, 0.20, 0.10])
ax_next = plt.axes([0.55, 0.07, 0.20, 0.10])

btn_prev = Button(ax_prev, "Zurück")
btn_next = Button(ax_next, "Weiter")
btn_prev.on_clicked(prev_slide)
btn_next.on_clicked(next_slide)

zeichne(index)
plt.show()
