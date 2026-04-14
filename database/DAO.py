from database.DB_connect import DBConnect
from model.go_daily_sales import DailySales
from model.go_retailers import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAnni():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""select YEAR(gds.Date) AS year
                    from go_daily_sales gds"""
        cursor.execute(query)
        res=[]
        for row in cursor:
            if row in res:
                continue
            else:res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select gp.Product_brand 
                    from go_products gp """
        cursor.execute(query)
        res = []
        for row in cursor:
            if row in res:
                continue
            else:
                res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllRetailers():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select gr.*
                    from go_retailers gr  """
        cursor.execute(query)
        res = {}
        for row in cursor:
            code=row["Retailer_code"]
            if code in res:
                continue
            else:
                res[code]=Retailer(row["Retailer_code"],
                                    row["Retailer_name"],
                                    row["Type"],
                                    row["Country"])


        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def handleTop5Vendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = f"""select gds.*
                    from go_daily_sales gds, go_products gp 
                    where YEAR(gds.`Date` )=%s
                    and gds.Product_number =gp.Product_number 
                    and gp.Product_brand =%s
                    and gds.Retailer_code =%s
                    order by (gds.Unit_sale_price * gds.Quantity  ) DESC
                    limit 5"""
        cursor.execute(query, (anno,brand,retailer))
        lista=[]
        for row in cursor:
                lista.append(DailySales(row["Retailer_code"],row["Product_number"], row["Order_method_code"], row["Date"],row["Quantity"],
                                        row["Unit_sale_price"]))
        if len(lista)==0:
            return None


        cursor.close()
        cnx.close()
        return lista

    @staticmethod
    def handleAnalizzaVenditore(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = f"""select SUM(gds.Unit_sale_price *gds.Quantity )as giro, COUNT(*) as vendite, 
                    COUNT(DISTINCT gds.Retailer_code) as retailers,
                    COUNT(DISTINCT gds.Product_number) as nprodotti
                    from go_daily_sales gds, go_products gp 
                    where YEAR(gds.`Date` )=%s
                    and gds.Product_number = gp.Product_number 
                    and gp.Product_brand =%s 
                    and gds.Retailer_code =%s"""
        cursor.execute(query, (anno, brand, retailer ))
        ris=tuple()

        for row in cursor:
            if row["giro"] is None:
                return None
            else:
                ris=(row["giro"], row["vendite"], row["retailers"], row["nprodotti"] )


        cursor.close()
        cnx.close()
        return ris

    @staticmethod
    def handleAllStatistiche():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = f"""select SUM(gds.Unit_sale_price *gds.Quantity )as giro, COUNT(*) as vendite, 
                    COUNT(DISTINCT gds.Retailer_code) as retailers,
                    COUNT(DISTINCT gds.Product_number) as nprodotti
                    from go_daily_sales gds, go_products gp 
                    where gds.Product_number = gp.Product_number """
        cursor.execute(query)
        ris = tuple()

        for row in cursor:
            if row["giro"] is None:
                return None
            else:
                ris = (row["giro"], row["vendite"], row["retailers"], row["nprodotti"])

        cursor.close()
        cnx.close()
        return ris
