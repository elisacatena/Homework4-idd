import random
import os
import json
from lxml import etree
from findElem import FindElement
import unittest

class FindElementTest:
    
    def __init__(self):
        self.xmlPath = "./testXML/"
        self.jsonPath = "./testJSON/"
        self.root = None

    def checkEquals(self, extracted_value, expected_value):
        if extracted_value == expected_value:
            print(f"Il valore estratto ({extracted_value}) corrisponde al valore atteso ({expected_value})")
        else: 
            print(f"Il valore estratto ({extracted_value}) NON corrisponde al valore atteso ({expected_value})")
    
    def checkEqualsList(self, extracted_list, expected_list):
        if(len(extracted_list) != len(expected_list)):
            print(f"Il valore estratto ({extracted_list}) NON corrisponde al valore atteso ({expected_list})")
        else:
            for elem in extracted_list:
                if elem not in expected_list:
                    print(f"Il valore estratto ({extracted_list}) NON corrisponde al valore atteso ({expected_list})")
            print(f"Il valore estratto ({extracted_list}) corrisponde al valore atteso ({expected_list})")
        
    def runTest(self):

        xmlFiles = os.listdir(self.xmlPath)
        cont = 0

        for file in xmlFiles:
            cont += 1
            print("File: " + file)
            data = open(self.xmlPath + file).read()
            root = etree.fromstring(data)
            self.root=root

            myClass = FindElement(file, self.xmlPath)            

            #PMCID
            extracted_pmcid = myClass.getPmcid().text
            expected_pmcid = "PMC" + str(cont)
            self.checkEquals(extracted_pmcid, expected_pmcid)
            
            #title
            extracted_title = myClass.getTitle()
            expected_title = "title" + str(cont)
            self.checkEquals(extracted_title, expected_title)

            #abstract
            extracted_abstract = myClass.getAbstract().text
            expected_abstract = "abstract" + str(cont)
            self.checkEquals(extracted_abstract, expected_abstract)
                
            #keywords
            extracted_kwd_list = myClass.getKeywords()
            expected_kwd_list = []
            for i in range (0,cont-1):
                expected_kwd_list.append("kwd" + i)
            self.checkEqualsList(extracted_kwd_list, expected_kwd_list)

            #tables
            contTab = 0
            for table in myClass.getTables():
                contTab += 1
                #table ID
                extracted_tableID = myClass.getTableID(table)
                expected_tableID = "tab" + str(contTab)
                self.checkEquals(extracted_tableID, expected_tableID)

                #body
                extracted_tableHead = myClass.getTableHead(extracted_tableID)
                extracted_tableBody = myClass.getTableBody(extracted_tableID)
                expected_tableHead = "<thead><tr><th>" + str(cont) + "</th><th>" + str(contTab) + "</th>"
                expected_tableBody = "<tbody><tr><td><bold>" + str(cont) + "</bold></td><td>" + str(cont+1) + "</td><tr><td><bold>" + str(cont+2) + "</bold></td><td>" + str(cont+3) + "</td></tbody>"
                self.checkEquals(extracted_tableHead, expected_tableHead)
                self.checkEquals(extracted_tableBody, expected_tableBody)

                #caption
                extracted_caption = myClass.getTableCaption(extracted_tableID).text
                expected_caption = "caption" + str(contTab)
                self.checkEquals(extracted_caption, expected_caption)
                    
                #cells
                extracted_content_cells = myClass.getCells(extracted_tableID)
                expected_content_cells = [cont,(cont+1),(cont+2),(cont+3)]
                print(extracted_content_cells)
                print(expected_content_cells)
                self.checkEqualsList(extracted_content_cells, expected_content_cells)
                    
            #figure
            contFig = 0
            for fig in myClass.getFigures():
                contFig += 1
                #fig ID
                extracted_figID = myClass.getFigureID(fig)
                expected_figID = "fig" + str(contFig)
                self.checkEquals(extracted_figID, expected_figID)
                #source
                extracted_url = myClass.getSource(extracted_figID, extracted_pmcid)
                expected_url = "https://www.ncbi.nlm.nih.gov/pmc/articles/" + expected_pmcid + "/bin/"+ str(contFig) +".jpg"
                self.checkEquals(extracted_url, expected_url)


if __name__ == "__main__":
    testClass = FindElementTest()
    testClass.runTest()