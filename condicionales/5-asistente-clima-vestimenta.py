clothing_by_temperature = {
    (0, 10): ["heavy coat", "scarf", "gloves"],
    (11, 18): ["light jacket", "sweater"],
    (19, 25): ["long-sleeve shirt", "comfortable pants"],
    (26, 30): ["t-shirt", "shorts"],
    (31, 40): ["very light clothing", "hat", "sunglasses"],
}

temperature = int(input("Enter the temperature in °C: "))
is_raining = input("Is it raining? (Y/N): ").lower()
recommendations = []

for temp_range, items in clothing_by_temperature.items():
    min_temp, max_temp = temp_range
    if min_temp <= temperature <= max_temp:
        recommendations.extend(items)
        break
if is_raining == "y":
    recommendations.extend(["umbrella", "raincoat"])
if recommendations:
    print(f"\nRecommended clothing for {temperature}°C:")
    print(", ".join(recommendations))
else:
    print("No recommendations available for this temperature")
