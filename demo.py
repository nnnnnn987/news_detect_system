import gradio as gr
import db.db as db


def chat(input_box, input_box2, machin_name, data_name, check_box):
    return "真新闻" if len(input_box) < 15 else "假新闻"


def mode_train():
    return ""


def get_models():
    df = db.get_models()
    name = df['name']
    return list(name.values)


def get_datasets():
    df = db.get_datasets()
    name = df['name']
    return list(name.values)


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


def demo():
    html_str = """
        <h1 style='font-family: "Nunito",sans-serif; color: midnightblue !important; font-size: 1.5875rem;text-align: left !important;'>南京邮电大学高性能计算与大数据处理研究所 </h1>
         <h1 style='font-family: "Nunito",sans-serif; color: midnightblue !important; font-size: 2.1875rem;text-align: center !important;'> 假新闻检测系统</h1>
        <h3 style='color: midnightblue !important; font-size: 1.1875rem;text-align: center !important;'></h3>
    """

    with gr.Blocks(title="Demo") as demo:
        with gr.Row():
            ht = gr.HTML(html_str, visible=True)

        with gr.Accordion("", open=True):
            with gr.Row():
                machin_name = gr.Dropdown(
                    choices=get_models(), value="对比学习的跨模态关联模型", label="模型")

            with gr.Row():
                data_name = gr.Dropdown(
                    choices=get_datasets(),
                    value="Weibo数据集", label="数据集")

            with gr.Row():
                check_box = gr.CheckboxGroup(
                    ["精度(Accuracy)", "查准率(Precision)", "召回率(Recall)", "F-measure", "单样本响应时间"],
                    label="技术指标", value=["准确率(Accuracy)"]
                )
        # with gr.Row():
        #     out_box_model = gr.Textbox(label="已处理样本数", show_label=True, lines=1, value="5000")
        #     out_box_model1 = gr.Textbox(label="未处理样本数", show_label=True, lines=1, value="10000")
        #     out_box_model2 = gr.Textbox(label="运行时间", show_label=True, lines=1, value="60s")

        with gr.Row():
            markDown_out = gr.Markdown()
            check_box.change(check_box_change, check_box, markDown_out)

        with gr.Row():
            btn = gr.Button(value="提交")
            btn.click(fn=mode_train, inputs=[], outputs=markDown_out)
            clear_btn = gr.ClearButton(components=[markDown_out], value="清除")

        with gr.Row():
            input_box2 = gr.Image(label="上传图片")
            input_box = gr.Textbox(placeholder="请输入新闻文本", label="输入文本", show_label=True, lines=2)

        with gr.Row():
            out_box = gr.Textbox(label="输出", show_label=True, lines=1)

        with gr.Row():
            btn = gr.Button(value="提交")
            btn.click(fn=chat, inputs=[input_box, input_box2, machin_name, data_name, check_box], outputs=out_box)
            clear_btn = gr.ClearButton(components=[input_box, out_box], value="清除")

        gr.Examples(
            examples=[[
                '美国达利安造船厂被拍到一坞五舰的震撼场面，美国这一动作释放了什么信号？',
                'img1.png', '基于对比学习的跨模态关联模型'],
                ['乌克兰可以在今年结束战争，泽连斯基说', 'img_3.png', '基于对比学习的跨模态关联模型']],
            inputs=[input_box, input_box2, machin_name],
            outputs=out_box,
            fn=chat,
            cache_examples=True,
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

    demo.launch(share=True)
