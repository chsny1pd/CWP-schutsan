#!/usr/bin/env python3
import sys

# เช็คว่ามีพารามิเตอร์ส่งมา 1 ตัวพอดีหรือไม่ (เมื่อรวมชื่อไฟล์แล้ว ความยาวต้องเท่ากับ 2)
if len(sys.argv) == 2:
    # โปรแกรมแสดงข้อความถามและรอรับคำตอบจากผู้ใช้
    text_input = input("What was the parameter? ")
    
    # นำคำตอบมาเทียบกับพารามิเตอร์ตอนที่สั่งรันโปรแกรม (sys.argv[1])
    if sys.argv[1] == text_input:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")