from flask import Flask
from flask import render_template
import parse_iislog

app = Flask(__name__)

@app.route("/")
def hello():
    plot_data = parse_iislog.run_parse()

    #return plot_data
    return render_template('base.html',data=plot_data, cat=list(plot_data.keys()), dat=list(plot_data.values()))
    
if __name__ == "__main__":
    app.run()