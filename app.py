from flask import Flask, url_for, redirect, render_template, request
import openai


app = Flask(__name__)

api="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"
openai.api_key = api
model_engine = "text-davinci-003"


    
@app.route("/", methods=["POST", "GET"])
def main():
    #return "<h1 style='color:red'>Poogle</h1>"
    if request.method == "POST":
        prompt = request.form["nm"]
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5, 
        )
        response = completion.choices[0].text
        #return f"<h2> { response } </h2> "
        return render_template("poogle.html", response=response)
       
    else:
        return render_template("index.html")



app.run(debug=True)