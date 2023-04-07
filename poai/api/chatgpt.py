# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/2/8 23:39
@Description     ：
'''
import openai


def chat(api_key, prompt, model_engine="gpt-3.5-turbo"):
    # 设置 API Key
    openai.api_key = api_key  # your_api_key

    # completions = openai.Completion.create(
    #     engine=model_engine,
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )
    # 获取 ChatGPT 的回复
    # message = completions.choices[0].text

    res = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "you are a wonderful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    message = res["choices"][0]["message"]["content"]
    print(message)
    return message
