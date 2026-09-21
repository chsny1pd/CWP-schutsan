para_input = input()
para = [i.strip('"') for i in para_input.split('" "')] # "Code Ninja" "Python" "Sad"

if para[0]:
    print(para[0])
else:
    print("none")