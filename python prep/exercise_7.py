current_temperature = float(input("Please enter temperature: "))

min_ideal_temperature = 20.0
max_ideal_temperature = 22.0

if current_temperature < min_ideal_temperature:
    print("Too cold")
    current_temperature = current_temperature + 1
elif current_temperature > max_ideal_temperature:
    print("Too hot")
    current_temperature = current_temperature - 1
else:
    print("Just nice")

print(f"New temperature: {current_temperature}")

#with temp didnt accept the syntax in python interpreter