#!/usr/bin/env python3
import sys

# sys.argv เป็นลิสต์ที่เก็บคำสั่งทั้งหมด
# ตำแหน่งที่ 0 คือชื่อไฟล์ (aff_first_param.py)
# ดังนั้นพารามิเตอร์ตัวแรกที่แท้จริงจะอยู่ที่ตำแหน่งที่ 1 (sys.argv[1])

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")

# para_input = input()
# para = [i.strip('"') for i in para_input.split('" "')] # "Code Ninja" "Python" "Sad"

# if para[0]:
#     print(para[0])
# else:
#     print("none")
