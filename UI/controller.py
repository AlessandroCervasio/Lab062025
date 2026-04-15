import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    #def handle_hello(self, e):
     #   name = self._view.txt_name.value
      #  if name is None or name == "":
      #      self._view.create_alert("Inserire il nome")
       #     return
        #self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        #self._view.update_page()

    def fill_dd_anni(self):
        anni=self._model.getAllAnni()
        self._view.dd_anno.options.append(ft.dropdown.Option("Nessun filtro"))
        for i in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(key=str(i["year"]),data=int(i["year"]), text=str(i["year"])))
        self._view.update_page()

    def fill_dd_brand(self):
        brand = self._model.getAllBrand()
        self._view.dd_brand.options.append(ft.dropdown.Option("Nessun filtro"))
        for i in brand:
            self._view.dd_brand.options.append(
                ft.dropdown.Option(key=str(i["Product_brand"]), data=str(i["Product_brand"]), text=str(i["Product_brand"])))
        self._view.update_page()


    def fill_dd_retailer(self):
        retailers = self._model.getAllRetailers()
        self._view.dd_retailer.options.append(ft.dropdown.Option("Nessun filtro"))
        for i in retailers:
            self._view.dd_retailer.options.append(
                ft.dropdown.Option(key=i, data=retailers[i], text=str(retailers[i])))
        self._view.update_page()


    def handleTop5Vendite(self, e):
        self._view.lv_out.controls.clear()
        string = "Nessun filtro"
        anno=self._view.dd_anno.value
        brand=self._view.dd_brand.value
        retailer=self._view.dd_retailer.value

        if anno is None or brand is None or retailer is None:
            self._view.create_alert("Selezionare tutti i parametri per effettuare la ricerca!")
            return
        if anno ==string or brand == string or retailer ==string:
            self._view.create_alert("Parametri non validi per la ricerca.")
            return

        topVendite=self._model.handleTop5Vendite( anno, brand, retailer)
        if topVendite is None:
            self._view.lv_out.controls.append(ft.Text("Nessuna vendita per i parametri selezionati"))
            self._view.update_page()

        else:
            for i in topVendite:
                self._view.lv_out.controls.append(ft.Text(str(i)))
        self._view.update_page()

    def handleAnalizzaVenditore (self, e):
        self._view.lv_out.controls.clear()
        string = "Nessun filtro"

        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        retailer = self._view.dd_retailer.value


        if anno == string and brand == string and retailer == string:
            tupla_AllStatistiche=self._model.handleAllStatistiche()
            self._view.lv_out.controls.append(ft.Text("Statistiche globali delle vendite:"))
            self._view.lv_out.controls.append(ft.Text(f"Giro d'affari: {tupla_AllStatistiche[0]}"))
            self._view.lv_out.controls.append(ft.Text(f"Numero vendite: {tupla_AllStatistiche[1]}"))
            self._view.lv_out.controls.append(ft.Text(f"Numero retailers coinvolti: {tupla_AllStatistiche[2]}"))
            self._view.lv_out.controls.append(ft.Text(f"Numero prodotti coinvolti: {tupla_AllStatistiche[3]}"))
            self._view.update_page()
            return

        elif anno is None or brand is None or retailer is None:
            self._view.create_alert("Selezionare tutti i parametri per effettuare la ricerca!")
            return
        tupla_statistiche= self._model.handleAnalizzaVenditore(anno,brand,retailer)
        if tupla_statistiche is None:
            self._view.lv_out.controls.append(ft.Text("Nessuna statistica disponibile per i parametri selezionati."))
        else:
            self._view.lv_out.controls.append(ft.Text("Statistiche vendite:"))
            self._view.lv_out.controls.append(ft.Text(f"Giro d'affari: {tupla_statistiche[0]}"))
            self._view.lv_out.controls.append(ft.Text(f"Numero vendite: {tupla_statistiche[1]}"))
            self._view.lv_out.controls.append(ft.Text(f"Numero retailers coinvolti: {tupla_statistiche[2]}"))
            self._view.lv_out.controls.append(ft.Text(f"Numero prodotti coinvolti: {tupla_statistiche[3]}"))


        self._view.update_page()



