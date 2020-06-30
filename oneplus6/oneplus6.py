import win32con
import re

import time
import datetime
import ctypes
import sys, os, subprocess
from subprocess import Popen, PIPE
import importlib, sys
import win32api
import random
import pyperclip
import win32clipboard as wincld

import sys, os, subprocess
from subprocess import Popen, PIPE
import importlib, sys
import win32api
import random
import win32clipboard as wincld
from gtts import gTTS
import os
from moviepy.editor import *
from moviepy.editor import VideoFileClip
from moviepy import editor
from PIL import Image, ImageDraw, ImageFont
import text_to_image
from PIL import Image, ImageFont, ImageDraw
import os
from PIL import Image, ImageFont, ImageDraw
import datetime
from moviepy.editor import *

importlib.reload(sys)
import subprocess
import re
import os
import ffmpeg
import aircv as ac
import datetime
import math
import win32api
import win32con
import time
import ctypes
import webbrowser
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import cv2
import numpy as np
import time
from PIL import ImageGrab
from moviepy.editor import *
import shutil
import pyttsx3
import comtypes.client
import comtypes.client


# my_img_height为小图片的高度，即为每次增加的像素,148
# 1080* 2280
def matchImg_up_down(imgsrc, imgobj, my_img_height):
    img = cv2.imread(imgsrc)
    y0, y1, x0, x1 = 0, 0, 0, 1080
    for step_y1 in range(my_img_height, 2280, my_img_height):
        cropped = img[y0:step_y1, x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
        cv2.imwrite('tmp_' + imgsrc, cropped)
        if ifmatchImgClick('tmp_' + imgsrc, imgobj):
            # print('找到了，' + str(step_y1))
            if matchImg('tmp_' + imgsrc, imgobj) is not None:
                # myx = str(matchImg('tmp_' + imgsrc, imgobj)['result'][0])
                # myy = str(matchImg('tmp_' + imgsrc, imgobj)['result'][1])
                # os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                # time.sleep(4)
                myx = str(matchImg('tmp_' + imgsrc, imgobj)['result'][0])
                myy = str(matchImg('tmp_' + imgsrc, imgobj)['result'][1])
                myx_off = str(matchImg('tmp_' + imgsrc, imgobj)['result'][0] - 935 )
                os.popen('adb -s 66819679 shell input tap ' + myx_off + ' ' + myy, 'r', 1)
                time.sleep(4)
            break
        else:
            pass


# if对比图片并点击
def ifmatchImgClick(myScreencap, mypng):
    if matchImg(myScreencap, mypng) is not None:
        print("！" + mypng + str(
            matchImg(myScreencap, mypng)['result'][0]) + ',' + str(
            matchImg(myScreencap, mypng)['result'][1]))
        myx = str(matchImg(myScreencap, mypng)['result'][0])
        myy = str(matchImg(myScreencap, mypng)['result'][1])
        # click(int(float(myx)), int(float(myy)))
        # print("-------------对比图片return True")
        return True
        # time.sleep(2)
    else:
        # print("-------------对比图片return False")
        return False

# 截图
def screencap():
    time.sleep(1)
    try:
        # 截图
        os.popen('adb -s 66819679 shell screencap -p /storage/emulated/0/Pictures/Screenshots/phoneScreencap.png')
        time.sleep(3)
        print("截图")
        # 发送到电脑
        os.popen('adb -s 66819679 pull /storage/emulated/0/Pictures/Screenshots/phoneScreencap.png')
        time.sleep(3)
    except Exception as e:
        print(e)
        print("这里有个异常adb -s 66819679 shell screencap")


# 打开浏览器
# webbrowser.open(url, new=0, autoraise=True)
# 在系统的默认浏览器中访问url地址，
# 如果new = 0, url会在同一个 浏览器窗口中打开；
# 如果new = 1，新的浏览器窗口会被打开;
# 如果new = 2 新的浏览器tab会被打开
def web_open(url):
    print('    # 打开' + url)
    webbrowser.open(url, new=0)
    time.sleep(10)


# 单击
def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    time.sleep(3)


# 模拟键盘输入字符串
def string_input(my_string):
    k.type_string(my_string)
    time.sleep(1)


# 对比图片并点击
def matchImgClick(myScreencap, mypng):
    if matchImg(myScreencap, mypng) is not None:
        print("-------------点击按钮！" + mypng + str(
            matchImg(myScreencap, mypng)['result'][0]) + ',' + str(
            matchImg(myScreencap, mypng)['result'][1]))
        myx = str(matchImg(myScreencap, mypng)['result'][0])
        myy = str(matchImg(myScreencap, mypng)['result'][1])
        click(int(float(myx)), int(float(myy)))
        time.sleep(3)
        print("-------------结束点击按钮。")


# 截图
def PrtSc(mypng):
    print("截图")
    im = ImageGrab.grab()
    # 放到pic文件夹下
    im.save(mypng)
    time.sleep(1)


# # 组合按键
def KEY_KEY(key1, key2):
    ctypes.windll.user32.keybd_event(key1, 0, 0, 0)
    ctypes.windll.user32.keybd_event(key2, 0, 0, 0)
    # https://blog.csdn.net/zhanglidn013/article/details/35988381
    # https://docs.microsoft.com/zh-cn/windows/desktop/inputdev/virtual-key-codes
    ctypes.windll.user32.keybd_event(key2, 0, win32con.KEYEVENTF_KEYUP, 0)
    ctypes.windll.user32.keybd_event(key1, 0, win32con.KEYEVENTF_KEYUP, 0)


# 按下一个按钮
def KEY(key1):
    ctypes.windll.user32.keybd_event(key1, 0, 0, 0)
    # https://blog.csdn.net/zhanglidn013/article/details/35988381
    # https://docs.microsoft.com/zh-cn/windows/desktop/inputdev/virtual-key-codes
    ctypes.windll.user32.keybd_event(key1, 0, win32con.KEYEVENTF_KEYUP, 0)


# 对比两张图，找到坐标。
def matchImg(imgsrc, imgobj):  # imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc, imobj,
                                    0.9)
    # 0.9、confidence是精度，越小对比的精度就越低 {'confidence': 0.5435812473297119,
    # 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.alipay_leave0)}
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
    return match_result


# 删除文件夹下面的所有文件(只删除文件,不删除文件夹)
import os
import shutil


# python删除文件的方法 os.remove(path)path指的是文件的绝对路径,如：
# os.remove(r"E:\code\practice\data\1.py")#删除文件
# os.rmdir(r"E:\code\practice\data\2")#删除文件夹（只能删除空文件夹）
# shutil.rmtree(r"E:\code\practice\data\2")#删除文件夹
# path_data = "E:\code\practice\data"#
def del_file(path_data):
    for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "\\" + i  # 当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:  # os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)


def phone_detect(fo_count):
    path_data = "./Camera"
    del_file(path_data)
    # path_data = "./video_cut"
    # del_file(path_data)
    print('home')
    os.popen('adb -s 66819679 shell input tap 540 1851')
    time.sleep(4)

    print('打开抖音')
    os.popen('adb -s 66819679 shell input tap 880 1525')
    time.sleep(6)

    # print('打开第一个视频')
    # os.popen('adb -s 66819679 shell input tap 185 972')
    # os.popen('adb -s 66819679 shell input tap 185 1583')

    time.sleep(4)

    for my_index in range(0, fo_count, 1):
        print('第' + str(my_index) + '个------------------------')
        print('分享')
        os.popen('adb -s 66819679 shell input tap 973 1228')
        time.sleep(3)

        screencap()
        try:
            if matchImg('phoneScreencap.png', 'comment.png') is not None:
                print("comment！" + str(
                    matchImg('phoneScreencap.png', 'comment.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'comment.png')['result'][1]))
                print('点击返回')
                os.popen('adb -s 66819679 shell input tap 838 1850')
                time.sleep(4)
        except Exception as e:
            print(e)
            print("这里有个异常")

        screencap()
        try:
            # 点击下载
            if matchImg('phoneScreencap.png', 'dl.png') is not None:
                print("dl！" + str(
                    matchImg('phoneScreencap.png', 'dl.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'dl.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'dl.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'dl.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(10)

        except Exception as e:
            print(e)
            print("这里有个异常")

        print('点击暂停')
        os.popen('adb -s 66819679 shell input tap 514 586')
        time.sleep(2)

        print('上划/下一个视频')
        os.popen('adb -s 66819679 shell input swipe 491 1304 491 333')
        time.sleep(3)

        # print('下划/上一个视频')
        # os.popen('adb -s 66819679 shell input swipe 491 333 491 1304')
        # time.sleep(3)

        print('开始传文件到电脑')
        os.popen('adb -s 66819679 pull /storage/emulated/0/DCIM/Camera/ ')
        time.sleep(4)
        print('开始删除手机里的文件')
        os.popen('adb -s 66819679 shell rm /storage/emulated/0/DCIM/Camera/*.mp4')
        print('结束')
        time.sleep(5)


def get_length_ffmpeg(filename):
    t = 0

    for r, ds, fs in os.walk('.'):
        for f in fs:
            if f.endswith('mp4'):
                file = os.path.join(r, f)
                t = t + float(ffmpeg.probe(file)['format']['duration'])
    print(t / 60 / 60)


def video_concat(my_final_name):
    mytime = datetime.datetime.now()
    print("现在时间（）：" + str(mytime.date()) + str(mytime.hour) + str(mytime.minute))
    # my_time_date_minute = str(mytime.date()) + str(mytime.hour) + str(mytime.minute)
    my_cmd_concat = r'ffmpeg -f concat -i ./Camera/filelist.txt -c copy datetime.mp4'
    my_cmd_concat = my_cmd_concat.replace('datetime', my_final_name)
    os.system(my_cmd_concat)


def video_concat_py(my_final_name):
    # 定义一个数组
    L = []

    # 访问 video 文件夹 (假设视频都放在这里面)
    for root, dirs, files in os.walk("./Camera"):
        # 按文件名排序
        files.sort()
        # 遍历所有文件
        for file in files:
            # 如果后缀名为 .mp4
            if os.path.splitext(file)[1] == '.mp4':
                # 拼接成完整路径
                filePath = os.path.join(root, file)
                # 载入视频
                video = VideoFileClip(filePath)
                # 添加到数组
                L.append(video)

    # 拼接视频
    final_clip = concatenate_videoclips(L)

    # 生成目标视频文件
    final_clip.to_videofile(my_final_name + ".mp4", fps=24, remove_temp=True)


def sort_file_by_time(file_path):
    files = os.listdir(file_path)
    if not files:
        return
    else:
        files = sorted(files, key=lambda x: os.path.getmtime(
            os.path.join(file_path, x)))  # 格式解释:对files进行排序.x是files的元素,:后面的是排序的依据.   x只是文件名,所以要带上join.
        return files


def produce_file(my_final_name_file_1, my_final_name_file):
    my_sort_files = sort_file_by_time("./Camera")
    for i in range(len(my_sort_files)):
        my_old_name = './Camera/' + str(my_sort_files[i])
        my_new_name = './Camera/' + str(i + 1) + ".mp4"
        os.rename(my_old_name, my_new_name)

    # 判断文件是否存在
    if os.path.exists('./Camera/filelist.txt'):
        os.remove('./Camera/filelist.txt')
    else:
        print("要删除的文件不存在！a+ 去生成")
    # # 写到txt文本文件
    # for i in range(len(my_sort_files)):
    #     with open('./Camera/filelist.txt', 'a+') as f:
    #         f.write('file ' + '\'' + my_sort_files[i] + '\'' + "\n")

    # 对每一个视频进行处理，去掉最后3秒
    my_sort_files = sort_file_by_time("./Camera")
    for i in range(len(my_sort_files)):
        video_cut(my_sort_files[i])

    video_concat(my_final_name_file)

    time.sleep(4)
    print('home')
    os.popen('adb -s 66819679 shell input tap 540 1851')

    upload_video(my_final_name_file_1, my_final_name_file)


def video_cut(path_name):
    video_duration = int(get_length(path_name))
    if video_duration != 999:

        my_end_time = video_duration - 3
        if my_end_time <= 9:
            print('my_end_time' + str(my_end_time))
            my_end_time = '0' + str(my_end_time)

        # my_cmd = r'ffmpeg -y -i D:/myPython/20200303_douyin_dl/my_get_douyin_url_phone/Camera/name.mp4 -ss 00:00:00.0 -t 00:00:xx -acodec copy -vcodec copy -async 1 D:/myPython/20200303_douyin_dl/my_get_douyin_url_phone//video_cut/name.mp4'
        # my_cmd = my_cmd.replace('xx', str(my_end_time))
        # my_cmd = my_cmd.replace('name.mp4', str(path_name))
        # print(my_cmd)
        # os.system(my_cmd)

        # 写到txt文本文件

        with open('./Camera/filelist.txt', 'a+') as f:
            f.write('file ' + '\'' + path_name + '\'' + "\n")


def video_cut_py(path_name):
    try:
        video = VideoFileClip('./Camera/' + path_name)
        if video.duration > 4:
            # 剪辑视频，从10秒开始到视频结尾前12秒
            video = video.subclip(0, video.duration - 3.5)
            video.to_videofile('./video_cut/' + path_name, fps=24, remove_temp=True)
        else:
            print('没有时间')
        print('video_cut_py结束')
    except:
        print("video_cut_py出错了---跳过")
        time.sleep(1)


def get_length(filename):
    filename = 'D:\\myPython\\20200303_douyin_dl\\my_get_douyin_url_phone\\Camera\\' + filename
    result = subprocess.Popen(["ffprobe", filename],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)

    for x in result.stdout.readlines():
        if b"Duration" in x:
            # print('duration')
            # print(video_duration)
            # x = re.search(rb"Duration.+?\d{2}:(\d{2}):\d{2}", x)
            # return int(x.group(1))
            video_duration_tmp = str(x[18:23])
            print('video_duration_tmp[2:4]:    ' + str(video_duration_tmp[2:4]))
            return video_duration_tmp[2:4]
    print('return 9999999')
    return 999


def upload_video(my_final_name_file_1, my_final_name_file):
    web_open('https://studio.youtube.com/channel/UCcrvfipWK74xk2aNBq4Aa7Q/videos?d=ud')
    web_open('https://studio.youtube.com/channel/UCcrvfipWK74xk2aNBq4Aa7Q/videos?d=ud')
    time.sleep(20)
    PrtSc("Screencap.png")
    matchImgClick("Screencap.png", "upload.png")

    pyperclip.copy('D:\\myPython\\20200303_douyin_dl\\my_get_douyin_url_phone\\' + my_final_name_file + '.mp4')
    time.sleep(1)
    KEY_KEY(17, 86)
    time.sleep(1)

    PrtSc("Screencap.png")
    matchImgClick("Screencap.png", "open.png")

    time.sleep(10)

    pyperclip.copy(my_final_name_file_1 + my_final_name_file)
    time.sleep(1)
    KEY_KEY(17, 86)
    time.sleep(1)

    PrtSc("Screencap.png")
    matchImgClick("Screencap.png", "goon.png")

    for index in range(0, 3, 1):
        PrtSc("Screencap.png")
        matchImgClick("Screencap.png", "select.png")
        # 点击空白
        click(1200, 700)

    PrtSc("Screencap.png")
    matchImgClick("Screencap.png", "select.png")

    PrtSc("Screencap.png")
    matchImgClick("Screencap.png", "douyin.png")

    # 点击空白
    click(1200, 700)

    # # 下
    # for index in range(0, 10, 1):
    #     KEY(40)
    #     time.sleep(0.4)

    PrtSc("Screencap.png")
    matchImgClick("Screencap.png", "no.png")

    PrtSc("Screencap.png")
    matchImgClick("Screencap.png", "goon.png")

    PrtSc("Screencap.png")
    matchImgClick("Screencap.png", "goon.png")

    PrtSc("Screencap.png")
    matchImgClick("Screencap.png", "publish.png")

    print('结束')


def del_file(path_data):
    # 判断文件是否存在
    # if os.path.exists('./sound/filelist.txt'):
    #     os.remove('./sound/filelist.txt')
    # else:
    #     print("要删除的文件不存在！a+ 去生成")
    for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "\\" + i  # 当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data):  # os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)


# def video_concat(my_final_name):
#     mytime = datetime.datetime.now()
#     print("现在时间（）：" + str(mytime.date()) + str(mytime.hour) + str(mytime.minute))
#     # my_time_date_minute = str(mytime.date()) + str(mytime.hour) + str(mytime.minute)
#     my_cmd_concat = r'ffmpeg -f concat -safe 0 -i ./sound/filelist.txt -c copy ./sound/datetime.mp4'
#     my_cmd_concat = my_cmd_concat.replace('datetime', my_final_name)
#     os.system(my_cmd_concat)


def save_mp3(my_text_path):

    # with open(my_text_path, 'r', encoding='utf-8') as f:
    #     line = f.read()  # 文件不大，一次性读取到list
    #     speak = comtypes.client.CreateObject("SAPI.SpVoice")
    #
    #     filestream = comtypes.client.CreateObject("SAPI.spFileStream")
    #     speak.Rate = 8
    #     filestream.open("./sound/output_person.mp3", 3, False)
    #     speak.AudioOutputStream = filestream
    #     speak.Speak('倒计时' + line)
    #     filestream.close()

        # for index_my in range(0, len(line), 1):
        #     # 文字生成语音
        #     my_line_text = line.replace('\n', '').replace('\r', '').replace(' ', '')
        #     tts = gTTS(text=my_line_text, lang='zh-CN')
        #     tts.save("./sound/input_speed_normal.mp3")
        #
        #     # 声音速度调节
        #     my_cmd_speed = r'ffmpeg -i ./sound/input_speed_normal.mp3 -filter:a "atempo=2.0" -vn ./sound/output.mp3'
        #     # my_cmd_speed = my_cmd_speed.replace('input', speed_normal)
        #     # my_cmd_speed = my_cmd_speed.replace('output', my_path_filename)
        #     print(my_cmd_speed)
        #     os.system(my_cmd_speed)

    # # 两个声音混合
    # my_cmd = r'ffmpeg -i ./sound/output_person.mp3  -i dida.mp3 -filter_complex amix=inputs=2:duration=first:dropout_transition=2 -f mp3 ./sound/output.mp3'
    # print(my_cmd)
    # os.system(my_cmd)

    # 文字生成图片
    # 文字生成图片
    W, H = (720, 1080)
    # msg = my_line_text
    im = Image.new("RGB", (W, H), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    font1 = ImageFont.truetype(os.path.join("fonts", r"D:\myPython\20200308_text2speech\msyhbd.ttc"), 60)
    font = ImageFont.truetype(os.path.join("fonts", r"D:\myPython\20200308_text2speech\msyhbd.ttc"), 40)
    # w, h = draw.textsize(msg.encode('utf-8'))

    draw.rectangle((0, 0, 720, 160), '#303F9F', '#303F9F')

    draw.text((260, 60), '倒计时', font=font1, fill="#FFFFFF")
    with open('test.txt', 'r', encoding='utf-8') as f:
        line = f.readlines()  # 文件不大，一次性读取到list
        for index_my in range(0, len(line), 1):
            # # 外切矩形为正方形时椭圆即为圆
            # draw.ellipse((550, 50, 600, 100), '#757575', '#757575')

            draw.rectangle((0, (80 + 70 * (index_my + 1)), 720, (80 + 70 * (index_my + 1) + 80 + 70 * (index_my + 1))), '#FFFFFF', '#BDBDBD')
            draw.text((200, 90 + 70 * (index_my + 1)), str(' ' + line[index_my].split(' ', 2)[0]), font=font, fill="#212121")
            draw.text((400, 90 + 70 * (index_my + 1)), str(line[index_my].split(' ', 2)[1]), font=font, fill="#E91E63")
            draw.text((480, 90 + 70 * (index_my + 1)), str('天'), font=font, fill="#212121")
    im.save('./sound/image.jpg')

    # # mkv成mp4
    # my_cmd = r'ffmpeg -i dida.wav ./sound/dida.mp3'
    # # my_cmd = my_cmd.replace('image', str(my_path_filename))
    # # my_cmd = my_cmd.replace('music', str(my_path_filename))
    # # my_cmd = my_cmd.replace('output', str(my_path_filename))
    # print(my_cmd)
    # os.system(my_cmd)

    # # 图片和声音合并成视频
    # # my_cmd = r'ffmpeg -loop 1 -framerate 1 -i ./sound/image.jpg -i  ./sound/output_person.mp3 -c:v libx264 -preset veryslow -crf 0 -c:a copy -shortest ./sound/daojishi.mp4'
    # my_cmd = r'ffmpeg -i dida.mp3  -i ./sound/image.jpg -acodec aac -strict -2 -vcodec libx264 -ar 22050 -ab 128k -ac 2 -pix_fmt yuvj420p -y ./sound/daojishi.mp4'
    # # my_cmd = my_cmd.replace('image', str(my_path_filename))
    # # my_cmd = my_cmd.replace('music', str(my_path_filename))
    # # my_cmd = my_cmd.replace('output', str(my_path_filename))
    # print(my_cmd)
    # os.system(my_cmd)

    # # mkv成mp4
    # my_cmd = r'ffmpeg -i dida.mp3 ./sound/daojishi.avi'
    # print(my_cmd)
    # os.system(my_cmd)

    # 图片和声音合并成视频
    # my_cmd = r'ffmpeg -loop 1 -framerate 1 -i ./sound/image.jpg -i  ./sound/output_person.mp3 -c:v libx264 -preset veryslow -crf 0 -c:a copy -shortest ./sound/daojishi.mp4'
    my_cmd = r'ffmpeg -r 15 -f image2 -loop 1 -i ./sound/image.jpg -i dida.mp3 -pix_fmt yuvj420p -t 278 -vcodec libx264 ./sound/daojishi.mp4'
    print(my_cmd)
    os.system(my_cmd)

    # # 写到txt文本文件
    # with open('./sound/filelist.txt', 'a+') as f:
    #     f.write('file ' + '\'' + str('daojishi') + '_' + my_line_text + '.mkv' + '\'' + "\n")




def to_phone_oneplus6():
    print('开始删除手机里的文件')
    # os.popen('adb -s 66819679 shell rm /storage/emulated/0/1/*')
    # time.sleep(2)
    # print('开始传文件到手机')
    # try:
    #     os.popen(r'adb -s 66819679 push ./sound/daojishi.mp4 /storage/emulated/0/1/')
    # except Exception as e:
    #     print(e)
    #     print("这里有个异常")
    # time.sleep(3)
    # # print('重启')
    # # os.popen(r'adb -s 66819679 reboot')
    # # time.sleep(60)
    # #

    print('home  ')
    os.popen('adb -s 66819679 shell input swipe 485 2279 485 1500 100')
    time.sleep(2)

    print('长按 input swipe 100 100 100 100 1000 ')
    os.popen('adb -s 66819679 shell input swipe 485 2279 485 1000 5000')
    time.sleep(10)

    # 清除
    print('清除')
    os.popen('adb -s 66819679 shell input tap 533 1936')
    time.sleep(4)

    print('home  ')
    os.popen('adb -s 66819679 shell input swipe 485 2279 485 1500 100')
    time.sleep(2)

    # 打开文件
    print('打开文件')
    os.popen('adb -s 66819679 shell input tap 142 606')
    time.sleep(4)
    #
    # 点击存储
    print('点击存储')
    os.popen('adb -s 66819679 shell input tap 411 2194')
    time.sleep(40)
    #
    # # 点击1
    # print('点击1')
    # os.popen('adb -s 66819679 shell input tap 485 611')
    # time.sleep(5)
    #
    # print('长按 input swipe 100 100 100 100 1000 ')
    # os.popen('adb -s 66819679 shell input swipe 485 611 485 611 1000')
    # time.sleep(2)
    #
    # print('3dian')
    # os.popen('adb -s 66819679 shell input tap 1020 143')
    # time.sleep(2)
    #
    # print('分享')
    # os.popen('adb -s 66819679 shell input tap 676 754')
    # time.sleep(2)
    #
    # print('选抖音')
    # os.popen('adb -s 66819679 shell input tap 149 1181')
    # time.sleep(30)
    #
    # # print('+')
    # # os.popen('adb -s 66819679 shell input tap 541 1690')
    # # time.sleep(10)
    #
    # # print('点击上传')
    # # os.popen('adb -s 66819679 shell input tap 871 1512')
    # # time.sleep(10)
    #
    # # print('选择视频')
    # # os.popen('adb -s 66819679 shell input tap 149 475')
    # # time.sleep(10)
    #
    # print('下一步')
    # os.popen('adb -s 66819679 shell input tap 898 204')
    # time.sleep(10)
    #
    # print('下一步')
    # os.popen('adb -s 66819679 shell input tap 939 1680')
    # time.sleep(15)
    #
    # print('发布')
    # os.popen('adb -s 66819679 shell input tap 796 1654')
    # time.sleep(10)



# str1是节假日 str2是现在时间
def days(str1, str2):
    date1 = datetime.datetime.strptime(str1[0:10], "%Y-%m-%d")
    date2 = datetime.datetime.strptime(str2[0:10], "%Y-%m-%d")
    if date1 >= date2:
        num = (date1 - date2).days
        return num
    else:
        return -1


def months(str1, str2):
    year1 = datetime.datetime.strptime(str1[0:10], "%Y-%m-%d").year
    year2 = datetime.datetime.strptime(str2[0:10], "%Y-%m-%d").year
    month1 = datetime.datetime.strptime(str1[0:10], "%Y-%m-%d").month
    month2 = datetime.datetime.strptime(str2[0:10], "%Y-%m-%d").month
    num = (year1 - year2) * 12 + (month1 - month2)
    return num


def my_holiday(my_word, my_date):
    mytime = datetime.datetime.now()
    # print("update_text现在时间（）：" + str(str(mytime)[:-7]))
    my_days = days(my_date, str(mytime)[:-7])
    my_text = my_word
    if my_days >= 0:
        return my_text.replace('n', str(my_days))
    else:
        return ''



def update_text():
    '''
    1清明节	4月4日~4月6日	无调休	共3天
    2劳动节	5月1日~5月5日	4月26日(周日)、5月9日(周六)上班	共5天

    3母亲节5月10日
    4护士节5月12日
    5高考  88天
    6端午节	6月25日~6月27日	6月28日(周日)上班	共3天
    7七夕节8月25日
    8教师节9月10日
    9中秋节	10月1日~10月8日	9月27日(周日)、10月10日(周六)上班	共8天
    10国庆节	10月1日~10月8日	9月27日(周日)、10月10日(周六)上班	共8天
    11今年还剩下2020年1月1日
    122021新年2月12日
    '''
    mytime = datetime.datetime.now()
    print("update_text现在时间（）：" + str(str(mytime)[:-7]))
    my_text_list = []
    my_text_list.append(my_holiday('清明 n 天', '2020-04-04 00:00:00'))
    my_text_list.append(my_holiday('劳动节 n 天', '2020-05-01 00:00:00'))
    my_text_list.append(my_holiday('母亲节 n 天', '2020-05-10 00:00:00'))
    my_text_list.append(my_holiday('护士节 n 天', '2020-05-12 00:00:00'))
    my_text_list.append(my_holiday('高考 n 天', '2020-06-07 00:00:00'))
    my_text_list.append(my_holiday('端午 n 天', '2020-06-25 00:00:00'))
    my_text_list.append(my_holiday('七夕 n 天', '2020-08-25 00:00:00'))
    my_text_list.append(my_holiday('教师节 n 天', '2020-09-10 00:00:00'))
    my_text_list.append(my_holiday('中秋节 n 天', '2020-10-01 00:00:00'))
    my_text_list.append(my_holiday('国庆节 n 天', '2020-10-01 00:00:00'))
    my_text_list.append(my_holiday('今年还剩 n 天', '2021-01-01 00:00:00'))

    if os.path.isfile('test.txt'):
        os.remove('test.txt')
    for my_list_index in range(0, len(my_text_list), 1):
        if my_text_list[my_list_index]:
            with open('test.txt', 'a+', encoding='utf-8') as f:
                f.write(my_text_list[my_list_index] + '\n')


def sun():
    print('开始摄影')
    print('打开手机相机')
    os.popen('adb -s 66819679 shell input tap 890 1200')
    time.sleep(10)
    my_time = datetime.datetime.now()
    print("现在时间：" + str(my_time))
    while True:
        if my_time.second % 5 and my_time.hour < 9:
            os.popen('adb -s 66819679 shell input tap 522 1745')

def get_pic():
    
    # 新建空列表，把想要的放进去列表里。
    my_list = []
    for root, dirs, files in os.walk("D:/dxp/douyin/old/flower/"):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            # 去掉后缀
            # print(root)
            # name = f.replace('.xls','')
            # print(name)
            # 把每张表的名字追加
            my_list.append(root + f)
    return my_list[random.randint(0,len(my_list)-1)]




def to_phone():
    print('开始删除手机里的文件')
    os.popen('adb -s 66819679 shell rm /storage/emulated/0/1/*')
    time.sleep(2)
    for my_i in range(1, 4, 1):
        print('开始传文件到手机')
        my_pic_file = get_pic()
        time.sleep(1)
        my_adb_push = r'adb -s 66819679 push  ' + my_pic_file + ' /storage/emulated/0/1/'
        print(my_adb_push)
        os.popen(my_adb_push)
        print("结束传送")
        time.sleep(5)

    time.sleep(10)
    print('重启')
    os.popen(r'adb -s 66819679 reboot')
    time.sleep(100)

    # # 打开文件
    # print('打开文件')
    # os.popen('adb -s 66819679 shell input tap 520 1200')
    # time.sleep(5)

    # # 点击存储
    # print('点击存储')
    # os.popen('adb -s 66819679 shell input tap 822 300')
    # time.sleep(40)

    # # 点击1
    # print('点击1')
    # os.popen('adb -s 66819679 shell input tap 485 611')
    # time.sleep(5)

    # print('长按 input swipe 100 100 100 100 1000 ')
    # os.popen('adb -s 66819679 shell input swipe 485 611 485 611 1000')
    # time.sleep(2)

    # print('3dian')
    # os.popen('adb -s 66819679 shell input tap 1020 143')
    # time.sleep(2)

    # print('分享')
    # os.popen('adb -s 66819679 shell input tap 676 754')
    # time.sleep(2)

    print('选抖音')
    os.popen('adb -s 66819679 shell input tap 144 1302')
    time.sleep(30)

    print('+')
    os.popen('adb -s 66819679 shell input tap 534 1690')
    time.sleep(20)

    print('点击上传')
    os.popen('adb -s 66819679 shell input tap 871 1512')
    time.sleep(20)

    print('选择图片选项卡')
    os.popen('adb -s 66819679 shell input tap 907 298')
    time.sleep(20)

    print('选择图片1')
    os.popen('adb -s 66819679 shell input tap 216 422')
    time.sleep(8)
    print('选择图片2')
    os.popen('adb -s 66819679 shell input tap 502 422')
    time.sleep(8)

    print('下一步')
    os.popen('adb -s 66819679 shell input tap 949 1684')
    time.sleep(20)

    print('下一步')
    os.popen('adb -s 66819679 shell input tap 949 1684')
    time.sleep(20)

    print('发布')
    os.popen('adb -s 66819679 shell input tap 781 1654')
    time.sleep(20)


def comment():
    print('---打开评论')
    os.popen('adb -s 66819679 shell input tap 992 1575')
    time.sleep(4)

    print('---点击空白框')
    os.popen('adb -s 66819679 shell input tap 108 2217')
    time.sleep(4)

    os.popen('adb -s 66819679 shell input tap 632 1930')
    time.sleep(0.3)
    os.popen('adb -s 66819679 shell input tap 700 1637')
    time.sleep(0.3)
    os.popen('adb -s 66819679 shell input tap 415 1940')
    time.sleep(0.5)
    os.popen('adb -s 66819679 shell input tap 700 1637')
    time.sleep(0.3)
    os.popen('adb -s 66819679 shell input tap 916 1636')
    time.sleep(0.5)
    os.popen('adb -s 66819679 shell input tap 592 2097')
    time.sleep(0.9)

    print('---点击icon')
    for my_c in range(1,random.randint(5,15), 1):

        os.popen('adb -s 66819679 shell input tap 60 1389')
        time.sleep(0.3)

    for my_c in range(1,random.randint(5,15), 1):
        os.popen('adb -s 66819679 shell input tap 200 1389')
        time.sleep(0.3)
    
    print('---点发送评论')
    os.popen('adb -s 66819679 shell input tap 1000 1146')
    time.sleep(3)

    print('---返回视频')
    os.popen('adb -s 66819679 shell input keyevent 4')
    time.sleep(2)





def add_love_comment():
# 粉丝加关注
    for my_index in range(1, 5000, 1):
        print("ooooo----------------" + str(my_index) + '    ' + str(datetime.datetime.now()))
        try:
            screencap()
            if matchImg('phoneScreencap.png', 'home.png') is not None:
                print('home')
                break
            if matchImg('phoneScreencap.png', 'add.png') is not None:
                print("add" + str(
                    matchImg('phoneScreencap.png', 'add.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'add.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'add.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'add.png')['result'][1])
                myy_off = str(matchImg('phoneScreencap.png', 'add.png')['result'][1] + 62 )
                print('点击手机')
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(2)

                print('打开用户')
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy_off, 'r', 1)
                time.sleep(random.randint(5,6))

            elif matchImg('phoneScreencap.png', 'add1.png') is not None:
                print("add1" + str(
                    matchImg('phoneScreencap.png', 'add1.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'add1.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'add1.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'add1.png')['result'][1])
                myy_off = str(matchImg('phoneScreencap.png', 'add1.png')['result'][1] + 62 )
                print('点击手机')
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(2)

                print('打开用户')
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy_off, 'r', 1)
                time.sleep(random.randint(4,5))

            screencap()
            if matchImg('phoneScreencap.png', 'videoisempty.png') is not None or matchImg('phoneScreencap.png', 'pri.png') is not None or matchImg('phoneScreencap.png', 'music.png') is not None:
                print("没有作品")
                print('---返回用户列表')
                os.popen('adb -s 66819679 shell input keyevent 4')
                time.sleep(2)
            else:
                if matchImg('phoneScreencap.png', 'video.png') is not None:
                    print("点击她的作品：" + str(
                        matchImg('phoneScreencap.png', 'video.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'video.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'video.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'video.png')['result'][1])
                    myy_off = str(matchImg('phoneScreencap.png', 'video.png')['result'][1] + 72 )
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy_off, 'r', 1)
                    time.sleep(4)

                print('点赞')
                os.popen('adb -s 66819679 shell input tap 988 1381')
                time.sleep(random.randint(1,2))

                # 随机评论
                # if random.choice([True, False]):
                comment()

                print('---返回用户列表')
                os.popen('adb -s 66819679 shell input keyevent 4')
                time.sleep(3)
                screencap()
                if matchImg('phoneScreencap.png', 'add.png') is not None or matchImg('phoneScreencap.png', 'add1.png') is not None:
                    print("add" + str(
                        matchImg('phoneScreencap.png', 'add.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'add.png')['result'][1]))
                else:
                    os.popen('adb -s 66819679 shell input keyevent 4')
                    time.sleep(2)

            # 滑动屏幕
            os.popen('adb -s 66819679 shell input swipe 520 1000 520 700 ')
            time.sleep(random.randint(2,3))


        except Exception as e:
            print(e)
            time.sleep(9)


def love():
    # 粉丝加关注
    for my_index in range(1, 150, 1):
        print("ooooo----------------" + str(my_index) + '    ' + str(datetime.datetime.now()))
        try:
            print("滑动屏幕")
            os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
            time.sleep(random.randint(2,3))
            screencap()
            if matchImg('phoneScreencap.png', 'live.png') is not None:
                print("直播")
                # os.popen('adb -s 66819679 shell input keyevent 4')
                # time.sleep(4)
                print("滑动屏幕")
                os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
                time.sleep(random.randint(2,3))
                print("再一次滑动屏幕")
                os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
                time.sleep(random.randint(2,3)) 
            elif matchImg('phoneScreencap.png', 'gift.png') is not None:
                print("直播中,关闭")
                os.popen('adb -s 66819679 shell input keyevent 4')
                time.sleep(4)
                print("滑动屏幕")
                os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
                time.sleep(random.randint(2,3))
                print("再一次滑动屏幕")
                os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
                time.sleep(random.randint(2,3)) 
            else:
                # 点赞
                os.popen('adb -s 66819679 shell input tap 988 1381')
                time.sleep(random.randint(1,2))

        except Exception as e:
            print(e)
            time.sleep(9)


# 图片添加字
def add_num(im01, mypng, x, y):
    img = Image.open(im01)
    imgmypng = Image.open(mypng)
    # ImageDraw.Draw()函数会创建一个用来对image进行操作的对象，
    # 对所有即将使用ImageDraw中操作的图片都要先进行这个对象的创建。
    draw = ImageDraw.Draw(img)

    # 设置字体和字号‪C:\Windows\Fonts\msyhbd.ttc
    myfont = ImageFont.truetype('C:/windows/fonts/msyhbd.ttc', size=80)

    # 设置要添加的数字的颜色为红色
    fillcolor = "#2F83C7"

    # 昨天博客中提到过的获取图片的属性
    width, height = imgmypng.size

    # 设置添加数字的位置，具体参数可以自己设置，从左上角开始
    draw.text((x - width / 2, y - height / 2), '99999999', font=myfont, fill=fillcolor)

    # 将修改后的图片以格式存储
    img.save(im01, 'png')

    return 0


# 涂鸦掉图片
def matchImg_delete2Continue(myScreencap, mypng):
    if matchImg(myScreencap, mypng) is not None:
        print("-------------涂鸦pic！" + mypng + str(
            matchImg(myScreencap, mypng)['result'][0]) + ',' + str(
            matchImg(myScreencap, mypng)['result'][1]))
        myx = str(matchImg(myScreencap, mypng)['result'][0])
        myy = str(matchImg(myScreencap, mypng)['result'][1])
        add_num(myScreencap, mypng, int(float(myx)), int(float(myy)))
        os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
        print("-------------结束点击按钮。")
        return True
    else:
        return False


def add_quickly():
 # 粉丝加关注
    for my_index in range(1, 30, 1):
        print("ooooo--------ooooooo-----" + str(my_index) + '    ' + str(datetime.datetime.now()))
        try:

            screencap()
            while matchImg_delete2Continue('phoneScreencap.png', 'add.png'):
                print('while')
                time.sleep(1)
            print('end while')
            print("滑动屏幕")
            os.popen('adb -s 66819679 shell input swipe 520 1100 520 300 ')
            time.sleep(random.randint(2,3))
        except Exception as e:
            print(e)
            time.sleep(9)


def back_control():
    for my_count_back in range(1, 10, 1):
        os.popen('adb -s 66819679 shell input keyevent 4')
        time.sleep(1)
    print("d打开抖音")
    os.popen('adb -s 66819679 shell input tap 553 1650')
    time.sleep(3)
    print("向右滑动屏幕")
    os.popen('adb -s 66819679 shell input swipe 84 1300 900 1300 ')
    time.sleep(3)
    print("向上滑动屏幕1")
    os.popen('adb -s 66819679 shell input swipe 520 1100 520 300 ')
    time.sleep(2)
    print("向上滑动屏幕2")
    os.popen('adb -s 66819679 shell input swipe 520 1100 520 300 ')
    time.sleep(2)

def python_peple_add():
    for my_loop_i in range(1, 200, 1):
        print("滑动屏幕------------" + str(my_loop_i))
        os.popen('adb -s 66819679 shell input swipe 520 1700 520 1550 ')
        time.sleep(random.randint(2,3))
        screencap()
        matchImg_up_down('phoneScreencap.png', 'love.png', 140)
        # if matchImg('phoneScreencap.png', 'love.png') is not None:
        #     print("点击她的作品：" + str(
        #         matchImg('phoneScreencap.png', 'love.png')['result'][0]) + ',' + str(
        #         matchImg('phoneScreencap.png', 'love.png')['result'][1]))
        #     myx = str(matchImg('phoneScreencap.png', 'love.png')['result'][0])
        #     myy = str(matchImg('phoneScreencap.png', 'love.png')['result'][1])
        #     myx_off = str(matchImg('phoneScreencap.png', 'love.png')['result'][0] - 935 )
        #     os.popen('adb -s 66819679 shell input tap ' + myx_off + ' ' + myy, 'r', 1)
        #     time.sleep(4)
        #     # 如果有关注的按钮就点击
        screencap()
        if matchImg('phoneScreencap.png', 'add2.png') is not None:
            print("add2" + str(
                matchImg('phoneScreencap.png', 'add2.png')['result'][0]) + ',' + str(
                matchImg('phoneScreencap.png', 'add2.png')['result'][1]))
            myx = str(matchImg('phoneScreencap.png', 'add2.png')['result'][0])
            myy = str(matchImg('phoneScreencap.png', 'add2.png')['result'][1])
            os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
            time.sleep(1)
            # back 返回
            print('back 返回')
            os.popen('adb -s 66819679 shell input keyevent 4')
            time.sleep(3)
        elif matchImg('phoneScreencap.png', 'id.png') is not None:
            print("id")
            # back 返回
            print('back 返回')
            os.popen('adb -s 66819679 shell input keyevent 4')
            time.sleep(3) 


if __name__ == '__main__':
    # 定义鼠标键盘实例
    k = PyKeyboard()
    m = PyMouse()

    # add_love_comment()
    
    # add_quickly()
    # back_control()
    # love()
    
    python_peple_add()