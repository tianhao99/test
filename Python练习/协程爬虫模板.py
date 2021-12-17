# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 08:38:33 2021

@author: kingb
"""
import  time
import asyncio
async def download(url):
    print("开始抓取")
    await asyncio.sleep(3) # 我要开始下载了
    print("下载结束", url)
    return "⽼⼦是源码你信么"
async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.h.com",
        "http://luoyonghao.com"
        ]
 # ⽣成任务列表
    tasks = [download(url) for url in urls]
    done, pedding = await asyncio.wait(tasks)
    for d in done:
        print(d.result())
if __name__ == '__main__':
    asyncio.run(main())