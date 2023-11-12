# This is a sample Python script.
import news_detect
import single_news_detect
from multiprocessing import Process
import argparse

parser = argparse.ArgumentParser(description='')

parser.add_argument('--port', type=int, default='7890')
parser.add_argument('--pageName', type=str, default='news_detect')
args = parser.parse_args()

if __name__ == '__main__':
    if args.pageName == 'news_detect':
        p2 = Process(target=news_detect.news_detect(args.port))
        p2.start()
    if args.pageName == 'single_news_detect':
        p1 = Process(target=single_news_detect.single_news_detect(args.port))
        p1.start()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
