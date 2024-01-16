##Choix du système
def syst1(*args,**kwargs):
    global choix_systeme
    choix_systeme = 'F'
    pyscript.write('choix_syst',choix_systeme) 
        
def syst2(*args,**kwargs):
    global choix_systeme
    choix_systeme = 'L'
    pyscript.write('choix_syst',choix_systeme)
    
def syst3(*args,**kwargs):
    global choix_systeme
    choix_systeme = 'P'
    pyscript.write('choix_syst',choix_systeme)
        
##Recherche 
        
        
##Afficher le tableau
        
import json
        
with open("class_categ.json") as json_file:
    data = json.load(json_file)

    
#Créer une liste vide servant de container    
data_lst = ['data1','data2','data3','data4','data5',
            
        'data6','data7','data8','data9','data10',
        'data11','data12','data13','data14','data15',
        'data16','data17','data18','data19','data20',
        'data21','data22','data23','data24','data25']
               
#Lien du mot saisie entre Python et html
saisie_rech = Element("saisie_rech")          
 
#Fonction qui va créer la liste data_lst en piochant dans le fichier data class_categ.json
def rech_btn(*args,**kwargs):
        
    #Efface la liste data_lst prédédente    
    for i in range(len(data_lst)):
        Element(data_lst[i]).clear()
        
    #Création de la liste avec les éléments recherchés 
    rech_lst = [elem for elem in data if choix_systeme in elem and saisie_rech.value.upper() in elem]    
        
    #Affichage de cette liste dans la fenêtre de Résultats
    #j: lignes
    #i: colonnes
    for j in range(len(rech_lst)):
        for i in range(5):
            Element(data_lst[i+5*j]).write(rech_lst[j][i])
     


def rech_btn_event(e):
    if e.key == "Enter":
        rech_btn()
   
saisie_rech.element.onkeypress = rech_btn_event

