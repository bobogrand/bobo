 #-*- coding: utf-8 -*-
import win32com.client

excel = win32com.client.Dispatch("Excel.Application") #
excel.Visible = True # 화면보여주기
wb = excel.Workbooks.Open("C:\\Users\\ksj\\Desktop\\te.xlsx")
# 엑셀 파일 열기


#엑티브 시트 열기
ws = wb.ActiveSheet
target = wb.Worksheets("sheet1")
#원하는 시트 열기


print(ws.Cells(2,1).Value)

#각 시트에 데이터 집어넣기
ws.Cells(2,1).Value = "gfdsgf"
target.Cells(1,1).Value = "fuck!"


#저장후 끝내기
wb.SaveAs("C:\\Users\\ksj\\Desktop\\te.xlsx")
excel.Quit()
