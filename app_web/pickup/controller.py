from flask import Blueprint,render_template,request
import os
import time
#
from app.pfe_classe import pickup
#
pickup_blueprint = Blueprint(
    'pickup',
    __name__,
    url_prefix= '/pickup',
    static_folder='../static',
    template_folder='../templates'
)
#
pick = None
#
@pickup_blueprint.route('/',methods=['GET','POST'])
def index():
    #
    global pick
    #
    if request.method == 'POST':
        #
        vehicule = int(request.form['v'])
        cout = request.form['c']
        #
        path = '../amiraTafsoutPickup/templates/cluster.html'
        if (os.path.exists(path)):
            #
            os.remove(path)
        ######### tlbo clarck right #######
        #
        pick = pickup(vehicule)
        pick.tokanization()
        pick.create_distance_matrix()
        #
        #
        pick.Recouvrement()
        pick.AffectCenter()
        pick.Create_Matrix()
        #
        for index, m in enumerate(pick.vehicule_matrix):
            #
            matrix = list(m.values())[0]
            vehicule = list(m.keys())[0]
            #
            # d=[list(x.values())[0]for x in list(m.values())[0]]
            #
            pop = pick.TLBO(m, pick.D, index)
            #
            # print('cluster nb : ',index,'',end_cluster - start_time)

        #
        pick.station()
        print(pick.pop_ameliori)
        pick.visualisation(pick.setupVisualisation())
        #
        return render_template('rslt.html',best_sol = pick.pop_ameliori)
    else:
        return render_template('index.html')
#
@pickup_blueprint.route('/add')
def addClient():
    #
    global pick
    #
    if pick is not None:
        #
        path = '../amiraTafsoutPickup/templates/cluster.html'
        if(os.path.exists(path)):
            #
            os.remove(path)
        #
        pick.dynamiClient()
        pick.pop_ameliori = []
        pick.vehicule_matrix = []
        # pick.Clustering = [x[2:]for x in pick.Clustering]
        # with
        # [print('clustering len',len(x)) for x in pick.Clustering]
        pick.Create_Matrix()
        for index, m in enumerate(pick.vehicule_matrix):
            #
            matrix = list(m.values())[0]
            vehicule = list(m.keys())[0]
            #
            # d=[list(x.values())[0]for x in list(m.values())[0]]
            #
            pick.TLBO(m, pick.D, index)
            #

        #
        pick.station()
        pick.visualisation(pick.setupVisualisation())
        # [print('pop len',len(x)) for x in pick.pop_ameliori]
        [print('Station', x[-1]) for x in pick.pop_ameliori]
        #
        return render_template('rsltPlus.html',best_sol = pick.pop_ameliori)
    #
    return render_template('index.html')
    #
@pickup_blueprint.route('/visual')
def show():
    #
    path = '../amiraTafsoutPickup/templates/cluster.html'
    while(True):
        #
        print(os.path.exists(path))
        if(os.path.exists(path)):
            return render_template('cluster.html')
        #
        time.sleep(1)
    #