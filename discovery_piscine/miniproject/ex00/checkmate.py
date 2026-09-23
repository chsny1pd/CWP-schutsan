def checkmate(board: str):
    try:
        rows = board.splitlines()
       
        if not rows:
            return 

        size = len(rows)  
        king_pos = None   
        king_count = 0    

        for r in range(size):
          
            if len(rows[r]) != size:
                print("Error")
                return
            
            for c in range(size):
                if rows[r][c] == 'K':
                    king_pos = (r, c)  
                    king_count += 1    

        if king_count != 1:
            print("Error")
            return

        kr, kc = king_pos

        directions = [
            (-1, 0, ['R', 'Q']),        
            (1, 0, ['R', 'Q']),         
            (0, -1, ['R', 'Q']),        
            (0, 1, ['R', 'Q']),         
            (-1, -1, ['B', 'Q']),       
            (-1, 1, ['B', 'Q']),        
            (1, -1, ['B', 'Q', 'P']),   
            (1, 1, ['B', 'Q', 'P'])     
        ]

        for dr, dc, threats in directions:
           
            r = kr + dr
            c = kc + dc
            distance = 1  

            while 0 <= r < size and 0 <= c < size:
                piece = rows[r][c]  

                if piece in ['P', 'B', 'R', 'Q']:

                    if piece in threats:

                        if piece == 'P' and distance > 1:
                            break 

                        print("Success")
                        return

                    break  

                r += dr
                c += dc
                distance += 1  

        print("Fail")
        
    except Exception:
        
        print("Error")