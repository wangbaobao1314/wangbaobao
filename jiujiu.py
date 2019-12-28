# !/usr/bin/python
# -*-coding:utf8-*-

# 百元百鸡
i = 0
for a in range(0,101):
    for b in range(0,101):
        for c in range(0,101):
            if a + b + c == 100:
                if 2*a + b + 0.5*c == 100:
                    i += 1
print(i)