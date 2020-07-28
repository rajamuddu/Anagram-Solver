from flask import Flask, request, render_template         # import flask
from anagram import anagrams
import re
app = Flask(__name__)             # create an app instance
app.config["DEBUG"] = True

@app.route("/",methods=["GET", "POST"])                   # at the end point /
def adder_page():
	errors=""
	if request.method=="POST":
		get_word=None
		p = re.compile('^[a-zA-Z]+$')
		get_word=request.form['word']
		input_word=p.match(get_word)
		if input_word is not None:
			return render_template("result.html", result=anagrams(get_word.lower()))
		else:
			errors += "{!r} is not a word. Please retry\n".format(request.form['word'])
			return render_template("error.html", e=errors)
	elif request.method=="GET":
		return render_template("home.html")
		
# Run the service on the local server it has been deployed to,
# listening on port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
