import os
import time
import shutil
import requests
import base64
from requests.adapters import HTTPAdapter
import json
import re
from shutil import copyfile
from utils.yamlUtils import YamlUtils
from utils.jiang import get_content as jiang_content
from utils.cfmem import get_content as cfmem_content
from utils.pawdroid import get_content as pawdroid_content
from utils.mattkaydiary import get_content as mattkaydiary_content


try:
    response = requests.get("https://vpn.fail/free-proxy/type/v2ray").text

    ips = re.findall("				<a href=\"https://vpn\.fail/free-proxy/ip/(.*?)\" style=", response)

    links = []
    for ip in ips:
        try:
            response = requests.get(f"https://vpn.fail/free-proxy/ip/{ip}").text
            link = response.split('class="form-control text-center" id="pp2" value="')[1].split('"')[0]
            links.append(link)
        except:
            pass
    
    base64_content = base64.b64encode(
            "\n".join(links).encode('utf-8')).decode('ascii')
    with open("pub/vpn.fail", 'w') as output:
        output.write(base64_content)
except:
    pass

try:
    pathToYamllist = json.loads(requests.get(
        'https://api.github.com/repos/changfengoss/pub/git/trees/main?recursive=1').text)["tree"]
    last_file = pathToYamllist[-1]["path"]
    date = last_file.split('/')[1]
    yamls = list(filter(lambda x: x["path"].__contains__(date) and x["path"].endswith(".yaml"), pathToYamllist))

    for (index, item) in enumerate(yamls):
        data = requests.get("https://raw.githubusercontent.com/changfengoss/pub/main/%s" % item["path"]).text

        with open("pub/changfengoss%d.yaml" % index, 'w') as output:
            output.write(data)
except:
    pass

    
try:
    source2 = requests.get('http://wxshi.top:9090/clash/proxies').text
    with open("pub/wxshi.yaml", 'w') as output:
        output.write(source2)
except:
    pass
    
try:
    source3 = requests.get('https://raw.githubusercontent.com/misersun/config003/main/config_all.yaml').text
    with open("pub/misersun-config003.yaml", 'w') as output:
        output.write(source3)
except:
    pass
        
    
try:
    source4 = requests.get('https://raw.githubusercontent.com/rezasalimi01/Matsuri/main/Servers.yml').text
    parts = source4.split('\n')
    real_parts = list(filter(lambda x: x.__contains__('://') and x.__len__() > 50, parts))
    
    base64_content = base64.b64encode(
            "\n".join(real_parts).encode('utf-8')).decode('ascii')
    with open("pub/Matsuri", 'w') as output:
        output.write(base64_content)
except:
    pass

try:
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=2))
    s.mount('https://', HTTPAdapter(max_retries=2))
    s.get('https://free.dswang.ga/clash/proxies', timeout=10)
    source5 = s.get('https://free.dswang.ga/clash/proxies', timeout=10).text
    with open("pub/dswang.yaml", 'w') as output:
        output.write(source5)
except:
    pass

bhqz = os.path.join("bhqz")
yamlUtils = YamlUtils(bhqz)
yamlUtils.clone_repo("https://github.com/bhqz/bhqz.git")
yamlUtils.make_template_dict()
yamlUtils.save_file("pub/bhqz.yaml")
shutil.rmtree(bhqz)

freenode = os.path.join("freenode")
yamlUtils = YamlUtils(freenode)
yamlUtils.clone_repo("https://github.com/adiwzx/freenode.git", "main")
yamlUtils.make_template_dict("adidesign.c")
yamlUtils.save_file("pub/freenode.yaml")
shutil.rmtree(freenode)

ssr = os.path.join("ssr")
yamlUtils = YamlUtils(ssr)
yamlUtils.clone_repo("https://github.com/ssrsub/ssr.git", "master")
yamlUtils.make_template_dict("yml")
yamlUtils.save_file("pub/ssr.yaml")
shutil.rmtree(ssr)

jiang_content()
cfmem_content()
pawdroid_content()
mattkaydiary_content()


pub = os.path.join("pub")
yamlUtils = YamlUtils(pub)
yamlUtils.make_template(
    ["jiang.yaml", "mattkaydiary.yaml", "freenode.yaml", "bhqz.yaml", "ssr.yaml", "cfmem.yaml"]
)
yamlUtils.save_file("pub/combine.yaml")
