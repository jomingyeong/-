food = [
    ["김치찌게", 123, 345 ],
    ["계란국", 321, 543 ]
]
name = input("조회할 음식 이름:")
for k in range (2):
    if name == food[k][0]:
        break
print("=================================")
print("이름:",food[k][0])
print("단백질:",food[k][1])
print("탄수화물:",food[k][2])



