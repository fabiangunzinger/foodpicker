from foodpicker.utils import load_foods_from_csv, export_selection_to_shopping_list_csv, select_custom_from_dict

def main():
    grouped_foods = load_foods_from_csv("foodpicker/data/foods.csv")

    # Set custom n per group
    n_per_group = {
        "Non-starchy vegetables": 1000,
        "Starchy vegetables": 1000,
        "Fruits": 1000,
        "Legumes": 1000,
        "Whole Grains": 1000,
        "Animal Proteins": 1000,
        "Dairy": 1000,
        "Fats & Oils": 1000,
        "Nuts & Seeds": 1000,
        "Sweeteners": 1000,
        "Beverages": 1000,
        "Spices & Herbs": 1000,
        "Fermented Foods": 1000,
        "Miscellaneous": 1000,
    }

    selected = select_custom_from_dict(grouped_foods, n_per_group)
    path = export_selection_to_shopping_list_csv(selected)
    if path:
        print(f"Weekly food list written to: {path}")

if __name__ == "__main__":
    main()
