#!/usr/bin/env python3
import sys
import re

# เช็คว่ามีพารามิเตอร์ส่งมา 2 ตัวพอดีหรือไม่ (รวมชื่อไฟล์เป็น 3)
if len(sys.argv) == 3:
    key = sys.argv[1]
    text = sys.argv[2]
    
    # นับจำนวนที่เจอ
    found = len(re.findall(key, text))
    
    if found:
        print(found)
    else:
        print("none")
else:
    print("none")