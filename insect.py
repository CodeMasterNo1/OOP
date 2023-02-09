import insect_class as ic


def main():
    my_insect = ic.insect()

    print("This insect can fly: ", my_insect.get_fly())

    #insect fly
    print('This insect is going to fly ten times: ')
    for count in range(10):
        my_insect.fly()

        # Display the side of the coin that is facing up.
        print('This insect flew:', my_insect.get_fly())






main()
