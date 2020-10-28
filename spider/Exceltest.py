import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("sheet1",cell_overwrite_ok=False)#允许覆盖
worksheet.write(0,0,'helle')
workbook.save('student.xls')