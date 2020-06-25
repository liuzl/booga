# encoding=utf-8
import sys
import os.path
import json

module_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(module_dir+'/lib/')
from tencent_ai_texsmart import *

from fastapi import FastAPI

engine = NluEngine(module_dir + '/data/nlu/kb/', 1)
app = FastAPI()

@app.get('/')
def index():
    return {'message': 'TexSmart服务'}

@app.get('/parse')
def parse(text: str):
    output = engine.parse_text(text)
    res = {
        "words": [{"str":x.str, "hit":[x.offset,x.len], "tag":x.tag} for x in output.words()],
        "phrases": [{"str":x.str, "hit":[x.offset,x.len], "tag":x.tag} for x in output.phrases()],
        "entities": [{"str":x.str, "hit":[x.offset,x.len],
            "type":{"name":x.type.name,"i18n":x.type.i18n,"flag":x.type.flag,"path":x.type.path},
            "meaning":None if x.meaning == "" else json.loads(x.meaning)} for x in output.entities()]
    }
    return res

if __name__ == "__main__":
    import uvicorn
    print("server star")
    uvicorn.run('texsmart_server:app',host='0.0.0.0', port=9080, debug=True, access_log=True)
