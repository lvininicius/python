letra=input("informe sey estado civil (D,C,S,V): ")
match letra:
    case "d" | "D":
        print ("divorciado")
    case "c" | "C":
        print ("casado")
    case "s" | "S":
        print ("solteiro")
    case "V" | "v":
        print ("Viuvo")
    case _:
        print("Opção Invalida")