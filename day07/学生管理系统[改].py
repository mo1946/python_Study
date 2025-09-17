info = [
    {'name': '小妹', 'id': '111', 'tel': '111'},
    {'name': '小明', 'id': '222', 'tel': '222'}
]


def print_logo():
    """显示操作界面"""
    print('1. 添加学生信息')
    print('2. 删除学生信息')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有学生信息')
    print('6. 退出系统')
    print('-' * 30)
    print()


def find_student(student_id):
    """查找学生信息"""
    for student in info:
        if student['id'] == student_id:
            return student
    return None


def input_student_info():
    """输入学生信息并验证"""
    while True:
        name = input('请输入姓名：')
        student_id = input('请输入id：')
        if find_student(student_id):
            print('学号已存在，请重新输入')
            continue
        tel = input('请输入电话号码：')
        return {'name': name, 'id': student_id, 'tel': tel}


def add_student():
    """添加学生信息"""
    student = input_student_info()
    info.append(student)
    print('添加成功！')


def del_student():
    """删除学生信息"""
    while True:
        student_id = input('请输入要删除的学生id(输入end结束删除)：')
        if student_id == 'end':
            print('结束删除')
            return

        student = find_student(student_id)
        if student:
            info.remove(student)
            print('删除成功！')
            return
        print('学号未录入，请重新输入')


def update_student():
    """修改学生信息"""
    while True:
        student_id = input('请输入要修改的学生id(输入end结束修改)：')
        if student_id == 'end':
            print('结束修改')
            return

        student = find_student(student_id)
        if student:
            info.remove(student)
            new_student = input_student_info()
            info.append(new_student)
            print('修改成功！')
            return
        print('学号未录入，请重新输入')


def search_one_student():
    """查询单个学生信息"""
    while True:
        student_id = input('请输入要查询的学生id(输入end结束查询)：')
        if student_id == 'end':
            print('结束查询')
            return

        student = find_student(student_id)
        if student:
            print(f"姓名：{student['name']}, 编号：{student['id']}, 电话号：{student['tel']}")
            return
        print('学号未录入，请重新输入')


def search_all_student():
    """查询所有学生信息"""
    if not info:
        print('暂无学生信息!')
    else:
        for student in info:
            print(f"姓名：{student['name']}, 编号：{student['id']}, 电话号：{student['tel']}")
    print()


def execute():
    """主执行函数"""
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
        except Exception as e:
            print(f"发生错误：{e}")


if __name__ == '__main__':
    execute()