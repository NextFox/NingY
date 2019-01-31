from django.urls import path

from ImageDel import views

urlpatterns = [
    # path('',views.index,name='index')

    # 首页跳转
    path('first', views.toFirst, name='first'),

    # 图片上传
    path('uploadImg', views.uploadImga, name='uploadimg'),

    # 图片显示相关
    # 1、查询所有图片
    path('showImgs', views.showImgs, name='showImgs'),
    # 2、模糊查询图片
    path('toselectImg', views.toselectImg, name='toselectImg'),
    path('selectImgs', views.selectImgs, name='selectImgs'),

    # 识别相关
    path('onLineGeneralRecognition', views.onLineGeneralRecognition, name='onLineGeneralRecognition'),
    # 1、通用物品识别
    path('toGeneralRecognition', views.toGeneralRecognition, name='toGeneralRecognition'),
    path('GeneralRecognition', views.GeneralRecognition, name='GeneralRecognition'),

    # 2、动物识别
    path('toAnimalRecognition', views.toAnimalRecognition, name='toAnimalRecognition'),
    path('AnimalRecognition', views.AnimalRecognition, name='AnimalRecognition'),

    # 3、植物识别
    path('toPlantRecognition', views.toPlantRecognition, name='toPlantRecognition'),
    path('PlantRecognition', views.PlantRecognition, name='PlantRecognition'),
    # 4、菜品识别
    path('toDishRecognition', views.toDishRecognition, name='toDishRecognition'),
    path('DishRecognition', views.DishRecognition, name='DishRecognition'),

    # 5、车辆识别
    path('toCarRecognition', views.toCarRecognition, name='toCarRecognition'),
    path('CarRecognition', views.CarRecognition, name='CarRecognition'),

    # 6、logo商标识别
    path('toLogoRecognition', views.toLogoRecognition, name='toLogoRecognition'),
    path('LogoRecognition', views.LogoRecognition, name='LogoRecognition'),

    # 7、图像主体检测
    path('toObjectRecognition', views.toObjectRecognition, name='toObjectRecognition'),
    path('ObjectRecognition', views.ObjectRecognition, name='ObjectRecognition'),

    # 8、地标识别
    path('toLandMarkRecognition', views.toLandMarkRecognition, name='toLandMarkRecognition'),
    path('LandMarkRecognition', views.LandMarkRecognition, name='LandMarkRecognition'),

]
