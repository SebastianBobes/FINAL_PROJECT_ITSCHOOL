from openpyxl import Workbook

def create_excel(name: str, data: list, first_column_name: str, second_column_name: str):
    wb = Workbook()
    ws = wb.active
    ws['A1'] = first_column_name
    ws['B1'] = second_column_name
    for row in data:
        ws.append(row)

    wb.save(f'{name}.xlsx')

def create_complex_exccel(name: str, data: list, first_column_name: str= '', second_column_name: str = '', third_column_name: str =''):
    wb = Workbook()

    ws = wb.active

    ws['A1'] = first_column_name
    ws['B1'] = second_column_name
    ws['C1'] = third_column_name

    for row_idx, row_data in enumerate(data, start=2):  # Rows are 1-indexed in openpyxl
        for col_idx, cell_value in enumerate(row_data, start=1):  # Columns are 1-indexed in openpyxl
            ws.cell(row=row_idx, column=col_idx, value=cell_value)

    wb.save(f"{name}.xlsx")
