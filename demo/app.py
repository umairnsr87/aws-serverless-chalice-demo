from chalice import Chalice

# defining the name of our chalice app
app = Chalice(app_name='demo')

# Defining the logging
import logging
app.log.setLevel(logging.DEBUG)

# Lambda Function:1
@app.lambda_function(name="index")
def index(event,context):
    app.log.debug("Index first with event is {} and context is {}".format(event, context))
    from chalicelib.helper import invoke_lambda_function
    """
    Invocation of another lambda function
    """

    response = invoke_lambda_function(function_name='lambda-chalice-first',
                                      invocation_type='RequestResponse',#'Event': For ayncronous invocation
                                      data={"hello":"world"})

    return {'response': response}


# Lambda Function:2
@app.lambda_function(name="lambda-chalice-first")
def lambda_first(event,context):
    app.log.debug("Lambda first with event is {} and context is {}".format(event,context))
    return {'lambda-chalice-first': 'Hello! I am lambda-chalice-first'}




# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
