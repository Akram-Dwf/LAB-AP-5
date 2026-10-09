def convert_temperature(value, source_scale, target_scale):
    """Convert a temperature between Celsius (C), Fahrenheit (F), and Kelvin (K)."""
    valid_scales = ("C", "F", "K")
    if source_scale not in valid_scales or target_scale not in valid_scales:
        raise ValueError()

    if source_scale == "C":
        celsius = value
    elif source_scale == "F":
        celsius = (value - 32) * 5 / 9
    else:  # K
        celsius = value - 273.15


    if target_scale == "C":
        result = celsius
    elif target_scale == "F":
        result = celsius * 9 / 5 + 32
    else:  # K
        result = celsius + 273.15

    return round(result, 2)


print("=== Temperature Conversion ===")
while True:
    temp_input = input("Enter temperature (or 'done' to exit): ")
    if temp_input.strip().lower() == "done":
        break

    try:
        temperature = float(temp_input)
    except ValueError:
        print("Error: Invalid temperature value.")
        continue

    source_scale = input("Source scale (C/F/K): ").strip().upper()
    target_scale = input("Target scale (C/F/K): ").strip().upper()

    try:
        result = convert_temperature(temperature, source_scale, target_scale)
        print(f"Result: {temperature} {source_scale} = {result} {target_scale}")
    except ValueError:
        print("Error: Unknown temperature scale.")