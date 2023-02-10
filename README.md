# chat-gpt-web

这是一个 Flask Web 应用，用于处理文本补全请求。它使用 OpenAI API 来实现文本补全功能。

## 前置调钱
- 拥有 OpenAI API 账户
- 创建 [API keys](https://platform.openai.com/account/api-keys)
- 一台拥有公网能力的服务器
## 安装部署

### 克隆项目
```
git clone https://github.com/zops/chat-gpt-web.git
```
### 修改配置
在 `app.py` 中修改 `openai.api_key` 的值,修改为你创建的 `API keys`
```
openai.api_key = 'xxxxx'
```
### 安装依赖
安装python 以及对应的依赖,提示少什么装什么.
### 启动项目
```
cd chat-gpt-web && python app.py 
``` 
### 测试访问
http://{你的IP地址}:{80端口}