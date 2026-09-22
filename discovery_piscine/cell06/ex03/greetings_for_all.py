#!/usr/bin/env python3

# กำหนดค่าเริ่มต้นเป็น "noble stranger" ตามข้อกำหนดของ Default Parameter
def greetings(name="noble stranger"):
    # เช็คว่าสิ่งที่ส่งมา เป็นชนิดข้อมูลแบบ String (str) หรือไม่
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

# ทดสอบเรียกใช้งานตามตัวอย่างเป๊ะๆ โดยไม่ต้องพึ่ง input()
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
# def greetings(name):
#     """print greetings"""
#     if not name:
#         name = "noble stranger"
#     if name.isnumeric():
#         print("Error! It was not a name.")
#     else:
#         print(f"Hello, {name}.")

# def main():
#     """call method greetings"""
#     name = str(input())
#     greetings(name)
# main()