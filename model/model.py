from database.DAO import DAO
class Model:
    def __init__(self):
        pass

    def getAllAnni(self):
        return DAO.getAllAnni()

    def getAllBrand(self):
        return DAO.getAllBrand()


    def getAllRetailers(self):
        return DAO.getAllRetailers()

    def handleTop5Vendite(self,anno, brand, retailer):
        return DAO.handleTop5Vendite(anno, brand, retailer)

    def handleAnalizzaVenditore(self, anno, brand, retailer):
        return DAO.handleAnalizzaVenditore(anno, brand, retailer)

    def handleAllStatistiche(self):
        return DAO.handleAllStatistiche()