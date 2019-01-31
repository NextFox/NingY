# -*-coding:utf-8 -*-
import datetime

from aip import AipImageClassify
from django.db.models import Q
from django.shortcuts import render

from ImageDel import models
from ImageDel.models import Img, Imga

# Create your views here.

'''
  """ 你的 APPID AK SK """
  百度识别基础配置信息
'''
APP_ID = '14968824'
API_KEY = 'UHyKYtEZNURQdfcpbeaurr4r'
SECRET_KEY = 'z0WLBTnVfTGReyQScTske1tMny1aq156'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

"""主页跳转"""


def toFirst(request):
    return render(request, 'ImageDel/First.html')


# 自定义图片上传
def uploadImga(request):
    if request.method == 'POST':
        # 编码问题一定要注意

        mee = request.POST.get('description')
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
        models.Imga.objects.create(img_url=request.FILES.get('img'),
                                   img_desc=request.POST['description'] + "--" + nowTime)
    return render(request, 'ImageDel/imgUpload.html')


# 批量图片上传
# def uploadImgs(request):
#    if request.method=='POST':


# 跳转
def toselectImg(request):
    return render(request, 'ImageDel/selectImg.html')


# 根据搜索模糊匹配图片并且下载
def selectImgs(request):
    if request.method == 'POST':
        description = request.POST['description']
        # img_desc__icontains两个_  __
        imgs = models.ImgSuper.objects.filter(img_keywords__icontains=request.POST['description'])
        context = {
            'imgs': imgs
        }
    return render(request, 'ImageDel/showImg.html', context)


'''
#图片下载
def downloadImg(request):
    if request.method=='GET':

'''


# 图片显示函数
def showImgs(request):
    imgs = models.Imga.objects.all()  # 从数据库中取出所有图片
    context = {
        'imgs': imgs,
    }
    return render(request, 'ImageDel/showImg.html', context)


""" 各种 识别  """


# 全部图片显示时 通用物体识别
def GeneralRecognition(request):
    img = models.Img.objects.create(img_url=request.FILES.get('img'))
    imga = get_file_content(img.img_url.path)
    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5

    """ 调用通用物体识别 """
    imgmessage = client.advancedGeneral(imga, options)
    context = {
        'imgurl': img,
        'imgmessagea': imgmessage
    }
    return render(request, 'ImageDel/GeneralRecognition.html', context)


# 1、通用物体识别跳转

def toGeneralRecognition(request):
    return render(request, 'ImageDel/toGeneralRecognition.html')


# 读取图片 调用通用物体识别并保存关键词
def onLineGeneralRecognition(request):
    img_id = request.GET.get('img_id')
    resulta = Imga.objects.get(id=img_id)
    imga = get_file_content(resulta.img_url.path)

    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5
    """ 调用通用物体识别 """
    imgmessagea = client.advancedGeneral(imga, options)
    resa = imgmessagea.get('result')
    ret = [] * 15
    for temp in resa:
        ret.append(temp.get('score'))
        ret.append(temp.get('root'))
        ret.append(temp.get('keyword'))
    models.ImgSuper.objects.create(
        img_url=resulta.img_url,
        img_score1=ret[0],
        img_root1=ret[1],
        img_keyword1=ret[2],
        img_score2=ret[3],
        img_root2=ret[4],
        img_keyword2=ret[5],
        img_score3=ret[6],
        img_root3=ret[7],
        img_keyword3=ret[8],
        img_score4=ret[9],
        img_root4=ret[10],
        img_keyword4=ret[11],
        img_score5=ret[12],
        img_root5=ret[13],
        img_keyword5=ret[14],
        img_keywords=ret[2] + ret[5] + ret[8] + ret[11] + ret[14],
    )
    context = {
        'imgurl': resulta,
        'imgmessagea': imgmessagea,
    }
    return render(request, 'ImageDel/GeneralRecognition.html', context)


# 2、动物识别跳转
def toAnimalRecognition(request):
    return render(request, 'ImageDel/toAnimalRecognition.html')


# 读取图片 调用动物识别并保存关键词
def AnimalRecognition(request):
    img_id = request.GET.get('img_id')
    resulta = Imga.objects.get(id=img_id)
    imga = get_file_content(resulta.img_url.path)
    """ 如果有可选参数 """
    options = {}
    options["top_num"] = 3
    options["baike_num"] = 5
    """ 调用通用物体识别 """
    imgmessagea = client.animalDetect(imga, options)
    context = {
        'imgurl': resulta,
        'imgmessagea': imgmessagea,
    }
    return render(request, 'ImageDel/GeneralRecognition.html', context)


# 3、植物识别跳转
def toPlantRecognition(request):
    return render(request, 'ImageDel/toPlantRecognition.html')


# 读取图片 调用植物识别并保存关键词
def PlantRecognition(request):
    img = models.Img.objects.create(img_url=request.FILES.get('img'))
    imga = get_file_content(img.img_url.path)
    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5
    """ 调用植物识别 """
    imgmessage = client.plantDetect(imga, options)
    context = {
        'imgurl': img,
        'imgmessagea': imgmessage,
    }
    return render(request, 'ImageDel/PlantRecognition.html', context)


# 4、菜品识别跳转
def toDishRecognition(request):
    return render(request, 'ImageDel/toDishRecognition.html')


# 读取图片 调用菜品识别并保存关键词
def DishRecognition(request):
    img = models.Img.objects.create(img_url=request.FILES.get('img'))
    imga = get_file_content(img.img_url.path)
    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5
    """ 调用通用物体识别 """
    imgmessage = client.dishDetect(imga, options)
    context = {
        'imgurl': img,
        'imgmessagea': imgmessage,
    }
    return render(request, 'ImageDel/DishRecognition.html', context)


# 5、车辆识别跳转
def toCarRecognition(request):
    return render(request, 'ImageDel/toCarRecognition.html')


# 读取图片 调用车辆识别并保存关键词
def CarRecognition(request):
    img = models.Img.objects.create(img_url=request.FILES.get('img'))
    imga = get_file_content(img.img_url.path)
    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5
    """ 调用通用物体识别 """
    imgmessagea = client.carDetect(imga, options)
    context = {
        'imgurl': img,
        'imgmessagea': imgmessagea,
    }
    return render(request, 'ImageDel/CarRecognition.html', context)


# 6、商标识别跳转
def toLogoRecognition(request):
    return render(request, 'ImageDel/toLogoRecognition.html')


# 读取图片 调用车辆识别并保存关键词
def LogoRecognition(request):
    img = models.Img.objects.create(img_url=request.FILES.get('img'))
    imga = get_file_content(img.img_url.path)
    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5
    """ 调用通用物体识别 """
    imgmessagea = client.logoSearch(imga, options)
    context = {
        'imgurl': img,
        'imgmessagea': imgmessagea,
    }
    return render(request, 'ImageDel/LogoRecognition.html', context)


# 7、图像主体检测 跳转
def toObjectRecognition(request):
    return render(request, 'ImageDel/toObjectRecognition.html')


# 读取图片 调用图像主体检测
def ObjectRecognition(request):
    img = models.Img.objects.create(img_url=request.FILES.get('img'))
    imga = get_file_content(img.img_url.path)
    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5
    """ 调用通用物体识别 """
    imgmessage = client.objectDetect(imga, options)
    context = {
        'imgurl': img,
        'imgmessagea': imgmessage,
    }
    return render(request, 'ImageDel/ObjectRecognition.html', context)


# 8、地标识别跳转
def toLandMarkRecognition(request):
    return render(request, 'ImageDel/toLandMarkRecognition.html')


# 读取图片 调用地标识别
def LandMarkRecognition(request):
    img = models.Img.objects.create(img_url=request.FILES.get('img'))
    imga = get_file_content(img.img_url.path)
    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5
    """ 调用通用物体识别 """
    imgmessagea = client.landmark(imga, options)
    context = {
        'imgurl': img,
        'imgmessagea': imgmessagea,
    }
    return render(request, 'ImageDel/LandMarkRecognition.html', context)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()