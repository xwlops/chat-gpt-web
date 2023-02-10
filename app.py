import openai
from flask import Flask, request, render_template
from datetime import datetime, timedelta
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# 创建 Flask 应用实例
app = Flask(__name__)
# 使用 Flask-Limiter 对请求进行限制
limiter = Limiter(app, key_func=get_remote_address)
# 设置 OpenAI API Key
openai.api_key = 'xxxxx'

# 白名单列表，里面的 IP 不受请求限制
whitelist = ['192.168.1.1', '192.168.1.2']

# 定义视图函数，对根路径进行请求响应
@app.route('/', methods=['GET', 'POST'])
def index():
    # 获取客户端 IP 地址
    client_ip = request.remote_addr
    # 获取请求中的问题
    question = request.form.get('question')

    # 判断客户端 IP 是否在白名单中
    if client_ip in whitelist:
        res = get_completion(question)
    else:
        res = get_completion(question, client_ip)
    # 返回渲染后的模板页面
    return render_template('index.html', question=question, res=res)

# 使用 Flask-Limiter 对 get_completion() 函数请求进行限制
@limiter.limit("1000/hour")
def get_completion(question, client_ip=None):
    try:
        # 使用 OpenAI API 获取补全结果
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{question}\n",
            temperature=0.9,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=None
        )
    except Exception as e:
        return str(e)

    if client_ip and not is_request_limit_exceeded(client_ip):
        return "免费次数已使用完毕，请明天再试"
    return response["choices"][0].text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
