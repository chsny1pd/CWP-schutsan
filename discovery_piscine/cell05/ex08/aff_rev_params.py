para_input = input()
para = [i.strip('"') for i in para_input.split('" "')] # "Code Ninja" "Python" "Sad"

if len(para) >= 2:
    for i in reversed(para):
        print(i)
else:
    print("none")