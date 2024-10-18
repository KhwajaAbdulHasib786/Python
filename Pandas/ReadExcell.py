# import  pandas as pd
# dt=pd.read_excel('Input.xlsx',sheet_name='Input')
# columnvalues=dt['Patient Name']
# for i in columnvalues:
#  print(i)


# read by python
# from openpyxl import workbook,load_workbook
#
# wb=load_workbook(filename='Input.xlsx')
# sh=wb['Input']
# print(sh['A3'].value)

# How to get cell values.
# from openpyxl import workbook,load_workbook
#
# wb=load_workbook(filename='Input.xlsx')
# sh=wb['Input']
# print(sh.cell(2,3).value)


# HOw to find max row
# from openpyxl import workbook,load_workbook
#
# wb=load_workbook(filename='Input.xlsx')
# sh=wb['Input']
# max_row=sh.max_row
# max_Columns=sh.max_column
# print(max_row)
# print(max_Columns)


# How to print column values and row value.
#
# from openpyxl import workbook,load_workbook
#
# wb=load_workbook(filename='Input.xlsx')
# sh=wb['Input']
# max_row=sh.max_row
# max_Columns=sh.max_column
#
# for i in range(1,max_row+1):
#     for j in range(1,max_Columns+1):
#         print(sh.cell(row=i,column=j).value,end=" ")
#         print("\n")