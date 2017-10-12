import ui

def address_touch_up_inside(sender):
    view['name_label'].text = ("Anthony Freeman")
    view['city_label'].text = ("Ottawa")
    view['province_label'].text = ("Ontario")

view = ui.load_view()
view.present('sheet')
