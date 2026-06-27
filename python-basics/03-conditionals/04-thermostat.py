device_status = "Active"

temperature = 40

if device_status == "Active":
    if temperature > 35:
        print("High temperature alert !")
    else:
        print("temperature is normal")
else:
    print("Device is offline")
