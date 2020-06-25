# TexSmart解析服务

## 准备

### 下载SDK

```sh
wget https://ai.tencent.com/ailab/nlp/texsmart/download/texsmart-sdk-0.1.1-s.zip
unzip texsmart-sdk-0.1.1-s.zip
mv texsmart-sdk-0.1.1-s/lib ./
mv texsmart-sdk-0.1.1-s/data ./
```

### 安装依赖

*需要提前安装好Anaconda3*

```sh
pip install fastapi
pip install uvicorn
```

## 启动服务
```sh
# uvicorn texsmart_server:app --reload --host 0.0.0.0 --port 9080
./run.sh
```
