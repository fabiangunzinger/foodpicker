from foodpicker.utils import load_foods_from_csv, export_selection_to_shopping_list_csv, select_custom_from_dict

def main():
    grouped_foods = load_foods_from_csv("foodpicker/data/foods.csv")

    # Set custom n per group
    n_per_group = {

        "Vegetables": 10,
        "Fruits": 5,
        "Legumes": 2,
        "Whole Grains": 1,
        "Animal Proteins": 4,
        "Dairy": 2,
        "Fats & Oils": 2,
        "Nuts & Seeds": 2,
        "Sweeteners": 1,
        "Beverages": 2,
        "Miscellaneous": 1,

        "Staples": 1000,
    }

    selected = select_custom_from_dict(grouped_foods, n_per_group)
    path = export_selection_to_shopping_list_csv(selected)
    if path:
        print(f"Weekly food list written to: {path}")

if __name__ == "__main__":
    main()
