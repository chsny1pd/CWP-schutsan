#!/usr/bin/env python3
import sys

# เช็คว่ามีพารามิเตอร์ 2 ตัวพอดีหรือไม่ (รวมชื่อไฟล์ตำแหน่งที่ 0 ความยาวต้องเท่ากับ 3)
if len(sys.argv) == 3:
    # ดึงค่าพารามิเตอร์ตำแหน่งที่ 1 และ 2 มาแปลงเป็นตัวเลข (int)
    startnum = int(sys.argv[1])
    endnum = int(sys.argv[2])
    
    # ใช้ลอจิกของคุณในการสร้าง list จาก range
    step = 1 if startnum < endnum else -1
    print(list(range(startnum, endnum + step, step)))
else:
    print("none")