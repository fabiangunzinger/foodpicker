import csv
from collections import defaultdict
from datetime import date
from pathlib import Path
import random


def select_custom_from_dict(grouped_foods, n_per_group):
    return {
        group: random.sample(items, min(n_per_group.get(group, 0), len(items)))
        for group, items in grouped_foods.items()
        if n_per_group.get(group, 0) > 0
    }

def load_foods_from_csv(filepath):
    grouped = defaultdict(list)
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            grouped[row["group"]].append(row["food"])
    return grouped

def export_selection_to_shopping_list_csv(selection, output_dir="shopping_lists"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    iso_year, iso_week, _ = date.today().isocalendar()
    filename = Path(output_dir) / f"weekly_food_{iso_year}w{iso_week:02}.csv"

    if filename.exists():
        print(f"🟡 File already exists: {filename}. Skipping generation.")
        return None

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for group, foods in selection.items():
            writer.writerow([f"**{group}**"])
            for food in foods:
                writer.writerow([food])
            writer.writerow([])  # blank line between groups

    print(f"✅ New weekly food list written to: {filename}")
    return filename
