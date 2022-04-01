from flask import Flask, render_template, request
from machinetranslation import translator

Flask_App = Flask(__name__)  # Creating our Flask Instance


@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')


@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    first_input = request.form['Input1']
    operation = request.form['operation']
    
    if operation=='fr':
        result=translator.englishToFrench(first_input)
    else:
        result=translator.frenchToEnglish(first_input)
    return render_template(
            'index.html',
            Input1=first_input,
            result=result,
            calculation_success=True
        )



if __name__ == '__main__':
    Flask_App.debug = False
    Flask_App.run()
