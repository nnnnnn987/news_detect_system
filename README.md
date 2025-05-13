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







# Project Introduction              <!-- by 刘巧来 -->

This project is a fake news detection system that evaluates the authenticity of news through machine learning models and datasets. Its main functions include:

- **Multiple model selection**: Users can choose different models and datasets to detect the authenticity of news.
- **Technical indicator display**: The system can display the performance indicators of the model, such as precision, precision rate, recall rate, F-measure, and single sample response time.
- **Single sample testing**: Users can upload pictures and input news text, and the system will give detection results according to the selected model and dataset.
- **Web interface interaction**: The Gradio library is used to create an interactive Web interface for convenient user operation.

## File Function Explanation

### misc.xml, Modules.xml, News_detect_system.iml, Vcs.xml

- **misc.xml**: Contains project configurations and settings that are not covered by other files.
- **Modules.xml**: Defines the project's module structure, including dependencies and configurations between modules.
- **News_detect_system.iml**: An IntelliJ IDEA project file that contains project metadata and configuration information.
- **Vcs.xml**: A version control system configuration file that manages version control settings within the project.

## db.py Code Explanation

- **Main Functions**:
  - Explains the functions of some main codes in the `db.py` file.
  - Adds error management code, including an exception handling mechanism to capture possible errors and perform appropriate handling, such as logging, returning default values, or reconnecting.

- **Deficiencies**:
  - Lack of single responsibility and reusability of functions.
  - Fails to handle situations like database connection failures or query errors, which may cause the program to crash or return unfriendly error messages.

- **Improvements**:
  - The exception handling mechanism enables the program to promptly capture various exceptions during operation, such as database connection errors, network request timeouts, and file read/write errors.
  - Takes corresponding handling measures according to different types of exceptions to prevent the program from crashing due to exceptions.

## Main.py Code Explanation

- **Main Functions**:
  - Explains the functions of some main codes in the `Main.py` file.

- **Current Limitation**:
  - Currently, the code can only start one page module.

- **Suggested Expansion**:
  - Can be expanded to support starting multiple page modules simultaneously.
  - Starting multiple page modules at the module level allows for the full utilization of the computer's multi-core processor resources.
  - Enables parallel processing of different news detection tasks.
  - Improves the overall efficiency and performance of the news detection system.         <!-- by 刘巧来 -->







# news_detect_system <!-- by 黄明娟 -->

## Project Introduction

This project is a fake news detection system that evaluates the authenticity of news through machine learning models and datasets. The main functions include:

- **Multiple model selection**: Users can choose different models and datasets to detect the authenticity of news.
- **Technical indicator display**: The system can display the performance indicators of the model, such as accuracy, precision, recall, F-measure, and single sample response time.
- **Single sample testing**: Users can upload images and input news text, and the system will provide detection results based on the selected model and dataset.
- **Web interface interaction**: An interactive web interface was created using the Gradio library to facilitate user operation.

There are two detection modes:
- **Batch News Detection Mode** (`news_detect.py`): Processing large amounts of news data.
- **Single News Detection Mode** (`single_news_detect.py`): Analyzing a single news item.

## `news_detect.py`

### 1. Overview

Used to implement batch detection of fake news based on datasets. A user interface was created using Gradio, including a model selection drop-down box, a dataset selection drop-down box, and a technical indicator checkbox. After selecting the parameters, the user clicks the "submit" button to call the `mode_run` function, which retrieves the model and dataset selected by the user. Then, the `process` function is called, and finally the `check_box_change` function is called to generate and display the technical indicators and results of the testing.

### 2. Import Module

- **`gradio`**: A Python library for quickly creating interactive web interfaces. It allows users to create web applications with input-output functionality through simple code.

### 3. Core Functional Functions

1. **`process(mode_name, data_name, check_box)`**
   - Calls the `check_box_change` function to generate the corresponding HTML table based on the technical indicators selected by the user.
   - The entry function for processing detection requests, receiving the model name, dataset name, and selected metric parameters.

2. **`mode_run(mode_name, data_name, check_box)`**
   - Retrieves the model and dataset selected by the user and calls the `process` function to process these inputs.
   - Runs the main function of the detection mode to obtain detailed information about the model and dataset, calls `process` to process and return the result.

3. **`single_mode_run(data_set_dir)`**
   - Single sample detection function (currently implemented as a placeholder). Specific detection logic should be implemented in practical applications. Currently, it fixedly returns "real" (real news).

### 4. Auxiliary Functions

1. **`get_mode(mode_name)`**
   - Obtains detailed model information.

2. **`get_dataset(data_name)`**
   - Gets detailed information about the dataset.

3. **`get_models()`**
   - Retrieves the list of available         <!-- by 黄明娟 -->