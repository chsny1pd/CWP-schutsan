#!/usr/bin/env python3
import sys

# เช็คว่ามีพารามิเตอร์ส่งมาหรือไม่ (ความยาว sys.argv ต้องมากกว่า 1 เพราะ index 0 คือชื่อไฟล์)
if len(sys.argv) > 1:
    # ดึงเฉพาะพารามิเตอร์มาเก็บไว้ในลิสต์ (เริ่มจาก index 1 ข้ามชื่อไฟล์ไป)
    params = sys.argv[1:]
    
    # แสดงจำนวนพารามิเตอร์
    print(f"parameters: {len(params)}")
    
    # วนลูปเพื่อแสดงค่าและความยาวของแต่ละพารามิเตอร์ตามลอจิกของคุณ
    for i in params:
        print(f"{i}: {len(i)}")
else:
    print("none")