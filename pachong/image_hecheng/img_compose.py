from PIL import Image  # 图片处理库 pillow
import os  # 文件处理库

im = Image.open('./images/清纯长发美女人像近照电脑壁纸下载.jpg')
w, h = im.size
image_row = 3  # 行
image_col = 3  # 列
names = os.listdir('./images')  # 所有的名字

new_img = Image.new('RGB', (image_col * w, image_row * h))  # 新图片

for y in range(image_row):
    for x in range(image_col):
        o_img = Image.open('./images/' + names[image_col * y + x])  # 打开要合成的图片
        new_img.paste(o_img, (x * w, y * h))
new_img.save('new_img.jpg')
