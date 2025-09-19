# Ask the user for the weather condition
weather_condition = input("What's the weather like today? (sunny/rainy/cloudy): ")

# Control flow to check the weather condition and give advice
# if statement for sunny conditions
if weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
# elif statement for rainy conditions
elif weather_condition == "rainy":
    print("Don't forget your umbrella. and a raincoat.")
# elif statement for cloudy conditions
elif weather_condition == "cloudy":
    print("Make sure to wear a warm coat and a scarf")
# else statement for any other conditions
else:
    print("Sorry, I don't have a recommendations for this weather.")