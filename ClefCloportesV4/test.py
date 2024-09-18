from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.counter = 1  # Compteur pour générer des textes uniques
        self.create_initial_buttons()
        return self.layout

    def create_initial_buttons(self):
        # Créer deux boutons initiaux avec des textes uniques
        button1 = Button(text=f'Bouton {self.counter}')
        self.counter += 1
        button2 = Button(text=f'Bouton {self.counter}')
        self.counter += 1
        
        # Lier les boutons à la méthode qui crée des boutons supplémentaires
        button1.bind(on_press=self.create_new_buttons)
        button2.bind(on_press=self.create_new_buttons)
        
        # Ajouter les boutons au layout
        self.layout.add_widget(button1)
        self.layout.add_widget(button2)

    def create_new_buttons(self, instance):
        # Effacer le layout
        self.layout.clear_widgets()
        
        # Créer deux nouveaux boutons avec des textes uniques
        new_button1 = Button(text=f'Nouveau Bouton {self.counter}')
        self.counter += 1
        new_button2 = Button(text=f'Nouveau Bouton {self.counter}')
        self.counter += 1
        
        # Lier les nouveaux boutons à la méthode pour créer encore plus de boutons
        new_button1.bind(on_press=self.create_new_buttons)
        new_button2.bind(on_press=self.create_new_buttons)
        
        # Ajouter les nouveaux boutons au layout
        self.layout.add_widget(new_button1)
        self.layout.add_widget(new_button2)

if __name__ == '__main__':
    MyApp().run()