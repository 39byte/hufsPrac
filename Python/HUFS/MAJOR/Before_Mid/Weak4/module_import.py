import Wk4_PlusModule as PMod

a = PMod.plus(1, 2)
print(a)
b = PMod.plus('Hello, ', 'World!')
print(b)

wp = input('무기가 무엇인가요? (sword / axe)\n')
lv = input('무기 레벨은 몇인가요?\n')
heart = 8000
heart -= PMod.damage(wp, 5)
print(heart)