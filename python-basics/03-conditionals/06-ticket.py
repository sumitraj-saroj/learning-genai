seat_type = input("Enter seat type (sleeper, AC, luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - AC available and beds available")
    case "luxury":
        print("You have everything")
