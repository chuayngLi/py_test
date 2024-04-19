import subprocess


def get_wifi_password():
    # 调用系统命令，获取WiFi密码
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile'])
    result = result.decode('gbk')  # 将命令输出转换为字符串

    # 提取WiFi名称
    profiles = [i.split(':')[1][1:-1] for i in result.split('\n') if '所有用户配置文件' in i]

    # 获取各个WiFi网络的密码
    passwords = []
    for profile in profiles:
        password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', 'name=' + profile, 'key=clear'])
        password = password.decode('gbk')  # 转换为字符串
        password = [i.split(':')[1][1:-1] for i in password.split('\n') if '关键内容' in i]
        passwords.append((profile, password[0]))

    return passwords


# 调用函数获取WiFi密码
wifi_passwords = get_wifi_password()

# 打印WiFi名称和密码
for wifi in wifi_passwords:
    print(f'WiFi名称：{wifi[0]}，密码：{wifi[1]}')
