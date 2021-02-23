'''
THIS CODE IS UNDER DEVELOPMENT.
'''

#import os
import pikepdf

#file_list = os.listdir(os.getcwd())
#print(file_list)

filename = input('파일 이름: ')
pdf = pikepdf.open(filename + '.pdf')
pdf.save('[UNLOCKED] ' + filename + '.pdf')
