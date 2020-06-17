from CurriculumDesign.models import Stu_Info
class MyException(object):
    def __init__(self, student):
        self.student = student

    def ip_exception(self):
        '''
            处理IP异常
        '''
        IP_list = Stu_Info.object.all().values('ip')
        if self.student.ip in [i['ip'] for i in IP_list] and self.student.ip != '127.0.0.1':
            return {'mes_title': 'IP冲突', 'mes_cont': ['当前IP已经投过票了','不能重复投票','亲😙，请不要恶意刷取数据哦。'], 'flag': 0}
        return None

    def id_exception(self):
        '''
            学号异常处理
            唯一标识，主键，重要！！id
        '''
        try:
            int(self.student.id)
        except:
            return {'mes_title': '学号错误', 'mes_cont': ['请输入正确的数字学号','学号作为身份唯一标识，谨慎填写','亲😙，请不要恶意刷取数据哦。'], 'flag': 0}
        # print(self.student.id)
        if len(self.student.id) > 12:
            return {'mes_title': '学号错误', 'mes_cont': ['学号长度不能超过12位','学号作为身份唯一标识，谨慎填写','亲😙，请不要恶意刷取数据哦。'], 'flag': 0}
        if self.student.id in [i['id'] for i in Stu_Info.object.all().values('id')]:
             return {'mes_title': '学号错误', 'mes_cont': ['学号已经存在哦','学号作为身份唯一标识，谨慎填写','亲😙，请不要恶意刷取数据哦。'], 'flag': 0}
        return None

    def name_exception(self):
        '''
            名字异常处理
        '''
        # 姓名长度
        if len(self.student.name) > 4:
            return {'mes_title': '姓名长度错误', 'mes_cont': ['请输入合法长度的名字', '亲😙，请不要恶意刷取数据哦。'], 'flag': 0}
        # 汉字
        for ch in self.student.name:
            if not (ch >= u'\u4e00' and ch <= u'\u9fa5'):
                return {'mes_title': '姓名格式错误', 'mes_cont': ['请输入中文名字哦', '例如：王小明', '亲😙，请不要恶意刷取数据哦。'], 'flag': 0}
        return None

    def classes_exception(self):
        '''
            班级输入异常处理
        '''
        if self.student.classes not in ['数据科学18-01', '数据科学18-02']:
            return {'mes_title': '班级名称错误', 'mes_cont': ['请输入正确班级哦', '例如：数据科学18-01 数据科学18-02', '亲😙，请不要恶意刷取数据哦。'], 'flag': 0}
        return None

    def major_exception(self):
        '''
            专业输入异常处理
        '''
        if self.student.major not in ['数据科学与大数据技术']:
            return {'mes_title': '专业名称错误', 'mes_cont': ['目前仅支持一个专业哦', '例如：数据科学与大数据技术', '亲😙，请不要恶意刷取数据哦。'], 'flag': 0}
        return None

    def information_exception(self):
        '''
            个人信息输入异常处理
        '''
        if len(self.student.information) == 0:
            return {'mes_title': '个人信息错误', 'mes_cont': ['不要留空哦', '谢谢支持', '亲😙，请不要恶意刷取数据哦。'], 'flag': 0}
        return None

    def deeds_exception(self):
        '''
            个人事迹输入异常处理
        '''
        if len(self.student.deeds) == 0:
            return {'mes_title': '个人事迹错误', 'mes_cont': ['不要留空哦', '谢谢支持', '亲😙，请不要恶意刷取数据哦。'], 'flag': 0}
        return None

    def methods(self):
        '''
            应该各种方法，返回错误，
            需要判断什么错误，可以按照下面格式添加
        '''
        #ip错误
        error_info = self.ip_exception()
        if error_info is not None:
            return error_info
        # id错误
        error_info = self.id_exception()
        if error_info is not None:
            return error_info
        # 姓名错误
        error_info = self.name_exception()
        if error_info is not None:
            return error_info
        # 班级错误
        error_info = self.classes_exception()
        if error_info is not None:
            return error_info
        # 专业错误
        error_info = self.major_exception()
        if error_info is not None:
            return error_info
        # 个人信息错误
        error_info = self.information_exception()
        if error_info is not None:
            return error_info
        # 事迹错误
        error_info = self.deeds_exception()
        if error_info is not None:
            return error_info
        return None
    def main(self):
        '''
            调用主函数
        '''
        return self.methods()
