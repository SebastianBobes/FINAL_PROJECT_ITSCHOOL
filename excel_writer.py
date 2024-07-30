from openpyxl import Workbook

def create_excel(name: str, data: list, first_column_name: str, second_column_name: str):
    wb = Workbook()
    ws = wb.active
    ws['A1'] = first_column_name
    ws['B1'] = second_column_name
    for row in data:
        ws.append(row)

    wb.save(f'{name}.xlsx')
