import os

dir1 = r'/home/silverbullet/Videos/MSR_Video_Description_Corpus/YouTubeClips'  # 图片文件存放地址
txt1 = 'list.txt' # 图片文件名存放txt文件地址
# txt1 = r'\home\silverbullet\Videos\msr_video_description_corpus\picture.txt'  # 图片文件名存放txt文件地址
f1 = open(txt1, 'a+')  # 打开文件流
# for filename in os.listdir(dir1):
#     f1.write(filename.rstrip('.jpg'))  # 只保存名字，去除后缀.jpg
#     f1.write("\n")  # 换行
for root,dirs,files in os.walk(dir1):
    for file in files:
        print(os.path.join(root,file))
        x = os.path.join(root,file)
        f1.write(x)
        f1.write("\n")
f1.close()  # 关闭文件流