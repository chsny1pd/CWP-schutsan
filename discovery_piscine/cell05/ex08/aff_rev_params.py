#!/usr/bin/env python3
import sys

# เช็คว่ามีพารามิเตอร์ส่งมาตั้งแต่ 2 ตัวขึ้นไป (เมื่อรวมชื่อไฟล์แล้ว ความยาวต้องมากกว่า 2)
if len(sys.argv) > 2:
    # ใช้ sys.argv[1:] เพื่อตัดชื่อไฟล์ (ตำแหน่งที่ 0) ทิ้งไปก่อน แล้วค่อยสั่ง reversed
    for i in reversed(sys.argv[1:]):
        print(i)
else:
    print("none")