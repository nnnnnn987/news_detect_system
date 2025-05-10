一、
#当前代码中没有处理数据库连接失败或查询错误的情况，这可能会导致程序崩溃或返回不友好的错误信息。我们可以添加异常处理机制，捕获可能的错误并进行适当的处理，如记录日志、返回默认值或重新连接等。
def fetch_data(table_name, columns=['*']):
    try:
        sql_cmd = f"SELECT {', '.join(columns)} FROM {table_name}"
        df = pd.read_sql(sql=sql_cmd, con=engine)
        return df
    except Exception as e:
        print(f"Error fetching data from {table_name}: {e}")
        # 可以选择记录日志、返回空 DataFrame 或重新抛出异常
        return pd.DataFrame()

二、p2 = Process(target=news_detect.news_detect, args=(args.port,))
p1 = Process(target=single_news_detect.single_news_detect, args=(args.port,))

三、import argparse
import logging
from multiprocessing import Process
import signal
import sys

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 全局进程列表
processes = []

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="新闻检测系统服务")
    parser.add_argument('--port', type=int, default=5000, help='服务端口号')
    return parser.parse_args()

def start_process(target_func, port, name):
    """启动子进程并记录日志"""
    try:
        p = Process(target=target_func, args=(port,), name=name)
        p.start()
        processes.append(p)
        logger.info(f"已启动进程 {name} (PID: {p.pid})")
        return p
    except Exception as e:
        logger.error(f"启动进程 {name} 失败: {e}")
        raise

def signal_handler(sig, frame):
    """处理终止信号，优雅关闭所有子进程"""
    logger.info(f"收到终止信号 {sig}，正在关闭所有进程...")
    for p in processes:
        if p.is_alive():
            p.terminate()
            p.join(timeout=2.0)
            if p.is_alive():
                logger.warning(f"进程 {p.name} 未能正常终止，强制终止")
                p.kill()
    logger.info("所有进程已关闭")
    sys.exit(0)

def main():
    try:
        # 解析命令行参数
        args = parse_args()
        logger.info(f"启动新闻检测系统，端口: {args.port}")

        # 导入服务模块
        import news_detect
        import single_news_detect

        # 注册信号处理函数
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        # 启动子进程
        start_process(news_detect.news_detect, args.port, "news_detect")
        start_process(single_news_detect.single_news_detect, args.port, "single_news_detect")

        # 主进程保持运行，等待信号
        logger.info("主进程已启动，按 Ctrl+C 终止")
        for p in processes:
            p.join()

    except KeyboardInterrupt:
        logger.info("用户手动终止程序")
    except Exception as e:
        logger.critical(f"程序异常终止: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # 确保所有进程都被清理
        for p in processes:
            if p.is_alive():
                p.terminate()

if __name__ == "__main__":
    main()