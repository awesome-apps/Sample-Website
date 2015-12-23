document.body.style.backgroundColor = "rgb(0, 115, 255)";
var tag = document.getElementsByTagName("p")[0];
text = tag.innerHTML;
// Here I would like to call the Python interpreter with Python function
arrOfStrings = openSomehowPythonInterpreter("~/client.py", "stuff()");

~/client.py
