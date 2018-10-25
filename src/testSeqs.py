from CurveADT import CurveT
from SeqADT import SeqT


def main():
    # check = True
    # while (check):
    #     Choice1 = input("Which would you like to test:\n"
    #                     "linVal                 (1)\n"
    #                     "quadVal                (2)\n"
    #                     "npolyVal               (3)\n"
    #                     "All other functions    (4)\n"
    #                     "Quit                   (0)\n"
    #                     "---> ")
    #     if (Choice1 == 0):
    #         print("Have a nice day!")
    #         check = False
    #     elif (Choice1 == 1):
    #         file = raw_input("Type the test file name you would like to use for linVal (example.txt): ")
    test1 = CurveT("lin_test.txt")
    x = -3.5 #input("What x value would you like to get the y value for?: ")
    y = test1.linVal(x)
    print("linVal: The y value for %f is %f" % (x, y))
    #     elif (Choice1 == 2):
    #         file = raw_input("Type the test file name you would like to use for quadVal (example.txt): ")
    test2 = CurveT("quad_test.txt")
    x = -3.5 #input("What x value would you like to get the y value for?: ")
    y = test2.quadVal(x)
    print("quadVal: The y value for %f is %f" % (x, y))
    #     elif (Choice1 == 3):
    #         file = raw_input("Type the test file name you would like to use for npolyVal (example.txt): ")
    test3 = CurveT("npoly_test.txt")
    n = 3 #input("What is the degree of the polynomial?: ")
    x = -4.5 #input("What x value would you like to get the y value for?: ")
    y = test3.npolyVal(n, x)
    print("npolyVal: The y value for %f is %f" % (x, y))
    #     elif (Choice1 == 4):
    #         print("Testing all other functions...\n")
    test4 = SeqT()
    test4.add(0, 1)
    test4.add(1, 2)
    test4.add(0, 0)
    if (test4.Seq[0] == 0 and test4.Seq[1] == 1 and test4.Seq[2] == 2):
        test_add = "Pass"
    else:
        test_add = "Fail"
    if (test4.size() == 3):
        test_size = "Pass"
    else:
        test_size = "Fail"
    if (test4.get(1) == 1):
        test_get = "Pass"
    else:
        test_get = "Fail"
    test4.rm(2)
    if (len(test4.Seq) == 2):
        test_rm = "Pass"
    else:
        test_rm = "Fail"
    test4.set(1, 1234)
    if (test4.Seq[1] == 1234):
        test_set = "Pass"
    else:
        test_set = "Fail"
    print("Function Tested:\tResult:\n"
          "add() \t              %s\n"
          "rm()  \t              %s\n"
          "get() \t              %s\n"
          "set() \t              %s\n"
          "size()\t              %s\n"
          % (test_add, test_rm, test_get, test_set, test_size))
    #
    #     else:
    #         print("Invalid choice. Please select options 1-4, or 0 to quit.")


main()
