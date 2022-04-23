from flask import Flask,request, render_template
app=Flask(__name__,template_folder="templates")
from bs4 import BeautifulSoup
import requests



source=requests.get("https://en.wikipedia.org/wiki/Tourism_in_India")
s = source.text
soup=BeautifulSoup(s,'html.parser')

print(soup)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/abc', methods=[ 'GET','POST'])
def my_form_post():
    text = request.args.get('lname')
    source=requests.get("https://en.wikipedia.org/wiki/"+text)
    s = source.text
    soup=BeautifulSoup(s,'html.parser')
    f = open("/templates/result.html", 'a')
    f.truncate()
    f.write(soup)
    f.close()

    print(soup)
    print(text)
    return render_template("result.html")


if __name__ == '__main__':
    app.run(debug=True)
