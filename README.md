# 基于OpenAI API的问答系统
## 简介
本项目使用Flask框架，基于OpenAI API开发的问答系统。它允许用户输入问题，并使用OpenAI API生成答案。

## 安装
- 安装Flask：
```
pip install flask
```
- 安装OpenAI API的Python客户端：
```
pip install openai
```
## 使用
- 在代码中配置OpenAI API的密钥：
```
openai.api_key = 'xxxxx'
```
- 启动Flask服务器：
```
touch nohup.out
nohup python3 app.py 
```
- 在浏览器中访问 [http://localhost:80](http://localhost:80)，输入问题并生成答案。
## 功能说明
使用OpenAI API的Completion.create方法，传入问题和参数，生成答案。
使用Flask框架，接收前端发送的问题，并返回生成的答案。
## 版本信息
- 当前版本：v1.0.0
- 日期：2023年2月10日
