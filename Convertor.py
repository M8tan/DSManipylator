# cd C:\Projects\Bootcamp\Python\PYDSConvertor  |  cls && python Convertor.py

def Convert_List_To_Dictionary(Input_List):
    Output_Dictionary = {}
    for i in range(len(Input_List)):
        Output_Dictionary[i] = Input_List[i]
    return Output_Dictionary
def Convert_List_To_Tuple(Input_List):
    Output_Tuple = tuple(Input_List)
    return Output_Tuple
def Convert_List_To_Set(Input_List):
    Output_Set = set()
    Remainders = list()
    for i in range(len(Input_List)):
        if Input_List[i] not in Output_Set:
            Output_Set.add(Input_List[i])
        else:
            Remainders.append(Input_List[i])
    if len(Remainders) > 0:
        return Output_Set, Remainders
    return Output_Set
def Reverse_List(Input_List):
    return Input_List[::-1]
def Find_List_Average(Input_List, Accuracy):
    Total = 0
    Yes_Int = 0
    for item in Input_List:
        if isinstance(item, (int, float)):
            Total += item
            Yes_Int += 1
    if Yes_Int == 0:
        return "No numbers in given list"
        #raise Exception("No numbers in given list")
    return round(Total / Yes_Int, Accuracy)
def Convert_To_Lowercase(Input_String):
    Output_String = ""
    for i in range(len(Input_String)):
        Current_Char = Input_String[i]
        match(Current_Char):
            case "A":
                Output_String += "a"
            case "B":
                Output_String += "b"
            case "C":
                Output_String += "c"
            case "D":
                Output_String += "d"
            case "E":
                Output_String += "e"
            case "F":
                Output_String += "f"
            case "G":
                Output_String += "g"
            case "H":
                Output_String += "h"
            case "I":
                Output_String += "i"
            case "J":
                Output_String += "j"
            case "K":
                Output_String += "k"
            case "L":
                Output_String += "l"
            case "M":
                Output_String += "m"
            case "N":
                Output_String += "n"
            case "O":
                Output_String += "o"
            case "P":
                Output_String += "p"
            case "Q":
                Output_String += "q"
            case "R":
                Output_String += "r"
            case "S":
                Output_String += "s"
            case "T":
                Output_String += "t"
            case "U":
                Output_String += "u"
            case "V":
                Output_String += "v"
            case "W":
                Output_String += "w"
            case "X":
                Output_String += "x"
            case "Y":
                Output_String += "y"
            case "Z":
                Output_String += "z"
            case _:
                Output_String += Current_Char
    return Output_String
def Convert_To_Uppercase(Input_String):
    Output_String = ""
    for i in range(len(Input_String)):
        Current_Char = Input_String[i]
        match(Current_Char):
            case "a":
                Output_String += "A"
            case "b":
                Output_String += "B"
            case "c":
                Output_String += "C"
            case "d":
                Output_String += "D"
            case "e":
                Output_String += "E"
            case "f":
                Output_String += "F"
            case "g":
                Output_String += "G"
            case "h":
                Output_String += "H"
            case "i":
                Output_String += "I"
            case "j":
                Output_String += "J"
            case "k":
                Output_String += "K"
            case "l":
                Output_String += "L"
            case "m":
                Output_String += "M"
            case "n":
                Output_String += "N"
            case "o":
                Output_String += "O"
            case "p":
                Output_String += "P"
            case "q":
                Output_String += "Q"
            case "r":
                Output_String += "R"
            case "s":
                Output_String += "S"
            case "t":
                Output_String += "T"
            case "u":
                Output_String += "U"
            case "v":
                Output_String += "V"
            case "w":
                Output_String += "W"
            case "x":
                Output_String += "X"
            case "y":
                Output_String += "Y"
            case "z":
                Output_String += "Z"
            case _:
                Output_String += Current_Char
    return Output_String
def Convert_First_Character_To_Lowercase(Input_String):
    Output_String = ""
    for i in range(len(Input_String)):
        Current_Char = Input_String[i]
        if i == 0:
            match(Current_Char):
                case "A":
                    Output_String += "a"
                case "B":
                    Output_String += "b"
                case "C":
                    Output_String += "c"
                case "D":
                    Output_String += "d"
                case "E":
                    Output_String += "e"
                case "F":
                    Output_String += "f"
                case "G":
                    Output_String += "g"
                case "H":
                    Output_String += "h"
                case "I":
                    Output_String += "i"
                case "J":
                    Output_String += "j"
                case "K":
                    Output_String += "k"
                case "L":
                    Output_String += "l"
                case "M":
                    Output_String += "m"
                case "N":
                    Output_String += "n"
                case "O":
                    Output_String += "o"
                case "P":
                    Output_String += "p"
                case "Q":
                    Output_String += "q"
                case "R":
                    Output_String += "r"
                case "S":
                    Output_String += "s"
                case "T":
                    Output_String += "t"
                case "U":
                    Output_String += "u"
                case "V":
                    Output_String += "v"
                case "W":
                    Output_String += "w"
                case "X":
                    Output_String += "x"
                case "Y":
                    Output_String += "y"
                case "Z":
                    Output_String += "z"
                case _:
                    Output_String += Current_Char
        else:
            Output_String += Current_Char
    return Output_String
def Convert_First_Character_To_Uppercase(Input_String):
    Output_String = ""
    for i in range(len(Input_String)):
        Current_Char = Input_String[i]
        if i == 0:
            match(Current_Char):
                case "a":
                    Output_String += "A"
                case "b":
                    Output_String += "B"
                case "c":
                    Output_String += "C"
                case "d":
                    Output_String += "D"
                case "e":
                    Output_String += "E"
                case "f":
                    Output_String += "F"
                case "g":
                    Output_String += "G"
                case "h":
                    Output_String += "H"
                case "i":
                    Output_String += "I"
                case "j":
                    Output_String += "J"
                case "k":
                    Output_String += "K"
                case "l":
                    Output_String += "L"
                case "m":
                    Output_String += "M"
                case "n":
                    Output_String += "N"
                case "o":
                    Output_String += "O"
                case "p":
                    Output_String += "P"
                case "q":
                    Output_String += "Q"
                case "r":
                    Output_String += "R"
                case "s":
                    Output_String += "S"
                case "t":
                    Output_String += "T"
                case "u":
                    Output_String += "U"
                case "v":
                    Output_String += "V"
                case "w":
                    Output_String += "W"
                case "x":
                    Output_String += "X"
                case "y":
                    Output_String += "Y"
                case "z":
                    Output_String += "Z"
                case _:
                    Output_String += Current_Char
        else:
            Output_String += Current_Char
    return Output_String
def Reverse_String(Input_String):
    #return Input_String[::-1]
    Output = ""
    i = len(Input_String)
    while i > 0:
        Current_Char = Input_String[i - 1]
        Output += Current_Char
        i -= 1
    return Output
def Remove_Duplicates_From_List(Input_List):
    Output = []
    for item in Input_List:
        if item not in Output:
            Output.append(item)
    return Output
def Flatten_List(Input_List):
    Output = []
    for item in Input_List:
        if isinstance(item, (list)):
            Output.extend(Flatten_List(item))
        else:
            Output.append(item)
    return Output
def Find_Max_Value_In_Dictionary(Input_Dict):
    return Input_Dict[max(Input_Dict.keys())]
def Find_Max_Value_Key_In_Dictionary(Input_Dict):
    return max(Input_Dict.keys())

if __name__ == "__main__":

    Test_List = [1, 2, 4, [2, 5], 8, "a", 3, 7, 2]
    Test_String = "Hello, world!!\ni loVe u 3000"
    print(Convert_First_Character_To_Lowercase(Test_String))
    print(Remove_Duplicates_From_List(Flatten_List(Test_List)))
    
    