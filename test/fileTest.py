# 文件生成测试
import os.path

dirs = './file/'
if not os.path.exists(dirs):
    os.makedirs(dirs)

filename = './file/testEntity.java'
if not os.path.exists(filename):
    os.mknod(filename)

if __name__ == '__main__':
    pass

