from shiny import render, ui
from shiny.express import input

ui.panel_title("Environmental Data Science Methods Energy Analysis Calcultor")



ui.input_numeric("datasize_numeric", "Select your data size", 100) 

ui.input_selectize("datasize_unit", "and which unit", 
                   ["MB", "GB", "TB"])



ui.input_selectize(  
    "method_selectize",  
    "Select your method:",  
    {"LR": "Linear Regression", "RF": "Random Forest", "1B": "Choice 1B", "1C": "Choice 1C"},  
)  

# comparing approaches

@render.text
def txt():
    return f"n*2 is {input.n() * 2}"
