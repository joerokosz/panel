"""
Program: panelDemo.py
Chapter 8 (Page 274)
1/23/2024

**NOTE: the module breezypythonygui.py MUST be in the same directory as this file for the app to run correctly!

Example showing the use of panel graphic components to enhance application designs.
"""

from breezypythongui import EasyFrame
# Other imports go here

# Class header (class name will change project to project)
class PanelDemo(EasyFrame):

	# Definition of our classes constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Panel Demo", background = "yellow")

		# Create the nested frame for the top panel
		topPanel = self.addPanel(row = 0, column = 0, background = "gray")

		# Create and add widgets to the top panel
		topPanel.addLabel(text = "Label 1", row = 0, column = 0, background = "gray")
		topPanel.addTextField(text = "Text 1", row = 0, column = 1)
		topPanel.addLabel(text = "Label 2", row = 1, column = 0, background = "gray")
		topPanel.addTextField(text = "Text 2", row = 1, column = 1)

		# Create the nested frame for the bottom panel
		bottomPanel = self.addPanel(row = 1, column = 0, background = "black")

		# Create and add buttons to the BOTTOM PANEL
		bottomPanel.addButton(text = "B1", row = 0, column = 0)
		bottomPanel.addButton(text = "B2", row = 0, column = 1)
		bottomPanel.addButton(text = "B3", row = 0, column = 2)

# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	PanelDemo().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()