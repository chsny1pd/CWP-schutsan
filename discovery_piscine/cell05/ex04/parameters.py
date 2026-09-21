para_input = input()
para = [i.strip('"') for i in para_input.split('" "')]
print("Number of parameters: ", len(para) if para[0] else 0)