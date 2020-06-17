from .models import Stu_Info
from django.utils import timezone

class Student(object):
    '''
        学生类
        建树或者学生的信息展示方法
    '''

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        self.id = value.id
        self.name = value.name
        self.classes = value.classes
        self.major = value.major
        self.information = value.information
        self.deeds = value.deeds
        self.is_deleted = value.is_deleted
        self.ip = value.ip
        self.votes = value.votes

    def show_id(self):
        return


class InfoDeal(object):
    def __init__(self):
        self.students = Stu_Info.object.filter(is_deleted=False)
        self.hash_list = []
        # 哈希表最大长度
        self.max_length = len(self.students)
        # 构建方法 mod
        self.hash_mod = self.max_length + 5
        # 哈希表
        self.hash_table = [None for i in range(self.max_length)]
        # 二次排序树根节点
        self.root = Student(self.students[0])
        # 存储排名信息
        self.rank_list = []


    def build_hash(self):
        '''
            开放寻址法
            构建哈希
        '''
        # 冲突的数据延迟添加
        bad_hash_data = []
        for student in self.students:
            # 寻找位置,注意主键的类型
            # print(student.id)
            insert_pos = int(student.id) % self.hash_mod
            if self.hash_table[insert_pos] is None:
                self.hash_table[insert_pos] = student
            else:
                bad_hash_data.append(student)
        # 消解冲突
        for student in bad_hash_data:
            insert_pos = int(student.id) % self.hash_mod
            # 当前冲突位置向后查找
            while insert_pos < self.max_length:
                if self.hash_table[insert_pos] is None:
                    self.hash_table[insert_pos] = student
                    break
                insert_pos += 1
            # 表首冲突位置向后查找
            if insert_pos >= self.max_length:
                for insert_pos in range(0, self.max_length):
                    if self.hash_table[insert_pos] is None:
                        self.hash_table[insert_pos] = student
                        break

    def find_hash(self, value):
        '''
            查找关键字
            传递的参数是id
            返回下标
        '''
        find_pos = int(value) % self.hash_mod
        # 直接定位
        if self.hash_table[find_pos].id == value:
            return find_pos

        # 解决冲突
        # 当前位置向后查找
        while find_pos < self.max_length:
            if self.hash_table[find_pos].id == value:
                return find_pos
            find_pos += 1

        # 表首位置向冲突位置查找
        for find_pos in range(int(value) % self.hash_mod):
            if self.hash_table[find_pos].id == value:
                return find_pos

        # 没有查找到
        return -1


    def update_vote(self, *values):
        '''
            传递的参数是学号（主键）
            可以传递若干个 学号
            更新数据信息，投票自增1
        '''
        for value in values:
            user = Stu_Info.object.get(id=value)
            user.votes += 1
            user.last_update_time = timezone.now()
            user.save()
 
    def return_vote_info(self):
        '''
            返回学生的id，name
            information,calsses
            字典
        '''
        self.build_sort_tree()
        self.mid_order_tree(self.root)

        votes_list = []
        i = 1
        for student in self.rank_list[::-1]:
            votes_list.append({
                'id':student.id,
                'name':student.name,
                'information':student.information,
                'classes':student.classes,
                'rank': i,
                'votes':student.votes
            })
            i += 1

        return votes_list

    def build_sort_tree(self):
        '''
            构建二叉排序树
            self.root 是根节点
            节点是 student 
            按照 student.votes <=> tree_node.votes
        '''

        for student in self.students[1:]:
            tree_node = Student(student)
            self.insert_tree(self.root, tree_node)
        # print('tree data is ', self.root.id,  self.root.votes)
        # print('tree data is ', self.root.right.id, self.root.right.votes)
            
    def insert_tree(self, node, value):
        '''
            插入节点
            传递参数是 student 类
            使用 value 当作形参
            返回值 空
            插入到 self.root 树里面
        '''
        # 左子树
        if value.votes < node.votes:
            if node.left is None:
                node.left = value
            else:
                self.insert_tree(node.left, value)
        else:
            if node.right is None:
                node.right = value
            else:
                self.insert_tree(node.right, value)

    def mid_order_tree(self, node):
        '''
            中序遍历
        '''
        if node is None:
            return
        self.mid_order_tree(node.left)
        self.rank_list.append(node)
        # print("当前节点的票数是", node.votes)

        self.mid_order_tree(node.right)




    def tree_main(self):
        self.build_sort_tree()
        self.mid_order_tree(self.root)

    def return_rank_info(self):
        self.build_sort_tree()
        self.mid_order_tree(self.root)
        

        name = [student.name for student in self.rank_list][::-1]
        votes = [student.votes for student in self.rank_list][::-1]
        
        if len(name) > 10:
            return name[:10], votes[:10]
        # 反转降序传参
        return name, votes