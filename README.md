<!DOCTYPE html>
<html>
<head>
</head>
<body>
    <h1>Data Collection Tool</h1>
  <img src="plant.jpg" alt="Plant Image">
    <p>Image source: <a href="https://www.freepik.com" target="_blank">Freepik</a></p>
    <p>This python-based data collection tool is designed to gather external data relevant to fertilizer inventory and demand planning. The tool is modular and scalable, allowing for easy integration of additional data sources for different agricultural products.</p>

  <h2>Dependencies</h2>
    <p>The required dependencies are listed in the <code>requirements.txt</code> file:</p>
    <ul>
        <li>pandas==2.2.2</li>
        <li>numpy==1.26.4</li>
        <li>requests==2.31.0</li>
        <li>faostat==1.1.2</li>
        <li>beautifulsoup4==4.12.3</li>
    </ul>
    <p>To install these dependencies, run the following command in your shell or command prompt:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

  <h2>Setup and Configuration</h2>
    <p>Before running the script, ensure that you have configured the <code>config.yaml</code> file correctly. This file should contain your API key and other required parameters. Here's an example of what the <code>config.yaml</code> might look like:</p>
    <pre><code>API: "YOUR_API_KEY_HERE"
id:
  - 101
  - 102
codes:
  - code1
  - code2
YEAR:
  - 2020
  - 2021
</code></pre>
<p>The reference file for <code>id</code> is <code>variables.csv</code> and for <code>codes</code> is <code>domain.csv</code>.</p>
<p>You may expand the list in the <code>config.yaml</code> file to add more <code>ids</code> and <code>codes</code> as needed, according to the reference files <code>variables.csv</code> and <code>domain.csv</code>, to access different datasets at the same time.</p>
<p>You may also expand the list of <code>YEAR</code> in the <code>config.yaml</code> file to include more years in the retrieved dataset.</p>

  <h2>Running the Script</h2>
    <p>To execute the data collection script, run the following command in your shell or command prompt:</p>
    <pre><code>py agdc.py</code></pre>

  <h2>Usage</h2>
    <p>The script performs the following tasks:</p>
    <ol>
        <li>Loads the configuration from <code>config.yaml</code>.</li>
        <li>Authenticates with the USDA API using the provided API key.</li>
        <li>Validates the provided variable IDs and codes.</li>
        <li>Retrieves data from the USDA API based on the specified years and variable IDs, and saves it as CSV files.</li>
        <li>Retrieves data from the FAO API based on the specified codes and years, and saves it as CSV files.</li>
    </ol>
    <p>The retrieved data will be saved in the <code>data_csv</code> directory.</p>

  <h2>Documentation</h2>
    <p>Ensure that the following files are present and correctly set up:</p>
    <ul>
        <li><code>requirements.txt</code>: Lists all the required dependencies.</li>
        <li><code>config.yaml</code>: Configuration file with API key, variable IDs, codes, and years.</li>
        <li><code>agdc.py</code>: Main script for data collection.</li>
    </ul>
    <p>For more detailed documentation, please refer to the comments within the <code>agdc.py</code> script.</p>

  <h2>Troubleshooting</h2>
    <p>If you encounter any issues, please check the following:</p>
    <ul>
        <li>Ensure your API key is correct and has access to the required endpoints.</li>
        <li>Verify that your configurations in <code>config.yaml</code> is correct.</li>
        <li>Check the console output for any error messages and follow the instructions provided.</li>
    </ul>

<h2>Additional Notes</h2>
    <ul>
        <li>Configuration File: The <code>config.yaml</code> file should be correctly formatted and include all required fields.</li>
        <li>Execution: The script should be executed with the command <code>py agdc.py</code> or <code>python agdc.py</code> depending on your Python installation.</li>
    </ul>

<h2>Video Tutorial</h2>
    <p>For a complete walkthrough of the repository setup, execution, and data interpretation, watch the video tutorial
    <a href="https://youtu.be/nL8vVXgSArY" target="_blank">here</a></p>

  <h2>Contact</h2>
    <p>For any questions or further assistance, please contact me <a href="mailto:aasuranjan2k15@gmail.com">here</a>.</p>
</body>
</html>
