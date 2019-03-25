import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


ratings =pd.read_csv('da.csv',index_col=0)
ratings["songID"]=ratings["songID"].astype(str)
ratings["rating"]=ratings["rating"].astype(float)



relation=pd.pivot_table(ratings,index='userID',columns='songID',values='rating')

def algoPearson(movie1,movie2):
    related_rating1=movie1-movie1.mean()
    related_rating2=movie2-movie2.mean()
    
    k=np.sum(related_rating1 * related_rating2) /np.sqrt(np.sum(related_rating1**2)* np.sum(related_rating2**2))
    if np.isnan(k):
        return 0
    else:
        return k
    
    

def reccomendation(movie_id,relation,k):
    review=[]
    for title_id in relation.columns:
        if title_id==movie_id:
            continue
        correlation =algoPearson(relation[title_id],relation[movie_id])
        if np.isnan(correlation):
             continue
        else:
             review.append((title_id,correlation))

    review.sort(key=lambda tup: tup[1], reverse=True)
    return review[:k]

ans=reccomendation('726',relation,k)
ans[:k]
