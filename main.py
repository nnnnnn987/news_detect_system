# This is a sample Python script.
import news_detect
import single_news_detect
from multiprocessing import Process
import argparse

parser = argparse.ArgumentParser(description='')#用于处理命令行参数。目前描述为空，可以补充说明该脚本的作用。

parser.add_argument('--port', type=int, default='7860')
parser.add_argument('--pageName', type=str, default='news_detect')
args = parser.parse_args()#命令行参数，并将结果存储在 args 对象中。

#确保以下代码块仅在脚本直接运行时执行，而不是在被导入时执行。
if __name__ == '__main__':
    if args.pageName == 'news_detect':
        p2 = Process(target=news_detect.news_detect(args.port))
        p2.start()
    if args.pageName == 'single_news_detect':
        p1 = Process(target=single_news_detect.single_news_detect(args.port))
        p1.start()

#目前代码只能启动一个页面模块，我们觉得可以扩展支持同时启动多个页面模块。
if __name__ == '__main__':
    processes = []
    try:
        if args.pageName == 'news_detect':
            function = import_module_function('news_detect', 'news_detect')
            p = Process(target=function, args=(args.port,))
            p.start()
            processes.append(p)
            logging.info(f"新闻检测模块已启动，端口：{args.port}")
        if args.pageName == 'single_news_detect':
            function = import_module_function('single_news_detect', 'single_news_detect')
            p = Process(target=function, args=(args.port,))
            p.start()
            processes.append(p)
            logging.info(f"单条新闻检测模块已启动，端口：{args.port}")
        # 等待所有进程完成
        for p in processes:
            p.join()
    except Exception as e:
        logging.error(f"启动模块时出错：{e}")
        for p in processes:
            p.terminate()
        sys.exit(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
