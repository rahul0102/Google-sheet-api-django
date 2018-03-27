import json
import pygsheets
from pygsheets import SpreadsheetNotFound
# class Sheet():
#     id = None
#     title = None
#     url = None
#     worksheets = []
#     index = 0
#
#     def get_all_worksheets(self):
#         return


# def get_counter(counter=0):
#     return counter+1
# counter = get_counter()
# print(counter)

# add_worksheet(title, rows=100, cols=26, src_tuple=None, src_worksheet=None, index=None):
    # """
    # Adds a new worksheet to a spreadsheet.
    #
    # title – A title of a new worksheet.
    # rows – Number of rows.
    # cols – Number of columns.
    # src_tuple – a tuple (spreadsheet id, worksheet id) specifying a worksheet to copy
    # src_worksheet – source worksheet object to copy values from
    # index – worksheet position
    # """
#     pass
def get_credential():
    client = pygsheets.authorize(service_file='client_secret.json')
    return client

def create_worksheet():
    pass

def get_worksheet(sheet, title = None,index = None,id = None):
    if title:
        return sheet.worksheet_by_title(title)
    if index:
        return sheet.worksheet(property = 'index', value = index)
    if id:
        return sheet.worksheet(property = 'id', value = id)

def get_available_worksheets():
    # client = get_credential()
    sheet = open_sheet(client, url = sheet_url)
    worksheet_list = sheet.worksheets()
    worksheet_choices = []
    for worksheet in worksheet_list:
        ch = (worksheet.title,  worksheet.title)
        worksheet_choices.append(ch)
    # print(worksheet_choices)
    # print(counter, "inside")
    return worksheet_choices

def get_data_after_row(row=1, worksheet_title = "School_Friends"):

    sheet = open_sheet(client, url = sheet_url)
    worksheet = sheet.worksheet_by_title(worksheet_title)
    col_length = worksheet.cols
    row_length = worksheet.rows
    row = row + 1 # because from next row
    # print(col_length, row_length, worksheet)
    list_of_data = worksheet.get_values((row,1), (row_length,col_length),
        include_empty=False) # (start, end)
    # print(list_of_data)
    return json.dumps(list_of_data)
def get_data_as_panda_frame(worksheet_title = "School_Friends"):
    sheet = open_sheet(client, url = sheet_url)
    worksheet = sheet.worksheet_by_title(worksheet_title)
    # get_as_df(has_header=True, index_colum=None, start=None, end=None, numerize=True, empty_value='')
    df = worksheet.get_as_df()
    print(df)
def open_sheet(client, title = None, key = None, url = None):
    if title:
        return client.open(title)
    if key:
        return client.open_by_key(key)
    if url:
        return client.open_by_url(url)
    raise SpreadsheetNotFound


def save_data_to_worksheet(row_data, worksheet_title = "Test1"):
    sheet = open_sheet(client, url = sheet_url)
    worksheet = sheet.worksheet_by_title(worksheet_title)
    # or
    # worksheet = sheet.worksheet('index', 0)
    # worksheet = sheet[0]

    # worksheet.cell('A1').set_text_format('bold', True).value = 'FirstName'
    # # worksheet.cell('B1').set_text_format('bold', True).value = 'LastName'

    list_of_values = worksheet.get_all_values()
    length = len(list_of_values)
    # check if sheet has no value and if so then set headers
    if length == 1:
        set_headers(worksheet)
    index = length + 1
    print("index", index)
    worksheet.update_row(index, row_data)

def set_headers(worksheet):

    # print("called")
    header_values = [['FirstName', 'LastName', 'DOB', 'Mobile No', 'Address', 'Occupation']]
    worksheet.update_cells(crange='A1:F1', values=header_values)
    # worksheet.update_cells(cell_list = header_values)
    # data_range = worksheet.get_named_ranges(headers.name)
    headers = worksheet.range('A1:F1', returnas='range')
    header_cell = pygsheets.Cell('A1')
    header_cell.set_text_format('bold', True)
    headers.apply_format(header_cell)

def create_sheet(client, title):
    return client.create(title)

def list_sheets(client):
    return client.list_ssheets()

sheet_url = "https://docs.google.com/spreadsheets/d/\
1pFdoDO1PPTLphVz_dBLY4lwR0RLL2wQOXjIZDIC4ZrY/edit?usp=sharing"
client = get_credential()
# print('Client: ', client.oauth.__dict__)
