# import gspread
# from google.oauth2.service_account import Credentials

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')

# data = sales.get_all_values()

data_dict = {
    'sales': {
        'cheese ham': [28, 26, 28, 25, 22, 27, 28],
        'tom moz': [31, 32, 28, 32, 28, 27, 26],
        'chicken salad': [21, 33, 30, 31, 30, 36, 32],
        'egg salad': [23, 25, 22, 24, 23, 26, 28],
        'hummus veg': [30, 28, 29, 19, 33, 32, 26],
        'ham egg': [30, 27, 26, 30, 28, 31, 31]
    },
    'surplus': {
        'cheese ham': [4, 4, -6, -2, -7, 3, 0],
        'tom moz': [-5, 0, 0, -4, 0, 5, -6],
        'chicken salad': [5, -2, -3, 0, 3, 5, 6],
        'egg salad': [-8, -4, 3, 0, -3, 4, -5],
        'hummus veg': [0, -2, 6, 0, 10, 2, 7],
        'ham egg': [4, -6, 8, 5, 0, 2, 5]
    },
    'stock': {
        'cheese ham': [24, 22, 34, 27, 29, 24, 28, 28],
        'tom moz': [36, 32, 28, 36, 28, 23, 32, 31],
        'chicken salad': [16, 35, 33, 31, 27, 31, 26, 33],
        'egg salad': [31, 29, 19, 24, 26, 22, 33, 29],
        'hummus veg': [30, 30, 23, 19, 23, 30, 19, 22],
        'ham egg': [26, 33, 18, 25, 28, 29, 26, 31]
    }
}


def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data

def validate_data(values):
    """
    to validate the data entered by the user
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    updated_data_dict = data_dict.copy()
    print("Updating sales worksheet...\n")
    for key in data_dict['sales']:
                updated_data_dict['sales'][key] = data_dict['sales'][key] + sales_data

    # sales_worksheet = SHEET.worksheet("sales")
    # sales_worksheet.append_row(data)
    # print("Sales worksheet updated successfully.\n")


data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)
print(data_dict['sales'])


