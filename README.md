# news_detect_system
# Fake News Detection System        <!-- by 韦玉雪 -->

## Overview
A web interface for fake news detection using multimodal analysis (text + images). Currently a demo with simulated results.

## Features
- Interactive Gradio interface
- Model/dataset selection
- Performance metrics display
- Example inputs
- Single news verification

## How to Use
1. Install requirements: `pip install gradio`
2. Run: `python script.py`
3. Access the web interface
4. Either:
   - Select model/dataset and enter text + image
   - Use provided examples
5. View "detection" results (currently simulated)

## Technical Notes
- Placeholder detection logic (always returns "real")
- Sample models/datasets are listed but not fully implemented
- Performance stats are hardcoded                       <!-- by 韦玉雪 -->







 <!-- by 刘巧来 -->
Explain the main functions of the misc.xml, Modules.xml, News_detect_system.iml, and Vcs.xml files, laying the foundation for the subsequent code execution.
In the db.py code, explain the functions of some main codes. We think there are still some deficiencies in this code, such as the lack of single responsibility and reusability of functions. Also, it fails to handle situations like database connection failures or query errors, which may cause the program to crash or return unfriendly error messages. Therefore, we add error management code to this code, including an exception handling mechanism. This mechanism can capture possible errors and perform appropriate handling, such as logging, returning default values, or reconnecting. This enables the program to promptly capture various exceptions that occur during the program's operation, such as database connection errors, network request timeouts, file read and write errors, etc. And corresponding handling measures are taken according to different types of exceptions to avoid the program from crashing due to exceptions.
In the Main.py code, explain the functions of some main codes. Currently, the code can only start one page module. We can expand it to support starting multiple page modules simultaneously. By starting multiple page modules at the module, we can fully utilize the multi-core processor resources of the computer, achieve parallel processing of different news detection tasks, and thus improve the overall efficiency and performance of the news detection system.
Project Introduction
This project is a fake news detection system that evaluates the authenticity of news through machine learning models and datasets. Its main functions include:
Multiple model selection: Users can choose different models and datasets to detect the authenticity of news.
Technical indicator display: The system can display the performance indicators of the model, such as precision, precision rate, recall rate, F-measure, and single sample response time.
Single sample testing: Users can upload pictures and input news text, and the system will give detection results according to the selected model and dataset.
Web interface interaction: The Gradio library is used to create an interactive Web interface for convenient user operation. <!-- by 刘巧来 -->