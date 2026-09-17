destination = str(input("Enter your destination (Beach/Mountains/City): "))
time = str(input("Enter the time (Day/Night): "))
type = str(input("Enter the visitor type (Minor/Adult): "))
packet = ""
match destination:
    case "Beach":
        if time == "Day" and (type == "Minor" or type == "Adult"):
            packet = "A"
        elif time == "Night" and type == "Adult":
            packet = "C"
    case "Mountains":
        if time == "Day" and type == "Adult":
            packet = "B"
        elif time == "Night" and type == "Adult":
            packet = "C"
    case "City":
        if time == "Night" and (type == "Minor" or type == "Adult"):
            packet = "C"
    case _:
        print("No packets available")
if packet:
    print("Packet", packet)
else:
    print("No packets available")

