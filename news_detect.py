import gradio as gr
import db.db as db


def process(mode_name, data_name, check_box):
    return check_box_change(check_box)


def mode_run(mode_name, data_name, check_box):
    mode = get_mode(mode_name)
    dataSet = get_dataset(data_name)
    return process(mode, dataSet, check_box)


def single_mode_run(data_set_dir):
    return "real"


def get_mode(mode_name):
    return "mode_name"


def get_dataset(data_name):
    return "data_name"


def get_models():
    df = db.get_models()
    name = df['name']
    return list(name.values)
    # return ["基于对比学习的跨模态关联模型", '基于图网络的多域自适应模型']


def get_datasets():
    df = db.get_datasets()
    name = df['name']
    return list(name.values)
    # return ["Weibo数据集", "Fakeddit数据集"]


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


def news_detect(port):
    # ' <h1 style='font-family: "Nunito",sans-serif; color: midnightblue !important; font-size: 1.5875rem;text-align: left !important;'>南京邮电大学高性能计算与大数据处理研究所 </h1>'
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

            with gr.Row():
                check_box = gr.CheckboxGroup(
                    ["精度(Accuracy)", "查准率(Precision)", "召回率(Recall)", "F-measure", "单样本响应时间"],
                    label="技术指标", value=["准确率(Accuracy)"]
                )

        # 结果输出
        with gr.Row():
            markDown_out = gr.Markdown()

        with gr.Row():
            btn = gr.Button(value="提交")
            btn.click(fn=mode_run, inputs=[model_name, data_name, check_box], outputs=markDown_out)
            clear_btn = gr.ClearButton(components=[markDown_out], value="重置")

    demo.launch(share=True,server_name='0.0.0.0', server_port=port)
