# -*-coding:utf-8-*-
import pywifi, time
from pywifi import const


def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # acquire the first Wlan card,maybe not
    iface.scan()  # 扫描wifi
    time.sleep(1)  # 休息一下
    basewifi = iface.scan_results()

    for i in basewifi:
        print("wifi scan result:{}".format(i.ssid))
        print("wifi device MAC address:{}".format(i.bssid))

        # 尝试连接wifi
        profile = pywifi.Profile()  # 配置文件
        profile.ssid = i.ssid  # wifi名称
        profile.auth = const.AUTH_ALG_OPEN  # 需要密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        gen_key()

        iface.remove_all_network_profiles()  # 删除其它配置文件
        tmp_profile = iface.add_network_profile(profile)  # 加载配置文件
        iface.connect(tmp_profile)
        time.sleep(5)
        if iface.status() == const.IFACE_CONNECTED:
            print("connect successfully!")
        else:
            print("connect failed!")
        time.sleep(1)
    return basewifi


def gen_key():
    # 生成wifi破解密码，通用做法是读取密码字典库
    pass


if __name__ == '__main__':
    scan_wifi()