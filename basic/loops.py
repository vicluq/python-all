## While 

''' 
    while [condition]:
        code_block
'''

num = int(input("Num to calc factorial: "))
backup = num
result = 1

while num > 0:
    result = result * num
    num = num - 1

print(f"factorial({backup}) = {result}")

# continue e break

num = backup
result = 1

while True:
    result = result * num
    num = num - 1
    if not num: # say do loop quando num = 0 pois 0 é falso
        break

print(f"factorial({backup}) = {result}")