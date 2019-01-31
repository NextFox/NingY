from baiduai.AipImageClassify import client

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


""" 调用通用物体识别 """
image = get_file_content('N:/photoes/rec/dish.jpg')
client.advancedGeneral(image);

""" 如果有可选参数 """
options = {}
options["baike_num"] = 5

""" 带参数调用通用物体识别 """
res = client.advancedGeneral(image, options)
resa = res.get('result')
result = [] * 15
for temp in resa:
    # for i in temp:
    print(temp.get('score'))
    print(temp.get('root'))
    print(temp.get('keyword'))
    result.append(temp.get('score'))
    result.append(temp.get('root'))
    result.append(temp.get('keyword'))
    # print(temp["i"])

#for i in result:
print(result[11])
print(res.get('result'))
