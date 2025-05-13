<!-- by 刘巧来 -->

# Code Enhancements and Explanations

## One、Enhancing Database Operations with Exception Handling

# 当前代码中没有处理数据库连接失败或查询错误的情况，这可能会导致程序崩溃或返回不友好的错误信息。我们可以添加异常处理机制，捕获可能的错误并进行适当的处理，如记录日志、返回默认值或重新连接等。
def fetch_data(table_name, columns=['*']):
    try:
        sql_cmd = f"SELECT {', '.join(columns)} FROM {table_name}"
        df = pd.read_sql(sql=sql_cmd, con=engine)
        return df
    except Exception as e:
        print(f"Error fetching data from {table_name}: {e}")
        # 可以选择记录日志、返回空 DataFrame 或重新抛出异常
        return pd.DataFrame()

## Two、Multiprocessing for Parallel Execution

p2 = Process(target=news_detect.news_detect, args=(args.port,))
p1 = Process(target=single_news_detect.single_news_detect, args=(args.port,))

## Three、Main Script with Logging and Graceful Shutdown

import argparse
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
<!-- by 刘巧来 -->






<!-- by 黄明娟 -->
# 项目问题与优化

## 1. 项目搭建与环境配置问题

- **问题**：在搭建项目时，遇到了依赖库安装的问题。运行 `pip install -r requirement.txt` 命令安装项目所需的 gradio、sqlalchemy、pymysql、pandas 库时，出现 gradio 库版本不兼容导致部分功能无法正常使用的情况。
- **AI 给的回答**：不同版本的 gradio 库在接口和功能实现上可能存在差异，当前项目代码可能依赖于特定版本的接口，而安装的版本不匹配。
- **我的解决方法**：我参考 AI 提供的 gradio 官方文档，确定了项目所需的 gradio 库的准确版本，重新安装了指定版本的 gradio 库。

## 2. 代码理解与函数逻辑分析

- **问题**：对于 `news_detect.py` 中 `get_mode` 和 `get_dataset` 函数的具体实现逻辑存在疑问，不清楚如何从数据库中准确获取模型和数据集的详细信息。
- **AI 给的回答**：询问 AI 后得知，`db.db` 模块中的 `get_models` 和 `get_datasets` 函数负责从数据库读取数据，`get_mode` 和 `get_dataset` 函数只是简单返回固定字符串，在实际应用中应修改为调用 `db.db` 模块函数获取真实数据。
- **优化方向**：在 AI 的指导下，理解了整个数据获取的流程，明确了后续完善这部分代码的方向。

## 3. 界面交互功能优化思考

- **优化目标**：考虑优化假新闻检测系统的界面交互功能，比如添加更多的示例数据，让用户能更直观地体验系统功能。
- **AI 建议**：向 AI 咨询实现思路，AI 建议利用 `gr.Examples` 组件，在 `single_news_detect.py` 中已有示例的基础上，根据不同模型和数据集的特点，增加更多具有代表性的新闻文本和图片示例，同时调整示例的展示布局，以提高用户体验。

## 4. 响应时间优化

- **问题**：系统单样本响应时间较长影响用户体验。
- **AI 分析与建议**：经 AI 分析，可能是模型加载和数据处理耗时。AI 建议优化数据库查询语句，采用缓存机制减少重复查询。
- **优化结果**：依此对 `db.db` 模块查询函数优化，添加数据缓存功能，测试后单样本响应时间明显缩短。

## 5. 资源占用优化

- **问题**：运行过程中系统内存占用较高。
- **AI 分析**：AI 指出可能存在内存泄漏或资源未及时释放。
- **解决方法**：借助 AI 推荐的性能分析工具，定位到部分函数中数据处理后未释放内存问题。
<!-- by 黄明娟 -->
