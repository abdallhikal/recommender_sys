from api_rec import db 
from api_rec.models import Data
from sklearn.neighbors import NearestNeighbors

for i in Data.query.all():
    data = i.data_mat
    model = NearestNeighbors().fit(data)
    i.model_mat = model
    db.session.commit()  
