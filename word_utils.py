# -*- coding: utf-8 -*-
'''
Created on 2013-6-19

@author: huijieli
'''
#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import win32com.client
import os
class easyWord:
    def __init__(self,visible=False):
        self.wdApp = win32com.client.Dispatch('Word.Application')
        self.wdApp.Visible = visible
    def new(self,filename=None):
        if filename:
            return self.wdApp.Documents.Add(filename)
        else:
            return self.wdApp.Documents.Add()
    def open(self,filename):
        return self.wdApp.Documents.Open(filename)

    def visible(self,visible=True):
        self.wdApp.Visible = visible

 
if __name__ == "__main__":
    we=easyWord()
    filename="C:\Users\huijieli\Desktop\442342.doc"
    we.open(filename)