from service.mergeData import *
from service.etl import *
from service.showData import *


while True:
    print(" ")
    print("menu : ")
    print("1. Merge data")
    print("2. etl")
    print("3. show data analytic")
    print("0. Exit")
    print(" ")

    user_input = int(input("input menu code : "))
    print(" ")

    if user_input == 1:
        merge_data()
    elif user_input== 2:
        run_etl()
    elif user_input== 3:
        show_analytic()
    elif user_input== 0:
        break
    else:
        print("please input valid code !")
        print(" ")