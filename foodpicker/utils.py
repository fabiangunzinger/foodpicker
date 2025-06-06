import ast
import csv
from collections import defaultdict
from datetime import date
from pathlib import Path
import random


MONTH_ABBR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def get_current_month():
    return MONTH_ABBR[date.today().month - 1]

def parse_food_item(food, season):
    try:
        months = eval(season)
        return food, months
    except:
        return food, ["All"]

def select_custom_from_dict(grouped_foods, n_per_group):
    current_month = get_current_month()
    result = {}
    for group, items in grouped_foods.items():
        seasonal = []
        non_seasonal = []
        for name, german, season in items:
            months = ast.literal_eval(season)
            label = f"{name} ({german})"
            if current_month in months or "All" in months:
                seasonal.append(label)
            else:
                non_seasonal.append(label)
        result[group] = sorted(seasonal) + (["-- Out of season --"] if seasonal and non_seasonal else []) + sorted(non_seasonal)
    return result


def load_foods_from_csv(filepath):
    grouped = defaultdict(list)
    with open(filepath, newline="", encoding="utf-8") as f:
        lines = (line for line in f if not line.strip().startswith("#"))
        reader = csv.DictReader(lines)
        for row in reader:
            group = row["group"]
            food_en = row["food"]
            food_de = row["food (german)"]
            season = row["season"]
            grouped[group].append((food_en, food_de, season))            
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
