import os
from PIL import Image
import numpy as np
import tensorflow as tf

# 导入图像数据
# 测试外部图片
model = tf.keras.models.load_model('my_model.h5')
model.summary()  # 看一下网络结构

print("模型加载完成！")
dict_label = {0: '汽车', 1: '饮料瓶'}


def read_image(paths):
    os.listdir(paths)
    filelist = []
    for root, dirs, files in os.walk(paths):
        for file in files:
            if os.path.splitext(file)[1] == ".jpg":
                filelist.append(os.path.join(root, file))
    return filelist


def im_xiangsu(paths):
    for filename in paths:
        try:
            im = Image.open(filename)
            newim = im.resize((128, 128))
            newim.save('F:/CNN/test/' + filename[12:-4] + '.jpg')
            print('图片' + filename[12:-4] + '.jpg' + '像素转化完成')
        except OSError as e:
            print(e.args)


def im_array(paths):
    im = Image.open(paths[0])
    im_L = im.convert("L")  # 模式L
    Core = im_L.getdata()
    arr1 = np.array(Core, dtype='float32') / 255.0
    list_img = arr1.tolist()
    images = np.array(list_img).reshape(-1, 128, 128, 1)
    return images


test = 'F:/CNN/test/'  # 你要测试的图片的路径
filelist = read_image(test)
im_xiangsu(filelist)
img = im_array(filelist)
# 预测图像
predictions_single = model.predict(img)
print("预测结果为:", dict_label[np.argmax(predictions_single)])
# 这里返回数组中概率最大的那个
print(predictions_single)
