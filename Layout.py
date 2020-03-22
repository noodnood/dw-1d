# import kivy module   
import kivy
      
# base Class of your App inherits from the App class.     
# app:always refers to the instance of your application     
from kivy.app import App  
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.widget import Widget 
from kivy.lang import Builder

Builder.load_file('LockerSelect.kv')

class myApp(App): 
    def build(self): 
        return LockerSelect() 

# Create the App class 
class LockerSelect(GridLayout):     
    pass 


# Run the App class 
if __name__ == '__main__': 
    myApp().run()