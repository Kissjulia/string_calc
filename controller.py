import model_string as model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    value_c = view.input_str()
    model.init(value_c)
    result = model.do_it()
    view.view_data(result, 'result')
