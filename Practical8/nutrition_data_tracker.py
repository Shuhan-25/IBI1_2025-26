#nutrition_data_tracker.py

class FoodItem:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def calculate_daily_totals(food_list):
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for item in food_list:
        total_calories += item.calories
        total_protein += item.protein
        total_carbs += item.carbs
        total_fat += item.fat

    print("Daily Nutrition Report")
    print(f"Total calories: {total_calories:.1f} kcal")
    print(f"Total protein: {total_protein:.1f} g")
    print(f"Total carbohydrates: {total_carbs:.1f} g")
    print(f"Total fat: {total_fat:.1f} g")

    if total_calories > 2500:
        print(f"Warning: Calorie intake exceeds 2500 kcal ({total_calories:.1f} kcal)")
    else: 
        print(f"Your calorie intake are within healthy limits.")

    if total_fat > 90:
        print(f"Warning: Fat intake exceeds 90 g ({total_fat:.1f} g)")
    else:
        print("Your fat intake are within healthy limits.")
        
    return {
        "calories": total_calories,
        "protein": total_protein,
        "carbs": total_carbs,
        "fat": total_fat
    }

# Example call
if __name__ == "__main__":
    apple = FoodItem("Apple", 60, 0.3, 15, 0.5)
    chicken = FoodItem("Chicken", 165, 31, 0, 3.6)
    rice = FoodItem("Rice", 130, 2.7, 28, 0.3)
    cake = FoodItem("Cake", 350, 4, 45, 15)

    daily_meals = [apple, chicken, rice, apple, cake, chicken]
    totals = calculate_daily_totals(daily_meals)
