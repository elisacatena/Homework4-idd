import os
import xml.etree.ElementTree as ET
import json
from findElem import FindElement

myPath = "C:/Users/MariaDeDomenico/OneDrive - Lobra S.r.l/Desktop/file hw4/docs/"
filesName = os.listdir(myPath)
print(len(filesName))
print("\n")
cont=0
black_list=["PMC4791908.xml","PMC5993998.xml","PMC3079697.xml","PMC4940961.xml","PMC2519083.xml","PMC2649030.xml", "PMC3605808.xml"]
#try:
for file in filesName: 
    cont+=1
    if file != ".DS_Store" and file not in black_list and cont > 163:
    #if file == "PMC4791908.xml":
        json_data = {}
        json_content = {}
        json_name = file.split('.')[0]
        outfile = open("C:/Users/MariaDeDomenico/OneDrive - Lobra S.r.l/Desktop/file hw4/jsons/"+json_name+".json", "w")
        print(file)
        print("CONT:"+str(cont))
        myClass = FindElement(file)
        #PMCID
        pmcid = myClass.getPmcid()
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
            if tableID is not None:
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
                    json_table['CAPTION'] = ET.tostring(caption,encoding='unicode',method='text')
                else:
                    json_table['CAPTION'] = ''
                
                #caption_citation
                caption_citations = myClass.getCaptionCitations(caption)
                json_table['CAPTION CITATIONS'] = caption_citations
    

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
                content_cells = myClass.getCells(tableID)
                cells_list = []
                visited_cells = []
                for cell in content_cells:
                    if cell not in visited_cells:
                        visited_cells.append(cell)
                        #cited_in 
                        cited_in_list = myClass.getCitedIn(cell)
                    else:
                        cited_in_list = myClass.get_second_element_by_content(cell, cells_list)
                    cells_list.append({"content":cell,"cited_in":cited_in_list})
                json_table['CELLS'] = cells_list
                tables_list.append(json_table)
            else:
                json_table['TABLE ID'] = ''
                #raise Exception
            json_content['TABLES'] = tables_list

        #figure
        figures_list = []
        for fig in myClass.getFigures():
            json_figure = {}
            #fig ID
            figID = myClass.getFigureID(fig)
            if figID is not None:
                json_figure['FIG_ID'] = figID
                #source
                url = myClass.getSource(figID, json_name)
                json_figure['SRC'] = url
                #caption
                figCaption = myClass.getFigureCaption(figID)
                if figCaption is not None:
                    json_figure['CAPTION'] = ET.tostring(figCaption,encoding='unicode')
                else:
                    json_figure['CAPTION'] = ''
                #caption_citation
                caption_citations = myClass.getCaptionCitations(figCaption)
                json_figure['CAPTION CITATIONS'] = caption_citations
                
                json_figure['PARAGRAPHS'] = []
                figures_list.append(json_figure)

                #paragraph cited_in
                cited_in_list = myClass.getParagraphCitedIn(figID)
                paragraphs_fig_list = []
                for c in cited_in_list:
                    #paragraph citations
                    citations_list = myClass.getParagraphCitations(c)
                    paragraphs_fig_list.append({"cited_in":ET.tostring(c,encoding='utf-8').decode('utf-8'),"citations":citations_list})
                json_table['PARAGRAPHS'] = paragraphs_fig_list
            else:
                json_figure['FIG_ID'] = ''
                #raise Exception

        json_content['FIGURES'] = figures_list

        json_data['CONTENT'] = json_content
        json.dump(json_data,outfile,indent=4)
# except Exception as e:
#     print(f"Errore: {e}")