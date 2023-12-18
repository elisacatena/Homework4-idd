import random
import os
import json
from lxml import etree 
import elementpath

class FindElementTest:

    def setUp(self,file):
        self.myPath = "/Users/elisacatena/Desktop/Ingegneria dei dati/Homework/hw 4/file hw4/"
        data = open(self.myPath+file).read()
        root = etree.fromstring(data)
        for element in root:
            for comment in element.xpath('.//comment()'):
                comment.getparent().remove(comment)
        self.root=root


    def getValueTest(self, value, tagName):
        value_test = self.root.find(f'.//*[contains(., {value})]')
        if value_test is not None:
            return value_test.tag == tagName
        
    def getValueListTest(self, value_list, tagName):

        for value in value_list:
            value_test = self.root.find(f'.//*[contains(., {value})]')
            if value_test is not None:
                if value_test.tag != tagName:
                    return False
                
        return True
    
    def checkIfTagExists(self, value, tagName):
        value_test = self.root.findall(f'.//*[contains(., {value})]')
        for val in value_test:
            if val.tag == tagName:
                return True
            
        return False

        
    def runTest(self):

        filesName = os.listdir(self.myPath)
        visited_files = []
        cont_pmcid, cont_abstract, cont_kwd, cont_tableId, cont_caption, cont_figId, cont_captionFig, cont_src = 0, 0, 0, 0, 0, 0, 0, 0

        for i in range(0, 300):

            file_number = random.randint(0, len(filesName)-1)
            while file_number in visited_files :
                file_number = random.randint(0, len(filesName)-1)
            
            visited_files.append(file_number)
            self.setUp(filesName[file_number])

            json_file = open(self.myPath+filesName[file_number]).read()

            json_data = json.load(json_file)

            pmcid_json = json_data.get('PMCID')
            if self.getValueTest(pmcid_json, 'article-id'):
                cont_pmcid += 1

            content_json = json_data.get('CONTENT')
            abstract_json = content_json.get('ABSTRACT')
            if self.getValueTest(abstract_json, 'abstract'):
                cont_abstract += 1

            kwd_json = content_json.get('KEYWORDS')
            if self.getValueListTest(kwd_json, 'kwd'):
                cont_kwd += 1

            tableId_json = content_json.get('TABLES').get('TABLE ID')
            if self.checkIfTagExists(tableId_json, 'table-wrap'):
                cont_tableId += 1

            caption_json = content_json.get('TABLES').get('CAPTION')
            if self.getValueTest(caption_json, 'caption'):
                cont_caption += 1

            figId_json = content_json.get('FIGURES').get('FIG_ID')
            if self.checkIfTagExists(figId_json, 'fig'):
                cont_figId += 1
            
            captionFig_json = content_json.get('FIGURES').get('CAPTION')
            if self.getValueTest(captionFig_json, 'caption'):
                cont_captionFig += 1

            src_json = content_json.get('FIGURES').get('SRC')
            if self.getValueTest(src_json, 'graphic'):
                cont_src += 1

        with open(self.myPath+'stats.json', "w") as outfile:
            outfile.write('File testati: ' + len(visited_files))
            outfile.write('PMCID: ' + cont_pmcid)
            outfile.write('ABSTRACT: ' + cont_abstract)
            outfile.write('KWD: ' + cont_kwd)
            outfile.write('TABLE ID: ' + cont_tableId)
            outfile.write('CAPTION: ' + cont_caption)
            outfile.write('FIG ID: ' + cont_figId)
            outfile.write('CAPTION FIG: ' + cont_captionFig)
            outfile.write('SRC: ' + cont_src)
