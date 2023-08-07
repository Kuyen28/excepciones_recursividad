fruits = ["Banana", "Apple", "Watermelon", "Pineapple", "Strawberries"]

while True:
    user_option = (input("Ingresa un número entre el 0 y el 4 para elegir tu fruta, q para salir:"))
    
    if user_option == "q":
        break
    try:
        print(fruits[int(user_option)])
    except IndexError as indexerror:
        print("Por favor ingresar un número del 0 al 4.", indexerror)
    except ValueError as valueerror:
        print("Por favor ingresar un número", valueerror)