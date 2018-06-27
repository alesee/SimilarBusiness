import pandas as pd
import dill as pickle
import gensim

model_path = 'models/' 
model_pickle_path = model_path+'pv_dbow_final.bz2' 
datapath = 'data/'
company_data_path = datapath+'comp-df.pk'
contact_data_path = datapath+'contact-df.pk'
person_data_path = datapath+'person-df.pk'

#load company information dataframe    
with open(company_data_path, 'rb') as f:
    compDF = pickle.load(f) 
    
#load contact information dataframe    
with open(contact_data_path, 'rb') as f:
    contactDF = pickle.load(f) 
    
#load personnel information dataframe    
with open(person_data_path, 'rb') as f:
    personDF = pickle.load(f) 

#load model    
model = gensim.models.doc2vec.Doc2Vec.load(model_pickle_path) 
    
    
def get_similar_Companies(companyID, topn):
    """
    A function to get the similar companies to selected company ID
    
    Inputs: 
        companyID(int) -- index of selected company
        topn (int) – number of similar companies to return
       
    Returns:
         similar_companies(dataframe) -- dataframe containg similar companies information
    """
    selected_id = compDF.loc[companyID].comp_ID
    similar_list = [compDF[compDF.comp_ID == i[0]].index[0] for i in model.docvecs.most_similar(positive=[selected_id], topn=topn)]
    similar_companies = compDF.iloc[similar_list]
    return similar_companies
