import os
import pandas as pd
import getSimilar
from getSimilar import get_similar_Companies

compDF = getSimilar.compDF #
contactDF = getSimilar.contactDF
personDF = getSimilar.personDF

#list of all companies in database along with their indexes
allCompanies = compDF[['comp_op_name']].reset_index()
allCompanies.columns = ['data', 'value']
allCompanies = allCompanies.to_json(orient='records')


from flask import Flask, request, render_template

app = Flask(__name__)



@app.route("/", methods=['GET','POST']) 
def displayCompany():
    """
    Display homepage 
    
    """
    return render_template('index.html', allCompanies = allCompanies)


@app.route("/findsimilar/<int:companyID>", methods=['GET'])
def findsimilar(companyID):
    """
    Display result of get_similar_Companies function 
    
    """
    similarDF = get_similar_Companies(companyID, 10)
    return render_template('similar.html',
                           similarDF=similarDF,
                           selectcompanyDF=compDF.iloc[companyID],
                           selectID=companyID)

@app.route("/profile/<int:companyID>", methods=['GET'])
def displayProfile(companyID):
    """
    Display selected company information 
    
    """
    a = compDF.iloc[companyID].comp_ID
    selectPersonDF = personDF[personDF.comp_ID == a]
    return render_template('profile.html',
                           selectcompanyDF=compDF.iloc[companyID],
                           selectContactDF=contactDF.iloc[companyID],
                           selectPersonDF=selectPersonDF,
                           selectID=companyID)



if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

