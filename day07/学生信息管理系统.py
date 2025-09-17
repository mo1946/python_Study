
info = [
    {'name' : '小妹', 'id' : '111', 'tel' : '111'},
    {'name' : '小明', 'id' : '222', 'tel' : '222'}
]
def print_logo():
    '''
    显示操作界面
    :return:
    '''
    print('1. 添加学生信息')
    print('2. 删除学生信息')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有学生信息')
    print('6. 退出系统')
    print('-' * 30)
    print()

def add_student():
    """
    用于添加学生信息
    :return:
    """
    stu_name = input('请输入姓名：')
    stu_id = input('请输入id：')
    for list_id in info:
        if stu_id != list_id['id']:
            break
        else:
            while True:
                print('学号已有，请重新输入')
                stu_id = input('请输入id：')
                if stu_id != list_id['id']:
                    break
    stu_tel = input('请输入电话号码：')
    stu_dict = {'name' : stu_name, 'id' : stu_id, 'tel' : stu_tel}
    info.append(stu_dict)

def del_student():
    """
    用于删除学生信息
    :return:
    """
    while True:
        stu_id = input('请输入要删除的学生id(输入end结束删除)：')
        if stu_id == 'end':
            print('结束删除')
            return

        found = False
        for stu in info[:]:
            if stu['id'] == stu_id:
                info.remove(stu)
                print('删除成功！')
                found = True
                break

        if not found:
            print('学号未录入，请重新输入')
        else:
            return

def update_student():
    """
    修改学生信息
    :return:
    """
    while True:
        stu_id = input('请输入要修改的学生id(输入end结束删除)：')
        if stu_id == 'end':
            print('结束修改')
            return

        found = False
        for stu in info[:]:
            if stu['id'] == stu_id:
                info.remove(stu)
                add_student()
                print('修改成功！')
                found = True
                break

        if not found:
            print('学号未录入，请重新输入')
        else:
            return

def search_one_student():
    """
    查询单个学生信息
    :return:
    """
    while True:
        stu_id = input('请输入要查询的学生id(输入end结束删除)：')
        if stu_id == 'end':
            print('结束查询')
            return

        found = False
        for stu in info[:]:
            if stu['id'] == stu_id:
                print(f'姓名：{stu['name']}, 编号：{stu['id']}, 电话号：{stu['tel']}')
                found = True
                break

        if not found:
            print('学号未录入，请重新输入')
        else:
            return

def search_all_student():
    """
    查询所有学生信息
    :return:
    """
    if len(info) == 0:
        print('暂无学生信息!')
        print()
    else:
        for stu_info in info:
            print(f'姓名：{stu_info['name']}, 编号：{stu_info['id']}, 电话号：{stu_info['tel']}')
        print()
    return


def execute():
    """
    :return: 跳转编号所指定的操作
    """
    while True:
        print_logo()
        try:
            num = input('请输入你要执行的编号：')
            if num == '1':
                add_student()
            elif num == '2':
                del_student()
            elif num == '3':
                update_student()
            elif num == '4':
                search_one_student()
            elif num == '5':
                search_all_student()
            elif num == '6':
                print('-> 退出系统 <-')
                break
            else:
                print("输入有误，请重新输入")
        except:
            pass

if __name__ == '__main__':
    execute()

# 这个版本的代码重复较多，函数里的变量名不一致




