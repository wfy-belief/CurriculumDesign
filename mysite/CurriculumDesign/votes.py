from django.shortcuts import render
from CurriculumDesign.InfoDeal import InfoDeal
from CurriculumDesign.models import Stu_Info
from IPRECORD.models import IPRECORD


def submit_votes(request):
    students = InfoDeal().return_vote_info()
    return render(request, 'vote.html', {'students': students, 'flag': 1})


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    return ip


def get_info(request):
    request.encoding = 'utf-8'
    ip_list = IPRECORD.object.all().values('id')
    ip = str(get_ip(request))

    if ip in [i['id'] for i in ip_list]:
        return render(request, 'vote-info.html',
                      {'mes_title': '投票失败',
                       'mes_cont': ['投票失败', '您已经投过票了', '请勿重复投票'],
                          'flag': 0})
    iprecord = IPRECORD(id=ip)
    id_list = Stu_Info.object.all().values('id')
    for id in id_list:
        if id['id'] in request.POST:
            InfoDeal().update_vote(str(id['id']))
            iprecord.save()
            return render(request, 'vote-info.html',
                          {'mes_title': '投票成功', 'mes_cont': ['投票成功', '感谢参与'], 'flag': 0})
    return render(request, 'vote-info.html',
                  {'mes_title': '投票失败', 'mes_cont': ['投票失败'], 'flag': 0})
