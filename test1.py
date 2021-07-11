import pytest

def get_common_path(path: list):
    li = [[] for i in range(len(path))]
    com = []
    for i in range(len(path)):
        li[i]= path[i].split('/')

    le = min([len(i) for i in li])
    # print(le)

    for i in range(le):
        for j in range(len(li)-1):
            flag = 0
            if li[j][i] != li[j+1][i]:
                flag = 1
                break
        if flag == 0:
            com.append(li[j][i])
    # print(com)
    if com == ['']:
        return '/'
    return '/'.join(com)

path = ['/hogwarts/images/image1.png', '/hogwarts/images/image2.png']
path1 = ['/hogwarts/assets/style.css', '/hogwarts/scripts/app.js', 'home/setting.conf']
path2 = ['/hogwarts/assets/style.css', '/.bin/mocha', '/read.md']
print(get_common_path(path))
print(get_common_path(path1))
print(get_common_path(path2))

def test_get():
    assert get_common_path(['/hogwarts/images/image1.png', '/hogwarts/images/image2.png']) == '/hogwarts/images/'
    assert get_common_path(['/hogwarts/assets/style.css', '/hogwarts/scripts/app.js', 'home/setting.conf']) == ''
    assert get_common_path(['/hogwarts/assets/style.css', '/.bin/mocha', '/read.md']) == '/'

