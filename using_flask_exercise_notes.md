Going back to the calculator for this exercise

Remember to keep main.py clean, other things stored in other files and then imported.

Next, converting the calculator to a web app using Flask. Instead of inputting the numbers via command line, it will be added from a browser.

to isntall flask, use `pip install flask`

Other useful commands:

`export FLASK_APP=calculator/main
`

`export FLASK_ENV=development`


When runnign flask, you will issue just the flask_run command. It will then search for the files it needs to serve. therefore, it is necessary to point flask to the files that are used to serve the functions, in our case the calculator's main.py

In short, we are giving a pointer to flask to show where the code can be found

by setting FLASK_ENV to development, we get a lot more feedback and debugging information. if setting to production for example, the debuggin information would not be set.

Next up, enter `flask run`

Notice a few alterations to the python file are necessary

Of course, the Flask class needs importing, using `from flask import Flask`
when running via  subdirectory need to import calculator functions via `import calculator.calc_functions`

Also necessary to make sure a `__init__.py` file is in each directory python should search for code.

So, recap of what was jsut done

- created an app
- passed main to flask


Needed to set subURLs using, for example:

`@app.route('/')` is the default page


`@app.route('/add')` for add. 


However, notice that if just calling the /add url, an error will be thrown as there is no input

would need to change this to become 
`@app.route@app.route('/add/<int:number1>/<int:number2>')`

the output has to be in the correct format, so the return statement has to be assigned to a string type. with this, the url `http://127.0.0.1:5000/add/1/1` would return 2 for example.

```python
@app.route('/add/<int:number1>/<int:number2>')
def perform_add(number1, number2):
    return str(calc_functions.add(number1, number2))

```

next, tryign to use a query string. this requires adding a new function, and adding the import of request from flask.

```python
@app.route('/add')
def perform_add_query():
    number1 = request.args.get('num1', type=int)
    number2 = request.args.get('num2', type=int)
    return str(calc_functions.add(number1, number2))
    return str(calc_functions.add(number1, number2))
```

the new function takes in a query string after the /add. for example `http://127.0.0.1:5000/add?num1=5&num2=8` will return 13.


Adding error handling.

If the user was to try submitting a query string with non-integers, can use abort from flask to handle this, for example by adding into perform_add_query:

```python
    if number1 is None or number2 is None:
        abort(404)
```


can also add a default option, so that if hte user inputs nothing the default can be returned. Added into the definition of the request, such as `number1 = request.args.get('num1', type=int, default = 0)`.

Can also hand out standard error codes to let the user know what is going wrong using the number passed to abort. Lists of these are available online, see for example https://httpstatuses.com
