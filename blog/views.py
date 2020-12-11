import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blog.models import Article, index_slider, index_introduction, index_people, Achievementss, people, \
    people_detail_simple, people_education, Peradminuse, Achievementss_project
from django.core.paginator import Paginator
from blog.ueditor_view import get_ueditor_controller





# Create your views here.
get_ueditor_controller

def hello_world(request):
    return HttpResponse("hello world")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title:%s, brief_content: %s,' \
                 'content:%s,article_id: %s,publish_date: %s' % (title,
                                                                 brief_content,
                                                                 content,
                                                                 article_id,
                                                                 publish_date)
    return HttpResponse(return_str)


def get_index_page2(request):
    all_article = index_slider.objects.all()
    introduction = index_introduction.objects.all()[0]
    people = index_people.objects.all()[0]
    return render(request, 'lab/index.html', {
        'article_list': all_article,
        'introduction': introduction,
        'people': people,

    })


def get_about_page(request):
    return render(request, 'lab/about.html', {
        'labname': '扬州大学李志强教授实验室'
    })


def get_achievements_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    all_article = Achievementss.objects.all().order_by('orderID')
    all_achieveproject = Achievementss_project.objects.all().order_by('orderID')
    ##orderID = all_article.orderID
    ##paperinfo = all_article.paperinfo
    ##index = all_article.index
    paginator = Paginator(all_article, 10)#这是对应的论文

    page_num = paginator.num_pages#这是对应的论文
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    return render(request, 'lab/achievements.html', {
        ##'orderID':orderID,
        ##'paperinfo':paperinfo,
        ##'index':index,
        'article_list': page_article_list,
        'page_num': range(1, page_num + 1),
        'curr_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'no': (page - 1) * 10,

        'all_achieveproject': all_achieveproject

    })


def get_contact_page(request):
    return render(request, 'lab/contact.html', {
        'labname': '扬州大学李志强教授实验室'
    })


def get_detail_page(request):
    return render(request, 'lab/detail.html')


def get_list_page(request):
    return render(request, 'lab/list.html')


def get_people_page(request):
    all_article = people.objects.all()
    return render(request, 'lab/people.html', {
        'article_list': all_article,
        'labname': '扬州大学李志强教授实验室'
    })


def get_people_detail_page(request, id):
    # all_people = people_detail_simple.objects.all()
    # all_education = people_education.objects.all()
    curr_people = people_detail_simple.objects.filter(id=id).first()
    # imageuse = people.objects.filter(id=id).values("pic").first()
    imageuse = people.objects.filter(id=id).first()

    return render(request, 'lab/people-detail.html',
                  {
                      'curr_people': curr_people,
                      'imageuse': imageuse
                  })


def get_resources_page(request):
    return render(request, 'lab/resources.html', {
        'labname': '扬州大学李志强教授实验室'
    })


def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print('page param:', page)

    all_article = Article.objects.all()
    top5_article_list = Article.objects.order_by('publish_date')[:10]
    paginator = Paginator(all_article, 9)
    page_num = paginator.num_pages
    print('page num:', page_num)
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    return render(request, 'blog/index.html',
                  {
                      'article_list': page_article_list,
                      'page_num': range(1, page_num + 1),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous_page': previous_page,
                      'top5_article_list': top5_article_list,
                      'no': (page - 1) * 3
                  }
                  )


# def get_people_vue(request):
#     all_article = people.objects.all()
#     all_article = all_article[1]
#     return HttpResponse(all_article)


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            next_index == index
            previous_index == index - 1
        else:
            next_index == index + 1
            previous_index == index - 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      'curr_article': curr_article,
                      'section_list': section_list,
                      'previous_article': previous_article,
                      'next_article': next_article,

                  })


def use_vue(trans):  # 此方法为转类型
    trans = serializers.serialize("json", trans)
    data = json.loads(trans)
    b = []
    for i in data:
        a = i['fields']
        a['pk'] = i['pk']
        b.append(a)

    c = b
    return c


# def use2(trans):
#     a = str(trans, 'utf-8')
#     a = json.loads(a)
#     return a


def get_people_vue(request):
    if request.method == 'GET':
        a = request.GET['pageNum']
        if a == '':
            peopleuse = people.objects.all()
            use = use_vue(peopleuse)  # 我这里的因为没处理好pk所以在方法中以此加入pk
            justthis = use
        else:
            b = int(a)
            peopleuse = people.objects.all()[(b - 1) * 5:b * 5]
            count = people.objects.count()
            use = use_vue(peopleuse)
            for i in use:
                i['count'] = count
            justthis = use
        return JsonResponse(justthis, safe=False)
    if request.method == 'POST':
        define = request.POST['num']
        if define == '2':
            pk = request.POST['pk']
            pic = request.POST['pic']
            name = request.POST['name']
            identity = request.POST['identity']
            category = request.POST['category']
            people.objects.create(pk=pk, pic=pic, name=name, identity=identity,
                                  category=category)  # 这边还没写返回数据
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        elif define == '1':
            pk = int(request.POST['pk'])
            pic = request.POST['pic']
            name = request.POST['name']
            identity = request.POST['identity']
            category = request.POST['category']
            people.objects.filter(id=pk).update(pic=pic, name=name, identity=identity,
                                                  category=category)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        else:
            pk = int(request.POST['pk'])
            people.objects.filter(id=pk).delete()
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)


def gerloginper(request):
    login = Peradminuse.objects.all()
    if request.method == 'GET':
        use = use_vue(login)
        return JsonResponse(use, safe=False)
    if request.method == 'POST':
        if request.POST['num'] == '1':
            a = request.POST['name']
            b = Peradminuse.objects.filter(name=a)
            name = b.first().name
            number = b.first().number
            password = b.first().password
            sum = {}
            sum["name"] = name
            sum["number"] = number
            sum["password"] = password
            return JsonResponse(sum, safe=False)
        elif request.POST['num'] == '2':
            name = request.POST['name']
            number = request.POST['number']
            password = request.POST['password']
            Peradminuse.objects.filter(name=name).update(number=number, name=name, password=password)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        else:
            name = request.POST['name']
            number = request.POST['number']
            password = request.POST['password']
            state = {'state': 'true'}
            Peradminuse.objects.create(name=name,number=number,password=password)
            return JsonResponse(state, safe=False)



def article_content_vue(request):
    if request.method == 'GET':
        a = request.GET['pageNum']
        if a == '':
            article = Article.objects.all()
            use = use_vue(article)#我这里的因为没处理好pk所以在方法中以此加入pk
            justthis = use
        else:
            b = int(a)
            article = Article.objects.all()[(b - 1) * 5:b * 5]
            count = Article.objects.count()
            use = use_vue(article)
            for i in use:
                i['count'] = count
            justthis = use
        return JsonResponse(justthis, safe=False)
    if request.method == 'POST':
        b = request.POST['num']
        if request.POST['num'] == '1':
            id = request.POST['pk']
            title = request.POST['title']
            brief_content = request.POST['brief_content']
            content = request.POST['content']
            publish_date = request.POST['publish_date']
            Article.objects.filter(article_id=id).update(title=title, brief_content=brief_content, content=content,
                                                       publish_date=publish_date)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)

        elif request.POST['num'] == '2':
            title = request.POST['title']
            brief_content = request.POST['brief_content']
            content = request.POST['content']
            publish_date = request.POST['publish_date']
            Article.objects.create(title=title, brief_content=brief_content, content=content,
                                   publish_date=publish_date)  # 这边还没写返回数据
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        else:
            pk = request.POST['pk']
            Article.objects.filter(article_id=pk).delete()
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)


def people_education_vue(request):
    if request.method == 'GET':
        a = request.GET['pageNum']
        if a == '':
            educationuse = people_education.objects.all()
            use = use_vue(educationuse)  # 我这里的因为没处理好pk所以在方法中以此加入pk
            justthis = use
        else:
            b = int(a)
            educationuse = people_education.objects.all()[(b - 1) * 5:b * 5]
            count = people_education.objects.count()
            use = use_vue(educationuse)
            for i in use:
                i['count'] = count
            justthis = use
        return JsonResponse(justthis, safe=False)
    elif request.method == 'POST':
        define = request.POST['num']
        if define == '2':
            pk = request.POST['pk']
            time = request.POST['time']
            education = request.POST['education']
            university = request.POST['university']
            people_education.objects.create(pk=pk, time=time, education=education, university=university)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        # 这边还没写返回数据
        elif define == '1':
            pk = request.POST['pk']
            time = request.POST['time']
            education = request.POST['education']
            university = request.POST['university']
            people_education.objects.filter(id=pk).update(time=time,education=education, university=university)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        else:
            pk = request.POST['pk']
            people_education.objects.filter(id=pk).delete()
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)


def people_simples_vue(request):
    if request.method == 'GET':
        a = request.GET['pageNum']
        if a == '':
            peoplesimple = people_detail_simple.objects.all()
            use = use_vue(peoplesimple)  # 我这里的因为没处理好pk所以在方法中以此加入pk
            justthis = use
        else:
            b = int(a)
            peoplesimple = people_detail_simple.objects.all()[(b - 1) * 5:b * 5]
            count = people_detail_simple.objects.count()
            use = use_vue(peoplesimple)
            for i in use:
                i['count'] = count
            justthis = use
        return JsonResponse(justthis, safe=False)
    if request.method == 'POST':
        define = request.POST['num']
        if define == '2':
            pk = request.POST['pk']
            name = request.POST['name']
            identity = request.POST['identity']
            major = request.POST['major']  # 这里暂时不为主键
            subject = request.POST['subject']  # 这里暂时不为主键
            description = request.POST['description']  # 这里暂时
            people_detail_simple.objects.create(pk=pk, name=name, identity=identity, major=major, subject=subject,
                                                description=description)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        # 这边还没写返回数据
        elif define == '1':
            pk = request.POST['pk']
            name = request.POST['name']
            identity = request.POST['identity']
            major = request.POST['major']  # 这里暂时不为主键
            subject = request.POST['subject']  # 这里暂时不为主键
            description = request.POST['description']  # 这里暂时不为主键
            people_detail_simple.objects.filter(id=pk).update(name=name, identity=identity, major=major, subject=subject,
                                                                  description=description)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        else:
            pk = request.POST['pk']
            people_detail_simple.objects.filter(id=pk).delete()
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)


def index_slider_vue(request):
    if request.method == 'GET':
        a = request.GET['pageNum']
        if a == '':
            index_slideruse = index_slider.objects.all()
            use = use_vue(index_slideruse)  # 我这里的因为没处理好pk所以在方法中以此加入pk
            justthis = use
        else:
            b = int(a)
            index_slideruse = index_slider.objects.all()[(b - 1) * 5:b * 5]
            count = index_slider.objects.count()
            use = use_vue(index_slideruse)
            for i in use:
                i['count'] = count
            justthis = use
        return JsonResponse(justthis, safe=False)
    if request.method == 'POST':
        define = request.POST['num']
        if define == '2':
            slider_image = request.POST['slider_image']
            slider_title = request.POST['slider_title']
            slider_description = request.POST['slider_description']  # 这里暂时不为主键
            index_slider.objects.create(slider_image=slider_image, slider_description=slider_description,
                                        slider_title=slider_title)
            # 这边还没写返回数据
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        elif define == '1':
            pk = request.POST['pk']
            slider_image = request.POST['slider_image']
            slider_title = request.POST['slider_title']
            slider_description = request.POST['slider_description']
            # 这里暂时不为主键
            index_slider.objects.filter(slider_id=pk).update(slider_title=slider_title,
                                                                          slider_description=slider_description,
                                                                          slider_image=slider_image)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        else:
            pk = request.POST['pk']
            index_slider.objects.filter(slider_id=pk).delete()
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)


def index_people_vue(request):
    if request.method == 'GET':
        a = request.GET['pageNum']
        if a == '':
            indexpe = index_people.objects.all()
            use = use_vue(indexpe)  # 我这里的因为没处理好pk所以在方法中以此加入pk
            justthis = use
        else:
            b = int(a)
            indexpe = index_people.objects.all()[(b - 1) * 5:b * 5]
            count = index_people.objects.count()
            use = use_vue(indexpe)
            for i in use:
                i['count'] = count
            justthis = use
        return JsonResponse(justthis, safe=False)
    if request.method == 'POST':
        define = request.POST['num']
        if define == '2':
            people_pic = request.POST['people_pic']
            tutor = request.POST['tutor']
            tutor_en = request.POST['tutor_en']  # # 这里暂时
            index_people.objects.create(people_pic=people_pic, tutor=tutor, tutor_en=tutor_en)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        # 这边还没写返回数据
        elif define == '1':
            pk = request.POST['pk']
            people_pic = request.POST['people_pic']
            tutor = request.POST['tutor']
            tutor_en = request.POST['tutor_en']  # 这里暂时不为主键
            index_people.objects.filter(id=pk).update(people_pic=people_pic,tutor=tutor, tutor_en=tutor_en)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        else:
            pk = request.POST['pk']
            index_people.objects.filter(id=pk).delete()
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)


def index_introduction_vue(request):
    if request.method == 'GET':
        a = request.GET['pageNum']
        if a == '':
            intro = index_introduction.objects.all()
            use = use_vue(intro)  # 我这里的因为没处理好pk所以在方法中以此加入pk
            justthis = use
        else:
            b = int(a)
            intro = index_introduction.objects.all()[(b - 1) * 5:b * 5]
            count = index_introduction.objects.count()
            use = use_vue(intro)
            for i in use:
                i['count'] = count
            justthis = use
        return JsonResponse(justthis, safe=False)
    if request.method == 'POST':
        define = request.POST['num']
        if define == '2':
            introduction = request.POST['introduction']
            index_introduction.objects.create(introduction=introduction)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
            # 这边还没写返回数据
        elif define == '1':
            pk = int(request.POST['pk'])
            introduction = request.POST['introduction']
            index_introduction.objects.filter(id=pk).update(introduction=introduction)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        else:
            pk = request.POST['pk']
            index_introduction.objects.filter(id=pk).delete()
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)


def get_achievements_vue(request):

    # if request.method == 'GET':
    #     use = use_vue(achieve)
    #     return JsonResponse(use, safe=False)
    if request.method == 'GET':
        a = request.GET['pageNum']
        if a == '':
            achieve = Achievementss.objects.all()
            use = use_vue(achieve)#我这里的因为没处理好pk所以在方法中以此加入pk
            justthis = use
        else:
            b = int(a)
            achieve = Achievementss.objects.all()[(b - 1) * 5:b * 5]
            count = Achievementss.objects.count()
            use = use_vue(achieve)
            for i in use:
                i['count'] = count
            justthis = use
        return JsonResponse(justthis, safe=False)
    if request.method == 'POST':
        define = request.POST['num']
        if define == '2':
            orderID = request.POST['orderID']
            paperinfo = request.POST['paperinfo']
            index = request.POST['index']
            pdf_link = request.POST['pdf_link']
            index_link = request.POST['index_link']
            index2 = request.POST['index2']
            index3 = request.POST['index3']
            index_link2 = request.POST['index_link2']
            index_link3 = request.POST['index_link3']
            Achievementss.objects.create(orderID=orderID, paperinfo=paperinfo,
                                         index=index, pdf_link=pdf_link, index_link=index_link, index2=index2,
                                         index3=index3, index_link2=index_link2, index_link3=index_link3)  # 这边还没写返回数据
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        elif define == '1':
            orderID = request.POST['orderID']
            paperinfo = request.POST['paperinfo']
            index = request.POST['index']
            pdf_link = request.POST['pdf_link']
            index_link = request.POST['index_link']
            index2 = request.POST['index2']
            index3 = request.POST['index3']
            index_link2 = request.POST['index_link2']
            index_link3 = request.POST['index_link3']
            Achievementss.objects.filter(orderID=orderID).update(orderID=orderID, paperinfo=paperinfo,
                                                                 index=index, pdf_link=pdf_link, index_link=index_link,
                                                                 index2=index2, index3=index3, index_link2=index_link2,
                                                                 index_link3=index_link3)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        else:
            orderID = request.POST['orderID']
            Achievementss.objects.filter(orderID=orderID).delete()
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)


def project_vue(request):
    if request.method == 'GET':
        a = request.GET['pageNum']
        if a == '':
            indexpe = Achievementss_project.objects.all()
            use = use_vue(indexpe)  # 我这里的因为没处理好pk所以在方法中以此加入pk
            justthis = use
        else:
            b = int(a)
            indexpe = Achievementss_project.objects.all()[(b - 1) * 5:b * 5]
            count = Achievementss_project.objects.count()
            use = use_vue(indexpe)
            for i in use:
                i['count'] = count
            justthis = use
        return JsonResponse(justthis, safe=False)
    if request.method == 'POST':
        define = request.POST['num']
        if define == '2':
            orderID = request.POST['orderID']
            projectname = request.POST['projectname']
            projecturl = request.POST['projecturl']
            direction = request.POST['direction']
            peoplenum = request.POST['peoplenum']
            Achievementss_project.objects.create(orderID=orderID, projectname=projectname, projecturl=projecturl, direction=direction,peoplenum=peoplenum )
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        # 这边还没写返回数据
        elif define == '1':
            pk = request.POST['pk']
            orderID = request.POST['orderID']
            projectname = request.POST['projectname']
            projecturl = request.POST['projecturl']
            direction = request.POST['direction']
            peoplenum = request.POST['peoplenum']
            Achievementss_project.objects.filter(ID=pk).update(orderID=orderID,projectname=projectname,projecturl=projecturl, direction=direction,peoplenum=peoplenum)
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)
        else:
            pk = request.POST['pk']
            Achievementss_project.objects.filter(ID=pk).delete()
            state = {'state': 'true'}
            return JsonResponse(state, safe=False)


def getimageuse(request):
    a = request
    pass



def testPDF(request):
    abc = request
    print(request)
    state = {'state': 'true'}
    return JsonResponse(state, safe=False)


