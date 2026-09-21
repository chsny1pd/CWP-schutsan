para_input = input()

if not para_input:
    print("none")
else:
    text_input = input("What was the parameter? ")
    if para_input == text_input:
        print("Good job!")
    else:
        print("Nope, sorry...")