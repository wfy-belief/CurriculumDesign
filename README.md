# 项目部署指南

Ubuntu 18.04 Linux系统

### 防火墙

https://www.myfreax.com/how-to-disable-firewall-on-ubuntu-18-04/

使用`ufw disable`命令：

```bash
sudo ufw disable
```

输出将如下所示：

```bash
Firewall stopped and disabled on system startup
```

以上命令将停止并禁用防火墙，但不会删除防火墙规则。下次启用防火墙时，将加载相同的规则。

如果要禁用防火墙并删除所有防火墙规则，请使用`ufw reset`命令：

```bash
sudo ufw reset
```

系统会提示您是否要继续操作：

```bash
Resetting all rules to installed defaults. This may disrupt existing ssh
connections. Proceed with operation (y|n)? 
```

```bash
Backing up 'user.rules' to '/etc/ufw/user.rules.20190122_115214'
Backing up 'before.rules' to '/etc/ufw/before.rules.20190122_115214'
Backing up 'after.rules' to '/etc/ufw/after.rules.20190122_115214'
Backing up 'user6.rules' to '/etc/ufw/user6.rules.20190122_115214'
Backing up 'before6.rules' to '/etc/ufw/before6.rules.20190122_115214'
Backing up 'after6.rules' to '/etc/ufw/after6.rules.20190122_115214'
```

当您要还原所有更改并重新开始时，重置UFW防火墙非常有用。

### 环境

安装环境

```
apt-get remove python3
apt-get update
apt-get upgrade
apt install python3.7
```

将python3指向python3.7

```
cd /usr/bin
rm /usr/bin/python3
ln -s python3.7 python3
```

![image-20200617182151414](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images/img/image-20200617182151414.png)

3、pip安装

```
apt-get install python3-pip
```

安装django

```
pip3 install pyecharts
pip3 install django
pip3 install pymysql
pip3 install django_echarts
```

### 安装MySQL

卸载方法https://ywnz.com/linuxysjk/3141.html

https://blog.csdn.net/qq_42468130/article/details/88595418

```
apt-get install mysql-server -y
```

进入MySQL第一次输入密码即为默认

```
mysql -u root -p
```

安装库

```
create database info default charset=utf8;
```

新建用户赋予权限

```
create user 'user01'@'%' identified by '666666';
grant all privileges on *info* to 'user01'@'%' identified by '666666';
flush privileges;
```

配置文件

![image-20200617184418095](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images/img/image-20200617184418095.png)

### 安装git和下载项目

```
apt install git
```

```
git clone https://github.com/wfy-belief/CurriculumDesign.git
```

修改数据库配置

```
cd CurriculumDesign/mysite/mysite
vim settings.py
```

![image-20200617185313439](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images/img/image-20200617185313439.png)

最后一个是本机IP

![image-20200617185515909](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images/img/image-20200617185515909.png)

修改即可

### 创建表结构

```
cd ..
python3 manage.py migrate 
```

![image-20200617185904521](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images/img/image-20200617185904521.png)

出现如下错误，我们修改原码，注释下面的两行

```
vim /usr/local/lib/python3.7/dist-packages/django/db/backends/mysql/base.py
```

![image-20200617190047542](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images/img/image-20200617190047542.png)

```
python3 manage.py migrate 
```

![image-20200617190701533](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images/img/image-20200617190701533.png)

出现报错

```
/etc/mysql/mysql.conf.d
```

```
vim mysqld.cnf 
```

![image-20200617190759061](https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images/img/image-20200617190759061.png)

注释掉

```
python3 manage.py migrate 
```

### 后台管理员

```
python3 manage.py createsuperuser
```



### 运行服务

```
python3 manage.py runserver 0:8889
```



### 异常处理类的设计

| 名字                         | 备注                 |
| ---------------------------- | -------------------- |
| self.ip_exception()          | 限制IP以及返回IP信息 |
| self.id_exception()          | 判断学号格式错误     |
| self.name_exception()        | 判断名字格式错误     |
| self.classes_exception()     | 判断班级格式错误     |
| self.major_exception()       | 判断专业信息         |
| self.information_exception() | 个人信息审核         |
| self.deeds_exception()       | 个人事迹审核         |

### 信息处理设计

| 名字                    | 备注                       |
| ----------------------- | -------------------------- |
| class Student(object):  | 学生信息类/与数据格式相同  |
| class InfoDeal(object): | 信息处理类，下面是成员变量 |
| self.students           | 存储学生类/每个学生信息    |
| self.hash_list          | 构建哈希表                 |
| self.max_length         | 哈希表最大长度             |
| self.hash_mod           | 哈希表构建方法             |
| self.hash_table         | 存储哈希表                 |
| self.root               | 构建二叉排序树             |
| self.rank_list          | 排名信息                   |

### 哈希表构建

| 方法                        | 备注       |
| --------------------------- | ---------- |
| def build_hash(*self*):     | 开放寻址法 |
| find_hash(*self*, *value*): | 查找关键字 |

### 冲突消解

### 二叉排序树

| 方法                                  | 备注                     |
| ------------------------------------- | ------------------------ |
| build_sort_tree(*self*):              | 构建排序二叉树           |
| insert_tree(*self*, *node*, *value*): | 插入节点                 |
| mid_order_tree(*self*, *node*):       | 中序遍历后十即为排名前10 |

### 提供API接口

| 方法                            | 备注                                              |
| ------------------------------- | ------------------------------------------------- |
| return_rank_info(*self*):       | 从二叉排序树遍历的序列中返回排名需要的信息/数据   |
| return_vote_info(*self*):       | 从二叉排序中遍历的序列中返回投票需要的信息/数据   |
| update_vote(*self*, **values*): | 在哈希表中查找数据/存在进行数据的更新处理/votes++ |

