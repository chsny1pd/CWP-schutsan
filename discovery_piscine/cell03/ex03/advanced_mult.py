main_num = 0
while main_num <= 10:
    print(f"Table de {main_num}:", end="")
        
    sub_num = 0
    while sub_num <= 10:
        print(f" {main_num * sub_num}", end="")
        sub_num += 1
            
    print()
    main_num += 1