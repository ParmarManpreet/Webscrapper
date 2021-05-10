import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1ag4C3fVMZRnoBeE3maBOB1nygAbNWF3uQYyi5P43l5M')
worksheet = sh.sheet1

res = worksheet.get_all_values()
print(res)