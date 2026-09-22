#!/usr/bin/env python3
import sys

# sys.argv มีชื่อไฟล์อยู่ที่ตำแหน่ง 0 เสมอ
# ถ้าผู้ใช้ใส่พารามิเตอร์มา 1 ตัว ความยาวของ sys.argv จะต้องเท่ากับ 2 พอดี
if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print("none")