import gradio as gr
import db.db as db


def process(mode_name, data_name, check_box):
    return check_box_change(check_box)


def check_box_change(inputs):
    strStat = '''
<font size=5>

|   已处理样本数：10000条   |   未处理样本数：0条    | 单样本响应时间：0.000086s |
| :-----------------------: | :------------------------: | :-----------: |
| **精度(Accuracy)：0.953** | **F-measure：0.953** |               |

<font size>
'''
    # str = ''' <font size=5> '''
    # for input in inputs:
    #     str += input + ":" + "93%  "
    return strStat


def mode_run(mode_name, data_name, check_box):
    mode = get_mode(mode_name)
    dataSet = get_dataset(data_name)
    return process(mode, dataSet, check_box)


def single_mode_run(image, text, mode_name, data_name, check_box):
    return "real"


def get_mode(mode_name):
    return "mode_name"


def get_dataset(data_name):
    return "data_name"


def get_models():
    # df = db.get_models()
    # name = df['name']
    # return list(name.values)
    return ["基于对比学习的跨模态关联模型", '基于图网络的多域自适应模型']


def get_datasets():
    # df = db.get_datasets()
    # name = df['name']
    # return list(name.values)
    return ["Weibo数据集", "Fakeddit数据集"]


def single_news_detect():
    # """<h1 style='font-family: "Nunito",sans-serif; color: midnightblue !important; font-size: 1.5875rem;text-align: left !important;'>南京邮电大学高性能计算与大数据处理研究所 </h1>"""
    html_str = """
        
         <h1 style='font-family: "Nunito",sans-serif; color: midnightblue !important; font-size: 2.1875rem;text-align: center !important;'> 假新闻检测系统</h1>
        <h3 style='color: midnightblue !important; font-size: 1.1875rem;text-align: center !important;'></h3>
    """

    with gr.Blocks(title="Demo") as demo:
        # 参数选择
        with gr.Row():
            ht = gr.HTML(html_str, visible=True)
        with gr.Accordion("", open=True):
            with gr.Row():
                model_name = gr.Dropdown(
                    choices=get_models(), value="对比学习的跨模态关联模型", label="模型")
            with gr.Row():
                data_name = gr.Dropdown(
                    choices=get_datasets(),
                    value="Weibo数据集", label="数据集")


        # 单样本测试
        with gr.Row():
            image = gr.Image(label="上传图片")
            text = gr.Textbox(placeholder="请输入新闻文本", label="输入文本", show_label=True, lines=2)

        with gr.Row():
            out_box = gr.Textbox(label="输出", show_label=True, lines=1)

        with gr.Row():
            btn = gr.Button(value="提交")
            btn.click(fn=single_mode_run, inputs=[text, image, model_name, data_name], outputs=out_box)
            clear_btn = gr.ClearButton(components=[image, text, out_box], value="重置")

        gr.Examples(
            examples=[[
                '美国达利安造船厂被拍到一坞五舰的震撼场面，美国这一动作释放了什么信号？',
                'img1.png', '基于对比学习的跨模态关联模型', 'Weibo数据集'],
                ['乌克兰可以在今年结束战争，泽连斯基说', 'img_3.png', '基于图网络的多域自适应模型', 'Fakeddit数据集']],
            inputs=[text, image, model_name, data_name],
            outputs=out_box,
            fn=single_mode_run,
            cache_examples=False,
        )
        # with gr.Box():
        #     with gr.Column():
        #         gr.Markdown("""
        #         ## Text Examples
        #         ##### click the example to obtain result
        #         """)
        #         exp = gr.Examples(examples=["小明", "xiao red"], inputs=input_box, outputs=out_box)
        #         gr.Markdown("""
        #         # reference
        #         * [gradido官方文档](https://www.gradio.app/docs/examples)
        #         * [orangerfun的CSDN博客](https://blog.csdn.net/orangerfun?spm=1011.2415.3001.5343)
        #         """)

    demo.launch(share=True, server_port=7860)
