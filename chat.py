import openai

// 这里填写从OpenAI官网申请的API密钥
openai.api_key = "xxxxxxxxxxxxx"


def generate_prompt(payload):
    return payload + "."


print("")
print("### 嗨～请告诉我你的问题，我会尽力帮你解答～")
print("### 使用方法：")
print(">>> 一、启动模式：")
print("    0、陪聊模式")
print("    1、代码模式")
print(">>> 二、聪明程度：")
print("    0、智障模式")
print("    1、智慧模式")
print(">>> 三、结束程序：")
print("    输入'#'退出程序")

mode = input(">>> 请选择启动模式: ")
if mode == "'#'":
    exit(0)
if mode != '0' and mode != '1':
    print(">>> 乱输入！不给你用了！")
    exit(0)

model = ""
if mode == '0':
    model = "text-davinci-003"
else:
    model = "code-davinci-002"

intelligence = input(">>> 请选择聪明程度: ")
if intelligence == "'#'":
    exit(0)
if intelligence != '0' and intelligence != '1':
    print(">>> 又乱输入！我生气了！拜拜！！！")
    exit(0)

temperature = 0
if intelligence == 0:
    temperature = 0.1
else:
    temperature = 0.7

print(">>> 好啦！告诉我你的问题吧！\n")

while True:
    content = input(">>> 写在这里: ")
    if content == "'#'":
        print("嘿嘿～没想到是'#'吧！拜拜～")
        exit(0)
    response = openai.Completion.create(
        model=model,
        prompt=generate_prompt(content),
        temperature=temperature,
        n=1,
        max_tokens=2048,
        presence_penalty=1,

    )
    print("\n>>> " + response.choices[0].text + "\n")
