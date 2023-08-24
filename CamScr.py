from requests.auth import HTTPDigestAuth
import requests
import xml.etree.ElementTree as ET
import time

raw_data="""<User version="2.0" xmlns="http://www.isapi.org/ver20/XMLSchema">
 <id>1</id>
 <enabled>true</enabled>
 <userName>admin</userName>
 <password>New_Pass</password>
 <keypadPassword>Cam12345678</keypadPassword>
 <loginPassword>Old_Pass</loginPassword>
 <userOperateType>1</userOperateType>
 <bondIpAddressList>
 <bondIpAddress>
 <id>2</id>
 <ipAddress></ipAddress>
 <ipv6Address></ipv6Address>
 </bondIpAddress>
 </bondIpAddressList>
 <bondMacAddressList>
 <bondMacAddress>
 <id>2</id>
 <macAddress></macAddress>
 </bondMacAddress>
 </bondMacAddressList>
 <userLevel>Operator</userLevel>
 <attribute>
 <inherent>0</inherent>
 </attribute>
</User>"""

Cameras = open('cameras.txt','r')
for ip in Cameras:
    try:
        if ip[len(ip)-1] == '\n':
            ip=ip[0:len(ip)-1]
        if ip == "":
            break
        print('changing password on camera: ',ip)
        url = 'http://'+ip+'/ISAPI/Security/users'
        response=requests.put(url, auth=HTTPDigestAuth('admin', '12345678p'),data=raw_data)
        tree = ET.ElementTree(ET.fromstring(response.content))
        root = tree.getroot()
        print(root[3].text)
        print("=============================")
        time.sleep(1)
    except Exception as ex:
        print("*****************************************")
        print("error:",str(ex))
        print("*****************************************")



