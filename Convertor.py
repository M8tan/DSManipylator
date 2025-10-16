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
    
        
    

if __name__ == "__main__":

    Test_List = [1, 2, 4, 8, "a", 3, 7, 2]
    bs = ["a", "b", "c"]
    Converted = Convert_List_To_Set(Test_List)
    print((Converted[0]))
    print("H")
    