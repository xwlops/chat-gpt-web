import openai
from flask import Flask, request, render_template, redirect

# 创建 Flask 实例
server = Flask(__name__)

# 设置 OpenAI API Key
openai.api_key = 'xxxxx'

# 存储每个IP地址请求的次数
ip_request_counts = {}

# 定义 get_completion 函数，用于调用 OpenAI API 获取完成文本
def get_completion(question):
    try:
        # 调用 OpenAI API 完成文本
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
        # 如果调用 API 失败，打印异常信息并返回
        print(e)
        return e
    # 返回 API 调用的结果
    return response["choices"][0].text

# 定义路由，处理 HTTP 请求
@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        # 如果请求中没有问题，返回问题不能为空的提示
        if len(request.form['question']) < 1:
            return render_template(
                'index.html', question="null", res="问题不能为空")
        # 获取请求中的问题
        question = request.form['question']
        print("======================================")
        print("接到请求:", question)
        # 获取请求的 IP 地址
        client_ip = request.remote_addr
        
        # 如果当前 IP 地址不存在字典中，将该 IP 地址的请求次数设为0
        if client_ip not in ip_request_counts:
            ip_request_counts[client_ip] = 0
        
        # 如果该IP地址的请求次数超过10,返回超出请求限额的提示
        if ip_request_counts[client_ip] >= 10:
            return render_template('index.html', question=question, res="超出请求限额")
        
        ip_request_counts[client_ip] += 1
        
        res = get_completion(question)
        print("问题：\n", question)
        print("答案：\n", res)

        return render_template('index.html', question=question, res=str(res))
    return render_template('index.html', question=0)

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=80)
