# LineweaverBurkKinematics
Calculate Vmax and Km from substrate conc. and velocity
________
This repository has two Python 3 scripts.

numpy, scipy, and matplotlib are required.

to obtain these, the terminal commands are:

  pip install numpy
  pip install scipy
  pip install matplotlib

There are plenty of guides on how to install Python 3 and the required libraries, search engines are your friend.
________

"SingleEnzyme.py" will plot a Lineweaver-Burk diagram and give the user the associated Vmax (maximum velocity) and Km (Michaelis constant).
________
"CompareTwoEnzymes.py" will plot a Lineweaver-Burk diagram and give the user the associated Vmax (maximum velocity) and Km (Michaelis constant) for two different enzymes or a single enzyme before and after inhibition.

This is used to determine what kind of inhibition is acting on an enzyme.

I haven't put the functionality in to actually tell you what kind of competition it is.
You can easily figure it out by referencing a diagram like such:
https://commons.wikimedia.org/wiki/File:Inhibition_diagrams.png

________
The two scripts already have sample data that will serve as an example.
Modify the lists "s" and "v" (or vA & vB for CompareTwoEnzymes.py) in the first few lines of the program and input your own substrate concentration (μM) and velocity (μM/s) values, respectively.

The values that are already in place come from the two png images.
________

email me at griffincalme@wayne.edu for questions or help
