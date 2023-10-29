# This is a sample Python script.
import news_detect
import single_news_detect
from multiprocessing import Process

if __name__ == '__main__':
    p1 = Process(target=single_news_detect.single_news_detect())
    # p2 = Process(target=news_detect.news_detect())
    p1.start()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
