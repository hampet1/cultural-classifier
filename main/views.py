from flask import render_template, request, Blueprint, flash, current_app, redirect, url_for
from flask_login import current_user, login_required
import pandas as pd



views = Blueprint('views', __name__)



@views.route('/')

def home():
    return render_template("public/index.html", user=current_user, page="home")


@views.route('/about-project')
def about_project():
    return render_template("public/about.html", user=current_user, page="about_project")


@views.route('/guideline')
def guideline():
    return render_template("public/guideline.html", user=current_user, page="guideline")


@views.route('/classifier', methods=['POST', 'GET'])
def classify():
    """
    distinguish epig and eau based on geographical data
    function is converting list to dataframe to prevent it from mismatch error
    we are setting up some limitation for entered values
    as a result of this function classification result is rendered
    """
    model = current_app.config['MODEL']
    if request.method == 'POST':
        try:
            elevation = int(request.form['elevation'])
            distance = int(request.form['distance'])
            height = float(request.form['height'])
            viewshed = int(request.form['viewshed'])
            tw_short = int(request.form['terrain_short'])
            tw_long = int(request.form['terrain_long'])
        except ValueError:
            flash("you have to enter a number not a string or other characters", category="error")
            return render_template('public/index.html', user=current_user)

        if (tw_short < 0 or tw_short > 200):
            flash("terrain short value is out of range, the value is supposed be between 0 and 200", category="error")
            return render_template('public/index.html', user=current_user)
        elif (tw_long < 0 or tw_long > 400):
            flash("terrain long value is out of range, the value is supposed be between 0 and 400", category="error")
            return render_template('public/index.html',user=current_user)
        elif (elevation < 0 or elevation > 4000):
            flash("elevation is out of range, the value is supposed be between 0 and 4000", category="error")
            return render_template('public/index.html', user=current_user)
        elif (distance < 0 or distance > 100000):
            flash("distance is out of range, the value is supposed be between 0 and 100000", category="error")
            return render_template('public/index.html', user=current_user)
        elif (viewshed < 0 or viewshed > 1000000):
            flash("viewshed is out of range, the value is supposed be between 0 and 1000000", category="error")
            return render_template('public/index.html', user=current_user)
        elif (height < 0 or height > 1):
            flash("height is out of range, the value is supposed be between 0 and 1", category="error")
            return render_template('public/index.html', user=current_user)
        else:
            values = [tw_short, tw_long, elevation, distance, viewshed, height]

            result = pd.DataFrame([values], columns=['ter_var_small', 'ter_var_big', 'elevation', 'distance',
                                                 'viewshed', 'norm_height'])
            result = model.predict(result)[0]

            return render_template('public/classification.html', classification=result, user=current_user)
    else:

        flash("something went wrong", category="error")
        return redirect(url_for('views.home'))
