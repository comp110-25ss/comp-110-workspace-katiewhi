"""My Tea Party Planner!"""

__author__ = "730546969"


def main_planner(guests: int) -> None:
    """Entry point of the program."""
    tea_count: int = tea_bags(people=guests)
    treat_count: int = treats(people=guests)
    total: float = cost(tea_count=tea_count, treat_count=treat_count)

    # print out the plan for the tea party
    print(f"A Cozy Tea Party for {guests} People")
    print("Tea Bags: " + str(tea_count))
    print("Treats: " + str(treat_count))
    print("Cost: $" + str(total))


def tea_bags(people: int) -> int:
    """Returns the number of tea bags if each drinks 2 teas."""
    return people * 2  # Each person will drink 2 teas so we would multiply by 2


def treats(people: int) -> int:
    """Returns treats needed based on the teas (1.5 treats per tea)."""
    # Instead of redoing the math, I used the tea_bags
    # function so if the number of teas per person
    # changes, I only have to change it in one place in my code

    tea_count: int = tea_bags(people=people)
    return int(tea_count * 1.5)


# Here, I would multiply the number of teas by 1.5
# because that gives me the treat count and I use
# int to convert it to an integer


def cost(tea_count: int, treat_count: int) -> float:
    """Returns the total cost of tea bags and treats."""
    # Tea bags cost $0.50 each and treats cost $0.75 each

    return (tea_count * 0.50) + (
        treat_count * 0.75
    )  # I multiply the tea count by 0.50 and
    # the treat count by 0.75 to get the total cost of the tea party


if __name__ == "__main__":

    # This will ask the user for the number of guests
    # and convert their input to an integer
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
