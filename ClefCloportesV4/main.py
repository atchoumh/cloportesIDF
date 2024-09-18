from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import csv

class AppLayout(BoxLayout):
    #Méthodes pour importer la clef__________________________________________________________
    #Importe la clef depuis le tableur csv. La transforme en une liste de dictionnaires (un dico par ligne du tableur, avec comme indices les noms des colonnes)     
    def importClef():
        with open("ClefTableurCsv.csv", 'r', encoding='UTF-8', newline='') as clef:
            clef_reader = csv.DictReader(clef)
            clef_list = []
            for line in clef_reader:
                clef_list.append(line)
            return clef_list
    
    #Importe la clef dans une variable de classe
    clef = importClef()
    #Initialisation de la clef à l'étape ""
    etape = ""
    
    #Création des premiers boutons
    def create_initial_buttons(self):
        self.clear_widgets() #Nettoie le layout
        for x in self.clef:
            if x["NumChoix"][:-1] == self.etape: #Parcours la clef, s'arrête sur les NumChoix qui comprennent notre étape +1 caractère (l'étape suivante donc)
                newButton = Button(text=x["Critere"])
                newButton.bind(on_release=self.create_new_buttons) #On crée un bouton auquel on bind la fonction pour créer les boutons suivants
                
                self.add_widget(newButton)
                
                if x["Image"]: #S'il y a une image associée au choix, l'affiche en dessous
                        self.add_widget(Image(source=x["Image"]))  
                
                
    def create_new_buttons(self, instance):
        texte = instance.text #Prend le texte du bouton qui vient d'être pressé

        #On retrouve le NumChoix qui est associé au bouton qui a été actionné
        for x in self.clef:
            if x["Critere"] == texte:
                self.etape = x["NumChoix"]
                
        #Nettoie le layout, puis crée les boutons suivants en utilisant le NumChoix qu'on vient de trouver
        self.clear_widgets()
        for x in self.clef:
            if x["NumChoix"][:-1] == self.etape: #Pareil que pour les premiers boutons, prend les NumChoix qui font un caractère de plus    
                
                #On regarde si ce choix est une solution, ou s'il y a des étapes suivantes
                if x["Espece"]: 
                    #Si c'est une solution, on crée un label à la place d'un bouton
                    newLabel = Label(text=x["Critere"]+ "\n\n" + x["Espece"] + "\n\n" + x["Notes"]) 
                    self.add_widget(newLabel)
                    
                    if x["Image"]: #S'il y a une image associée au choix, l'affiche en dessous
                        self.add_widget(Image(source=x["Image"]))                    
                    
                else: #Sinon crée un bouton comme pour les premiers
                    newButton = Button(text=x["Critere"])
                    newButton.bind(on_release=self.create_new_buttons)
                    self.add_widget(newButton)
                    
                    if x["Image"]: #S'il y a une image associée au choix, l'affiche en dessous
                        self.add_widget(Image(source=x["Image"]))     
                    
        

class CloportesApp(App):
    def build(self):
        return AppLayout()

if __name__=="__main__":
    CloportesApp().run()