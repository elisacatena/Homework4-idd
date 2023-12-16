import os
import xml.etree.ElementTree as ET
import json
from findElem import FindElement

myPath = "/Users/elisacatena/Desktop/Ingegneria dei dati/Homework/hw 4/file hw4/"
filesName = os.listdir(myPath)
print(len(filesName))
print("\n")
cont=0
for file in filesName:
    cont+=1
    if file != ".DS_Store":
        json_data = {}
        json_content = {}
        json_name = file.split('.')[0]
        outfile = open("/Users/elisacatena/Desktop/json file hw4/"+json_name+".json", "w")
        print(file)
        print("CONT:")
        print(cont)
        myClass = FindElement(file)
        #PMCID
        pmcid=myClass.getPmcid()
        if pmcid is not None:
            json_data['PMCID'] = pmcid.text
        else:
            json_data['PMCID'] = ''

        
        #title
        title_text = myClass.getTitle()
        json_content['TITLE'] = title_text
        

        #abstract
        abstract = myClass.getAbstract()
        if abstract is not None:
            json_content['ABSTRACT'] = abstract.text
        else:
            json_content['ABSTRACT'] = ''
            
        #keywords
        kwd_list = myClass.getKeywords()
        json_content['KEYWORDS'] = kwd_list

        #tables
        tables_list = []
        for table in myClass.getTables():
            json_table = {}
            #table ID
            tableID = myClass.getTableID(table)
            json_table['TABLE ID'] = tableID

            #body
            tableHead = myClass.getTableHead(tableID)
            tableBody = myClass.getTableBody(tableID)
            if tableHead is not None:
                json_table['BODY'] = ET.tostring(tableHead,encoding='unicode')
            else:
                json_table['BODY'] = ''
            if tableBody is not None:
                json_table['BODY'] = json_table.get('BODY')+ET.tostring(tableBody,encoding='unicode')
            else:
                json_table['BODY'] = json_table.get('BODY')

            #caption
            caption = myClass.getTableCaption(tableID)
            if caption is not None:
                json_table['CAPTION'] = caption.text
            else:
                json_table['CAPTION'] = ''
            
            #caption_citation
            json_table['CAPTION CITATIONS'] = []
            #foot
            feet_list = myClass.getTablesFoot(tableID)
            json_table['FOOTS'] = feet_list

            #paragraph text
            text = myClass.getParagraphText(tableID)
            paragraphs_list = []
            for p in text:
                #paragraph citations
                citations_list = myClass.getParagraphCitations(p)
                paragraphs_list.append({"text":ET.tostring(p,encoding='utf-8').decode('utf-8'),"citations":citations_list})
            json_table['PARAGRAPHS'] = paragraphs_list
                
            #cells
            json_table['CELLS']=[]

            tables_list.append(json_table)
        json_content['TABLES'] = tables_list

        #figure
        figures_list = []
        for fig in myClass.getFigures():
            json_figure = {}
            #fig ID
            figID = myClass.getFigureID(fig)
            json_figure['FIG_ID'] = figID
            #source
            #print(root.find(".//fig[@id='"+fig.attrib.get("id")+"']//graphic/*"))
            #print(root.find('.//graphic').attrib.get('xlink:href', None))
            source = None
            if source is not None:
                json_figure['SRC'] = 'da fare'
            else:
                json_figure['SRC'] = ''
            #caption
            figCaption = myClass.getFigureCaption(figID)
            if figCaption is not None:
                json_figure['CAPTION'] = ET.tostring(figCaption,encoding='unicode')
            else:
                json_figure['CAPTION'] = ''
            
            json_figure['PARAGRAPHS'] = []
            figures_list.append(json_figure)
        
        json_content['FIGURES'] = figures_list

        json_data['CONTENT'] = json_content
        print("\n")
        json.dump(json_data,outfile,indent=4)