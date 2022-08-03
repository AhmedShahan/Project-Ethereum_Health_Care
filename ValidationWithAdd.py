from msilib.schema import tables
from PySimpleGUI import *

def create(add_another_degree,headings):
    add_another_degree_Layout=[
        [Table(values=add_another_degree,headings=headings, max_col_width=35,
              auto_size_columns=True,
              display_row_numbers=True,
              justification="center",
              num_rows=10,
              key="table",
              row_height=35,
              tooltip="Adding Degree Table",
              background_color="#214162",
            #   visible_column_map="visible",
              enable_events=True,
              select_mode=TABLE_SELECT_MODE_BROWSE
              )]
    ]
    adding_degree=Window("Added Degree",add_another_degree_Layout,modal=True)
    while True:
        event,value=adding_degree.read()
        if event== "Exit" or event== WIN_CLOSED:
            break
    adding_degree.Close()
    
# def velidation(values):
#   NULLVALUE=[]
#   for i in values:
#     if i==None or i==0:
#       NULLVALUE.append(i)
#   print(NULLVALUE)