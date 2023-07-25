### django
什么是MTV：
M 代表模型（Model），即数据存取层。 该层处理与数据相关的所有事务： 如何存取、如何验证有效
T 代表模板(Template)，即表现层。 该层处理与表现相关的决定： 如何在页面或其他类型文档中进行显示。
V 代表视图（View），即业务逻辑层。 该层包含存取模型及调取恰当模板的相关逻辑。 你可以把它看作模型与模板之间的桥梁。


#### 1、	步骤（创建，看setting，）
0
        （1）python manage.py startapp music 依照功能去建立一个app<br>
        （2）在settings.py 里面的INSTALLED_APPS加入项目名(也就是你自己建立的App名称)<br>
        （3）Models建库然后通过数据库迁移语句生成映射，使用django的orm操作数据库<br>
                python manage.py makemigrations//帮你建立一个档案，去记录你更新了哪些东西<br>
                python manage.py migrate//建立档案去更新你的DATABASE<br>
            ORM操作数据库的语句:<br>
                        xxxxx.objects.create(pk=pk, pic=pic, name=name, identity=identity,
                                  category=category)#增<br>
                        xxxxx.filter(id=pk).delete()#删<br>
                        xxxxx.objects.filter(id=id).first().id#查找到这条数据<br>
                        xxxxx.objects.get(id=id).id#查找到这条数据<br>
                        xxxxx.objects.filter(id=pk).update(pic=pic, name=name, identity=identity,<br>
                                  category=category)#更新<br>
                        xxxxx.objects.all().order_by('orderID')#排序<br>
                        xxxxx.objects.all()[(b - 1) * 5:b * 5]#对应分页使用取值<br>
                        xxxxx.objects.count()#总共条数，给分页总共多少条数显示<br>
        （4）之后在templates中使用在templates中的html页面中对应views.py中的绑定，路由配置<br>

#### 2、	使用流程<br>
0        做好路由配置<br>
         views.py里面写方法并且返回给template页面<br>
         写类似于el表达式的标签{%%}里面写python逻辑语句，{{}}里面引用返回值<br>
         大概思路从hw的urls向blog的urls映射，blog的urls使用的是view里面的逻辑<br>


#### 3、    解决跨域问题<br>
##有些版本这个需要安装插件<br>
   在setting里面   'django.middleware.csrf.CsrfViewMiddleware',去掉因为post不好访问<br>
    域名问题解决有两种<br>
      ALLOWED_HOSTS = ['kohang.com',]<br>
    或者ALLOWED_HOSTS=['127.0.0.1']<br>
        CORS_ORIGIN_ALLOW_ALL = False<br>
        CORS_ORIGIN_WHITELIST = (<br>
        'http://localhost:8080',<br>
        )
    <br>
   之后<br>
    MIDDLEWARE = [<br>
        'django.middleware.security.SecurityMiddleware',<br>
        'django.contrib.sessions.middleware.SessionMiddleware',<br>
        'corsheaders.middleware.CorsMiddleware', #注意顺序，必须放在这儿<br>
        'django.middleware.common.CommonMiddleware',<br>
        'django.middleware.csrf.CsrfViewMiddleware',<br>
        'django.contrib.auth.middleware.AuthenticationMiddleware',<br>
        'django.contrib.messages.middleware.MessageMiddleware',<br>
        'django.middleware.clickjacking.XFrameOptionsMiddleware',<br>
    ]


在百度富文本图片得使用，还存在一个路径问题<br>
在vue里面需要使用其中的config两个配置文件主要是server_url<br>
<img></img><br>
