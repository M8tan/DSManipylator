# cd C:\Projects\Bootcamp\Python\PYDSConvertor  |  cls && python Convertor.py

def Convert_List_To_Dictionary(Input_List):
    Output_Dictionary = {}
    for i in range(len(Input_List)):
        Output_Dictionary[i] = Input_List[i]
    return Output_Dictionary
def Convert_List_To_Tuple(Input_List):
    Output_Tuple = tuple(Input_List)
    return Output_Tuple
def Reverse_List(Input_List):
    return Input_List[::-1]
if __name__ == "__main__":

    Test_List = [1, 2, 4, 8, 6, 3, 7, 2]
    Test_Dict = Convert_List_To_Dictionary(Test_List)
    Test_Tuple = Convert_List_To_Tuple(Test_List)
    Eversed_List = Reverse_List(Test_List)
    print(Test_Dict)
    print(Test_Tuple)
    print(Eversed_List)