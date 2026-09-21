para_input = input()
para = [i.strip('"') for i in para_input.split('" "')]

if para[0]:
    for i in para:
        if not i.endswith("ism"):
            print(f"{i}ism")
else:
    print("none")