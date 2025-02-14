# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：  
# 1. 不得用于任何商业用途。  
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。  
# 3. 不得进行大规模爬取或对平台造成运营干扰。  
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。   
# 5. 不得用于任何非法或不当的用途。
#   
# 详细许可条款请参阅项目根目录下的LICENSE文件。  
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。  

# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : core.py
# Time       ：2025.2.14 23:22
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import requests
import re
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from ui_example.ui_widgets.weather.Weather import Ui_Form

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

my_key = '*******'


class View(QMainWindow):

    #### properties for widget value ####
    @property
    def test(self):
        return object
    @test.setter
    def test(self, value):
        return object

    def __init__(self, model, ctrl):
        self.ctrl = ctrl
        super(View, self).__init__()
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #### set Qt model for compatible widget types ####
        # self.ui_example.comboBox_test.setModel(self.model.test_model)

        ### connect widget signals to event functions ####
        self.ui.img.setAlignment(Qt.AlignCenter)
        self.ui.loc_scan.clicked.connect(lambda:self.set_myindex(
            index=self.ui.position.text(),
        ))
        self.ui.loc_scan.clicked.connect(lambda: self.get_lon_lat(
            location_name=self.ui.position.text(),
        ))
        self.ui.loc_scan.clicked.connect(lambda: self.get_weather(
            lng=self.ui.longitude.text(),
            lat=self.ui.latitude.text(),
            state=1,
        ))
        self.ui.temp_radioButton.toggled.connect(lambda: self.get_weather(
            lng=self.ui.longitude.text(),
            lat=self.ui.latitude.text(),
            state=2,
        ))
        self.ui.radioButton.toggled.connect(lambda: self.get_weather(
            lng=self.ui.longitude.text(),
            lat=self.ui.latitude.text(),
            state=3,
        ))
        self.ctrl.myindex_updated.connect(self.update_myindex)

    #### widget signal event functions ####
    def set_myindex(self,index):
        self.ctrl.set_myindex(index)

    def update_myindex(self):
        myindex = self.ctrl.get_myindex()
        print("myindex:",myindex)




    # 根据地点名称获取其经纬度以及简单的描述信息
    def get_lon_lat(self, location_name):
        location_api = 'https://map.baidu.com/geocoding/v3/?address={}&output=json&ak={}&callback=showLocation'.format(
            location_name, my_key)
        try:
            res = requests.get(location_api)
            res = res.text
        except Exception as e:
            print(e)
        res = eval(re.findall('{.*}', res)[0])
        if res:
            self.ui.longitude.setText(str(round(res['result']['location']['lng'], 6)))
            self.ui.latitude.setText(str(round(res['result']['location']['lat'], 6)))
            self.ui.information.setText(str(res['result']['level']))

    # 根据经纬度获取天气信息
    def get_weather(self, lng, lat, state):
        weather_api = 'https://res.abeim.cn/api-weather?lng={}&lat={}'.format(lng, lat)
        try:
            res = requests.get(weather_api)
            res = res.json()
        except Exception as e:
            print(e)
        if state==1:
            self.ui.temp_location.setText(res['地址'])
            self.ui.time_stamp.setText(res['更新时间'])
            self.ui.temp_now.setText(res['现在']['温度'])
            self.ui.humidity_now.setText(res['现在']['湿度'])
            self.ui.pressure.setText(res['现在']['气压'])
        elif state==2:
            temp = [i['温度'] for i in res['小时预报']['温度']]
            plt.figure()
            plt.plot(list(range(1, len(temp)+1)), temp)
            plt.xlabel('距离现在多少个小时')
            plt.ylabel('温度')
            plt.grid()
            plt.savefig('img/1.jpg')
            self.img.setPixmap(QPixmap('img/1.jpg'))
        elif state==3:
            temp = [float(i['风速']) for i in res['小时预报']['风']]
            plt.figure()
            plt.plot(list(range(1, len(temp)+1)), temp)
            plt.xlabel('距离现在多少个小时')
            plt.ylabel('风速')
            plt.grid()
            plt.savefig('img/2.jpg')
            self.img.setPixmap(QPixmap('img/2.jpg'))