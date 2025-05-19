from flask import Flask
from src.logger import logging

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info("I am testing here my second method of logging")
    return "Welcome to Salary prediction by Priyanka Yadav"

if __name__ == "__main__":
    app.run(debug=True)

