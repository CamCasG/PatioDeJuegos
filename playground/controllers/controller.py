from playground import app
from flask import render_template

@app.route('/')
def welcome():
    return "Bienvenido, usa /play para comenzar a jugar!"

@app.route('/play')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def cajas():
    return render_template("index.html", num=3, color='blue')  

@app.route('/play/<int:num>')          
def cajas_num(num):
    return render_template("index.html", num=num, color='blue')

@app.route('/play/<int:num>/<color>')          
def cajas_color(num, color):
    return render_template("index.html", num=num, color=color)
