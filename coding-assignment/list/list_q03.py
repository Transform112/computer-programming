'''
 Create a program that will keep track of items for a shopping list. The program should keep 
 asking for new items until nothing is entered (no input followed by enter/return key). The 
 program should then display the full shopping list. 
'''
print("Enter Your Choice,\n1-add items \n2-remove item \n3-display ShoppingList \n4-To exit")
user_input = int(input("Enter Valid Number: "))
shopping_list = []
while user_input:
    match user_input:
        case 1:
            new_input = input("Enter item Name:").capitalize()
            shopping_list.append(new_input)
            print("New Item Added")
        case 2:
            item_toremoved = input("Enter Item U want to Remove:").capitalize()
            if item_toremoved in shopping_list:
                shopping_list.remove(item_toremoved)
            elif len(shopping_list) == 0:
                print("No item Found")    
            else:
                print("No such Item found")    
            print("Item removed Succesfully")
        case 3:
            if len(shopping_list) == 0:
                print("No item added")
            else:
                for i in range(len(shopping_list)):
                    print(f'{i+1}: {shopping_list[i]}')
        case 4:
            print("You Pressed 4,Bye, See U Soon")
            break
        case _:
            print("Not Valid Input")
    user_input = int(input("Enter Valid Number: "))