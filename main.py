from Line_InterSection import Intersection


def main():
    number_A = eval(input(" A Enter the numbers:"))
    number_B = eval(input(" B Enter the numbers:"))
    number_C = eval(input(" C Enter the numbers:"))
    number_D = eval(input(" D Enter the numbers:"))
    number_E = eval(input(" E Enter the numbers:"))
    number_F = eval(input(" F Enter the numbers:"))

    value = Intersection(number_A, number_B, number_C, number_D, number_E, number_F)
    print("A is ", value.getA())
    print("B is", value.getB())
    print("The value for X is :", value.getX())
    print("The value for y is :", value.getY())


main()
