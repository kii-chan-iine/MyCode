#coding=utf-8
import time
import sys
import json
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
from dateutil import tz
import win32api, win32con, win32gui
import os

#这是图片的接口
conf = {
'last_refresh_url': 'http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json',
'img_url_pattern': 'http://himawari8-dl.nict.go.jp/himawari8/img/D531106/%id/550/%s_%i_%i.png',
'scale': 1,
}

def get_last_time():
    r = requests.get(conf['last_refresh_url'])
    # print('r.text',r.text)
    resp = json.loads(r.text)
    # resp = r.text
    # print('resp type',type(resp),resp)
    last_refresh_time = datetime.strptime(resp['date'], '%Y-%m-%d %H:%M:%S')
    return last_refresh_time

# 转换时间
def utf2local(utc):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = utc.replace(tzinfo=from_zone)
    return utc.astimezone(to_zone)

def download(args):
    scale = args['scale']
    fpath = ''
    png = Image.new('RGB', (550 * scale, 550 * scale))
    #还记得我前面说下载图片是一块一块嘛，把大图片分成行列分别下载
    for row in range(scale):
        for col in range(scale):
            strtime = args['time'].strftime("%Y/%m/%d/%H%M%S")
            url = conf['img_url_pattern'] % (args['scale'], strtime, row, col)
            print('url',url)
            r = requests.get(url)
            tile = Image.open(BytesIO(r.content))
            png.paste(tile, (550 * row, 550 * col, 550 * (row + 1), 550 * (col + 1)))
            if 'fout' in args:
                fpath = args['fout']
            else:
                fpath = "%s.bmp" % utf2local(args['time']).strftime("%Y/-%m/-%d/ %H.%M.%S").replace('/', '')
            png.save(fpath, "BMP")
            print('下载完成, 保存图片为 %s' % fpath)
    print('fpath',fpath)
    setWallPaper(fpath)

#我默认scale=4了，这样的图片是2200*2200分辨率，现在大家的电脑普遍都1920*1080了吧
def get_last_image(fout=None, scale=4):
    last_refresh_time = get_last_time()
    args = {'time': last_refresh_time}
    args['scale'] = scale
    if fout is not None:
        args['fout'] = fout
    download(args)
    pass

#setWallpaperFromBMP 和 setWallPaper用于修改电脑壁纸
def setWallpaperFromBMP(imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "6") #2拉伸,0居中,6适应
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)

def setWallPaper(imagePath):
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    print(current_file_path)
    bmpImage = Image.open(imagePath)
    newPath = current_file_path + '\\nowimage.bmp'
    bmpImage.save(newPath, "BMP")
    setWallpaperFromBMP(newPath)

def run(inc):
    while True:
        print('下载中......' )
        if len(sys.argv) == 1:
            get_last_image()
        elif len(sys.argv) == 2:
            get_last_image(fout=sys.argv[1])
        elif len(sys.argv) == 3:
            get_last_image(fout=sys.argv[1], scale=int(sys.argv[2]))
        print('over')
        time.sleep(inc)

if __name__ == '__main__':
	#你可以传入参数
	#第一个参数是图片的保存位置
	#第二个参数影响图片分辨率，1->550*550 2->1100*1100 4->2200*2200
    run(600)#10分钟执行一次
