def plus(a, b):
    result = a + b
    return result

def damage(weapon, level):
    if weapon == 'sword':
        dam = level * 1600
        return dam
    if weapon == 'axe':
        dam = level * 2000
        return dam

if __name__ == '__main__':
    print('내가 드디어 모듈을 만들었다!')