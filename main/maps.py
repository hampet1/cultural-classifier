from flask import Blueprint, render_template
from flask_login import current_user, login_required

maps = Blueprint('maps', __name__)



@maps.route("/map")
@login_required
def map():
    """
    maps main page

    """
    return render_template('maps/map.html', user=current_user, page="maps")


@maps.route("/clustermap")
@login_required
def clustermap():
    """
        display all archeological sites from our database related to
        epiaurignacian and epigracettian
        clustermap
    """
    return render_template('maps/clustermap.html', user=current_user)


@maps.route("/heatmap")
@login_required
def heatmap():
    """
        display all archeological sites from our database related to
        epiaurignacian and epigracettian
        heatmap
    """
    return render_template('maps/heatmap.html', user=current_user)
