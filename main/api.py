from flask import Blueprint, request, current_app, jsonify
import numpy as np
import pandas as pd

# creating api blueprint
api = Blueprint('api', __name__)


@api.route('/api/', methods=['POST', 'GET'])
def make_prediction():
    """
    creating prediction - using api
    using array2string method converting int64 into serializable object
    """
    model = current_app.config['MODEL']
    data = request.get_json()
    result = pd.DataFrame([data], columns=['ter_var_small', 'ter_var_big', 'elevation', 'distance',
                                           'viewshed', 'norm_height'])
    # array2string returns a string representation of an array, we can't use int64 because it's not serializable
    result = np.array2string(model.predict(result)[0])
    return jsonify(result)
