def My_print_name(name):
    print("Bienvenue dans mon programme, Ecrivez STOP pour arreter")
    while True:              
        if name.lower() == "stop":
            print("bye")
            break
            
        else:
            print("This is your name: ", name)

My_print_name(input("Put your name here :"))

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     else:
#         print("ok")
#     print(line)
    
# print('Done!')