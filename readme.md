<!--
Readme.md er skrevet i markdown.
For å rendre dette til Html må du åpne filen i en nettleser med en markdown plugin (f.eks. "Markdown Viewer" i Chrome)
-->


# Introduction
Python flask web app that takes a IIS log file, strips away garbage, and presents a graph of which IP addresses that has the most requests towards the IIS web site.


# How to get it running

1. Install Python (v3)
2. Navigate to the root folder of this project (e.g. `C:\iis_loganalyse`)
3. Create a new virtual environment with venv in the project folder:
    * `python -m venv C:\iis_loganalyse\`
4. Activate virtual environment
    * `.\Scripts\activate`
5. Install required packages in your virtual environment
    * `pip install -r requirements.txt`
6. Navigate to `flask_app\` and run `python app.py` to start the web server
7. The command line output should show which URL to navigate to (default http://localhost:5000)

# Todos

* In the first version of this web app, the file name of the IIS log file is hardcoded into `parse_iislog.py`. Feel free to modify this at any time :)
Ideally, the user should be able to provide a log file in the browser.

* The number of IP addresses to be displayed in the graph and the table below is hardcoded into the variable `number_of_bars` in  `parse_iislog.py`. The user should be able to adjust this in the browser.
