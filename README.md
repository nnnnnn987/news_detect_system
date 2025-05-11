# news_detect_system
一：project introduction
This project is a fake news detection system that evaluates the authenticity of news through machine learning models and datasets. The main functions include:
Multiple model selection: Users can choose different models and datasets to detect the authenticity of news.
Technical indicator display: The system can display the performance indicators of the model, such as accuracy, precision, recall, F-measure, and single sample response time.
Single sample testing: Users can upload images and input news text, and the system will provide detection results based on the selected model and dataset.
Web interface interaction: An interactive web interface was created using the Gradio library to facilitate user operation.

Two detection modes:
Batch News Detection Mode (news_detect. py) - Processing large amounts of news data
Single News Detection Mode (single_news_detect. py) - Analyze a single news item     <!-- by 黄明娟 -->


二：《new_detect.py》
1. Used to implement batch detection of fake news based on datasets.
A user interface was created using Gradio, which includes a model selection drop-down box, a dataset selection drop-down box, and a technical indicator checkbox.
After selecting the parameters, the user clicks the "submit" button and calls the mode_run function, which retrieves the model and dataset selected by the user. Then, the process function is called, and finally the check_ox_change function is called to generate and
Display the technical indicators and results of the testing.                        <!-- by 黄明娟 -->

2. Import module
gradio：A Python library for quickly creating interactive web interfaces. It allows users to create web applications with input-output functionality through simple code.          <!-- by 黄明娟 -->

3. Core functional functions
(1) process(mode_name, data_name, check_box)
Call the check_ox_change function to generate the corresponding HTML table based on the technical indicators selected by the user.
The entry function for processing detection requests receives the model name, dataset name, and selected metric parameters.   <!-- by 黄明娟 -->

(2) mode_run(mode_name, data_name, check_box)
Retrieve the model and dataset selected by the user, and call the process function to process these inputs.
Run the main function of the detection mode to obtain detailed information about the model and dataset, call process to process and return the result.        <!-- by 黄明娟 -->

(3) single_mode_run(data_set_dir)
Single sample detection function (currently implemented as placeholder), specific detection logic should be implemented in practical applications, currently fixed to return "real" (real news).               <!-- by 黄明娟 -->

4. auxiliary function 
(1) get_mode(mode_name)
Obtain detailed model information.      <!-- by 黄明娟 -->

(2) get_dataset(data_name)
Get detailed information about the dataset.      <!-- by 黄明娟 -->

(3) get_models()
Retrieve the list of available models from the database.
Return the list of model names.             <!-- by 黄明娟 -->

(4) get_datasets()
Retrieve the list of available datasets from the database
Return a list of dataset names.             <!-- by 黄明娟 -->

(5) check_box_change(inputs)
Generate result display based on user selected indicators
Currently returning a Markdown table in a fixed format
Includes sample processing statistics and performance indicators.          <!-- by 黄明娟 -->

5. Main interface function news_detect(port)
Function: Create a Gradio web interface where users can select models, datasets, and technical metrics, and submit requests to obtain performance metrics for the model.
Parameters:
Port: The port number on which the service is running.
Web interface layout:
HTML title: Display 'Fake News Detection System'.
Model selection: A dropdown menu where users can choose different models.
Dataset selection: A dropdown menu where users can choose different datasets.
Technical Indicator Selection: A checkbox group where users can select the technical indicators to be displayed.
Submit button: After clicking, the user calls the mode_run function to process the input and display the results.
Clear button: Clear the current output result.
Start service: Use the demo.launch method to start the Gradio service, set sharing options, server name, and port number.    <!-- by 黄明娟 -->

6. Current implementation characteristics
Simulated data: Currently, the displayed results are fixed simulated data, and the actual detection logic is yet to be implemented
Database integration: model and dataset information are obtained from the database
Responsive design: The interface will dynamically display results based on user selection
Multi indicator support: can choose to display detection indicators of different dimensions         <!-- by 黄明娟 -->

7. Part to be improved
Implementation of Actual News Detection Algorithm
Detailed configuration information of models and datasets
Dynamic calculation of detection results
More comprehensive visual display
User interaction experience optimization           <!-- by 黄明娟 -->