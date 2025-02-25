import requests

cookies = {
    'JSESSIONID': '54BE9C4C0205F8A4268AC6',
}

headers = {
    'Host': 'xcx.xybsyw.com',
    'n': 'content,deviceName,keyWord,blogBody,blogTitle,getType,responsibilities,street,text,reason,searchvalue,key,answers,leaveReason,personRemark,selfAppraisal,imgUrl,wxname,deviceId,avatarTempPath,file,file,model,brand,system,deviceId,platform,code,openId,unionid,clockDeviceToken,clockDevice,address',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c2d)XWEB/11581',
    'encryptvalue': '2ff76af1bd43029c8283a4f7335984ee51472137a5eeebd9de35e5e316a226723b1e953595a6a0ed42e9e3fbb4a3f02519ac26075b786cb7834403dd64c1c77d11dde0150ffce43a7c9cbb35c88fa190d2937543cd98bcbaad7e663188d9d69839ce7a811d03a6c899eb8525d1b4474ed883a0173b99cd26783c413002b169c8c8f674842edb066a2ade76bc9d4625352cdb9d397188787d42e2fba98dc59594',
    'm': 'ecd46c5b147f605ac',
    'v': '1.6.36',
    'content-type': 'application/x-www-form-urlencoded',
    'xweb_xhr': '1',
    't': '1740491742',
    's': '6_25_18_1042_0_48_50_32',
    'wechat': '1',
    'accept': '*/*',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://servicewechat.com/wx9f1c2e0bbc10673c/476/page-frame.html',
    'accept-language': 'zh-CN,zh;q=0.9',
}

# 113.949837,22.580005
data = {
    'model': 'microsoft',
    'brand': 'microsoft',
    'platform': 'windows',
    'system': 'Windows 10 x64',
    'openId': 'ooru94gEL0VEKcU',
    'unionId': 'oHY-uwafp1o7Y3Gq',
    'traineeId': '872',
    'adcode': '440',
    'lat': '22.5',
    'lng': '113.9',
    'address': '李华广场',
    'deviceName': 'microsoft',
    'punchInStatus': '1',
    'clockStatus': '1',
}

response = requests.post(
    'https://xcx.xybsyw.com/student/clock/Post!updateClock.action',
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.json())

# def entry():
#     """程序入口"""
#     pass
#
# if __name__ == '__main__':
#     entry()