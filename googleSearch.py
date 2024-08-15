from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/gsearch/<inputpara>")
def gsearch(inputpara):
    from googlesearch import search
    r = []
    count = 0
    for j in search(inputpara):
        r.append(j)
        count += 1
        if count == 5:
            break
    result_html = "<br>".join(r)
    return result_html
    
app.run(port=80,host="0.0.0.0")
