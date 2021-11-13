# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import joblib
from flask import Flask,render_template, request


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

  
@app.route('/home')
# ‘/’ URL is bound with app
def home():
    return render_template('index.html')
   
@app.route('/predict' , methods = ['POST'])  
def predict():
    preg =int(request.form.get('preg')) 
    plas = int(request.form.get('plas'))
    pres =int(request.form.get('pres'))
    skin =int(request.form.get('skin'))
    test =int(request.form.get('test'))
    mass = int(request.form.get('mass'))
    pedi = int(request.form.get('pedi'))
    age = int(request.form.get('age'))
    
    loaded_model=joblib.load('dib_78.pkl')
    prediction = loaded_model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if prediction[0]==1:
        print('dibatic')
        val = 'dibatic'
    else:
        print('not dibatic')
        val = 'not dibatic'

    return render_template("homepage.html", value = val)

    #print(loaded_model.predict([[10,20,30,4,5,6,8,9]]))

def __getitem__(self,index):
    return self.bricks.bricksId[index]

def __setitem__(self,index,value):
    self.bricks.bricksId[index] = value


   # main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()