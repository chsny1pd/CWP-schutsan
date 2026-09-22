#!/usr/bin/env python3
import sys

# เช็คว่ามีพารามิเตอร์ส่งมา 1 ตัวพอดีหรือไม่ (รวมชื่อไฟล์เป็น 2)
if len(sys.argv) == 2:
    # นับจำนวนตัว 'z' จากพารามิเตอร์ตัวแรก (ตำแหน่งที่ 1)
    count_z = sys.argv[1].count('z')
    
    if count_z > 0:
        print("z" * count_z)
    else:
        print("none")
else:
    print("none")