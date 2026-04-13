#  app.py
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
 
@app.route('/aboutus')
def aboutus():
     return "Welcome to the about us page\n"

@app.route('/faq')
def faq():
     return "Welcome to the FAQ page\n"

# 3. Run the Flask development server
if __name__ == '__main__':
   app.run(debug=True)
