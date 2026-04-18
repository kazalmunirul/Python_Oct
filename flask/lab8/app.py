from flask import Flask, render_template, request # Import request
app = Flask(__name__)
@app.route('/')
def form_page():
 return render_template('submit_name.html') # Serve the page with the form
@app.route('/submit',methods=['POST']) # This route handles the GET request from the first form
def handle_submission_post():
    return request.form # Print the form data to the console for debugging
#  fullname = request.form.get('fullname')
#  email = request.form.get('email')
#  gender = request.form.get('gender')
#  course = request.form.get('courses')

#  if fullname and email:
#   return (
#       f"<h1>Registration Successful!</h1>"
#       f"<ul>"
#       f"<li>Name: {fullname}</li>"
#       f"<li>Email: {email}</li>"
#       f"<li>Gender: {gender}</li>"
#       f"<li>Course: {course}</li>"
#       f"</ul>"
#   )
#  return "<h1>Please fill out all required fields!</h1>"

if __name__ == '__main__':
 app.run(debug=True)