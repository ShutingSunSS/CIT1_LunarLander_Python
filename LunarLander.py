def main():   
    print("The unit for altitude is meters, the unit for velocity is meters/second, the unit for fuel is liters.")
    play()
    again()
    
def play():
    """Initial values for altitude, velocity and fuel"""
    altitude = 1000.0
    velocity = 0
    fuel = 1000.0
    constant = 0.15

    # Before landing
    while altitude > 0:
        print("\naltitude (meters): ", altitude, "\nvelocity (meters/second): ", velocity, "\nfuel (liters): ", fuel)
        turnFuel = input("Enter how much fuel you want to burn (liters): ")
        # Make sure that each enter is a number
        while not isnumber(turnFuel):
               turnFuel = input("Enter how much fuel you want to burn (liters): ")
        turnFuel = float(turnFuel)
        # calculate how much fuel we actually can burn
        if turnFuel > fuel:
            turnFuel = fuel
        else:
            if turnFuel <= 0:
                turnFuel = 0
            else:
                turnFuel = turnFuel
        # calculate the velocity, altitude, and fuel after each burn
        velocity = velocity + 1.6 - turnFuel * constant
        altitude = altitude - velocity * 1
        fuel = fuel - turnFuel
        print("altitude (meters): ", altitude, "\nvelocity (meters/second): ", velocity, "\nfuel (liters): ", fuel)

    # After landing
    if altitude <= 0:
        if velocity <= 10:
            altitude = 0
            print("\nCongratulations! You've landed safely!")
            print("\naltitude (meters): ", altitude, "\nvelocity (meters/second): ", velocity, "\nfuel (liters): ", fuel)          
        else:
            print("\nThe crater you made on Mars is (meters): ", velocity)


# Try to make sure that the input of fuel is a number
def isnumber(num):
    try:
        val = float(num)
    except ValueError:
        print("That is not a number!")
        return False
    return True


# Ask if the player wants to play it again
def again():
    response = input("\nDo you wnat to play the game again? (any response that begins with 'y' or 'Y' means: yes, any response that begins with 'n' or 'N' means: no)")
    # If the first character of the input string is 'Y' or 'y', play again
    if response[:1] == 'y' or response[:1] == 'Y':
        play()
        return again()
    # If the first character of the input string is 'N' or 'n', print "Done"
    elif response[:1] == 'n' or response[:1] == 'N':
        print("Done")
    # If the first character of the input string is anything else, ask the question again
    else:
        return again()


if __name__ == "__main__":
    main()
