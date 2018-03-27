import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import *
from System.Windows.Forms import *

class MyForm(Form):
    def __init__(self):
        #Form Label
        self.Text = "Calc Test"

        #Form Sizing and Position
        self.FormBorderStyle = FormBorderStyle.Fixed3D
        self.StartPosition = FormStartPosition.CenterScreen;
        screenSize = Screen.GetWorkingArea(self)
        self.Height = 400
        self.Width = 300
        formHeight = 400
        formWidth = 300
        
       
        # Main Label for output
        self.label = Label()
        self.label.Text = str(" 0 ")
        self.label.Location = Point(40, 30)
        self.label.Height = 30
        self.label.Width = 200
        self.label.BorderStyle = BorderStyle.Fixed3D
        self.label.TextAlign = ContentAlignment.MiddleRight
        self.Controls.Add(self.label)

        # Calculator buttons
        self.button1 = Button()
        self.button1.Text = ' 1 '
        self.button1.Location = Point(45, 70)
        self.button1.Height = 30
        self.button1.Width = 57
        #button click below is causing app to break
        #self.button1.Click = self.numUpdate
        self.Controls.Add(self.button1)

        self.button2 = Button()
        self.button2.Text = ' 2 '
        self.button2.Location = Point(112, 70)
        self.button2.Height = 30
        self.button2.Width = 57
        self.Controls.Add(self.button2)

        self.button3 = Button()
        self.button3.Text = ' 3 '
        self.button3.Location = Point(179, 70)
        self.button3.Height = 30
        self.button3.Width = 57
        self.Controls.Add(self.button3)

        self.equalsButton = Button()
        self.equalsButton.Text = ' = '
        self.equalsButton.Location = Point(45, 110)
        self.equalsButton.Height = 250
        self.equalsButton.Width = 191
        self.Controls.Add(self.equalsButton)
     
    pass

#need to work through this numUpdate definition
def numUpdate(self, sender):
    value = sender.Name
    self.label.Text = str(value)

Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MyForm()
Application.Run(form)



              