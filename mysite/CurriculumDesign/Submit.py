from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from CurriculumDesign.models import Stu_Info
from CurriculumDesign.MyException import MyException
from CurriculumDesign.InfoDeal import InfoDeal
def lock_IP(request):
    # print(type(Stu_Info.object.all()[0].id))
    # test.build_hash()
    # print('查找的位置是', test.find_hash('13'))
    # ssss
    IP_list = Stu_Info.object.all().values('ip')
    if str(get_ip(request)) not in [i['ip'] for i in IP_list] or str(get_ip(request)) == '127.0.0.1':
        return  {'flag': 1}
    mes_title = 'IP冲突'
    mes_cont = ['您已经提交过表单了','感谢您的提交参与','课设答辩后资料统一发到您的邮箱']

    mes_cont.append('请勿重复提交')
    return  {'mes_title':mes_title, 'mes_cont':mes_cont, 'flag':0}

# 表单
def submit_form(request):
    # 锁定IP如果该IP提交过信息，则该IP不可以使用
    return render(request, 'submit.html',lock_IP(request))


# ip通常访问者的IP就在其中，所以我们可以用下列方法获取用户的真实IP：

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    return ip

# 接收请求数据


def submit_to_mysql(request):
    request.encoding = 'utf-8'
    id = request.POST['id']
    name = request.POST['name']
    classes = request.POST['classes']
    major = request.POST['major']
    information = request.POST['information']
    deeds = request.POST['deeds']
    is_nominated = True
    is_deleted = False
    votes = 0
    ip = str(get_ip(request))
    # submit_time = timezone.now
    # last_update_time = timezone.now
    student = Stu_Info(
        id=id,
        name=name,
        classes=classes,
        major=major,
        information=information,
        deeds=deeds,
        is_nominated=is_nominated,
        is_deleted=is_deleted,
        votes=votes,
        ip=ip
    )
    # my_exception(request, student)
    error_info = MyException(student).main()
    if error_info is not None:
        return render(request, 'submit-info.html',error_info)

    student.save()
    mes_title = '提交成功'
    mes_cont = ["♥提交成功♥", str(get_ip(request)), '谢谢支持！']
    return render(request, 'submit-info.html',
            {'mes_title':mes_title, 'mes_cont':mes_cont, 'flag':0})




