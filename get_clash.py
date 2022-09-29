import os
import time
import shutil
import requests
import json
from shutil import copyfile
from utils.yamlUtils import YamlUtils
from utils.jiang import get_content as jiang_content
from utils.cfmem import get_content as cfmem_content
from utils.pawdroid import get_content as pawdroid_content
from utils.mattkaydiary import get_content as mattkaydiary_content

pathToYamllist = json.loads(requests.get(
    'https://api.github.com/repos/changfengoss/pub/git/trees/main?recursive=1').text)["tree"]
pathToYamllist = pathToYamllist[-1]["path"]
date = pathToYaml.split('/')[1]
yamls = list(filter(lambda x: x["path"].__contains__(date) and x["path"].endswith(".yaml"), iterable))

for (index, item) in enumerate(yamls):
    data = requests.get("https://raw.githubusercontent.com/changfengoss/pub/main/%s" % item["path"]).text
    
    with open("pub/changfengoss%d.yaml" % index, 'w') as output:
        output.write(data)
        

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
