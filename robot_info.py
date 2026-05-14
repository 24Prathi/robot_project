# updated by me
# Ask user input
robot_name = input("Enter the robot name: ")
battery = int(input("Enter battery percentage: "))

# Display robot info
print("\nRobot Name:", robot_name)

# Check battery condition
if battery >= 50:
    print("Robot is ready to move")
else:
    print("Low battery, please charge")