from server import sio
from system.mysql import fnSql
import hashlib
from config import *


@sio.on('login')
def connect(sid, data):
    #服务器接收登录消息，登录data = {username:xxxxx,password:xxxxx(未加密)}
    print(data)
    sql = 'select username,password from user where username="%s";' % data['username']
    sqlres = fnSql(sql)
    

    if len(sqlres)>0:
        #返回来的数据是元祖，（（username,password），）
        md5password = hashlib.md5(bytes(M_md5num.encode('utf-8')))  # 双重加密的加密参数
        md5password.update(bytes(data['password'].encode('utf-8')))

        data['password'] = md5password.hexdigest()
        if sqlres[0][1] == data['password']:
            sio.emit('login','success')
            sql = 'update user set islogin=1,sid="%s" where username = "%s";'%(sid,data['username'])
            fnSql(sql)
        else:
            sio.emit('login','fail')
    else:
        sio.emit('login', 'fail')



    #判断是否账号和密码是否正确

    #如果密码未加密，那么就对密码加密

    #通过数据库查询语句，查找username的数据库密码

    # if 加密密码== 数据库密码：
        #登录成功
        #数据库里用户信息里面他的是否在线字段要修改为真，sid的值要更新
    # else:
        #登录失败
        #密码或者用户名不正确，可以再次尝试，或者是重新注册。
        #没有这个用户，可以尝试注册
        #密码不正确


    print('login')
    print(data)
    
