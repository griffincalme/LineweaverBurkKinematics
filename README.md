# LineweaverBurkKinematics
Calculate Vmax and Km from substrate conc. and velocity

This repository has two similar Python 3 scripts

"SingleEnzyme.py" will plot a Lineweaver-Burk diagram and give the user the 
associated Vmax (maximum velocity) and Km (Michaelis constant).

"CompareTwoEnzymes.py" will plot a Lineweaver-Burk diagram and give the user the 
associated Vmax (maximum velocity) and Km (Michaelis constant) for two different enzymes 
or a single enzyme before and after inhibition.
This is used to determine what kind of inhibition is acting on an enzyme.

I haven't put the functionality in to actually tell you what kind of competition it is.
You can easily figure it out by referencing a diagram like such:
https://commons.wikimedia.org/wiki/File:Inhibition_diagrams.png

The two scripts already have sample data that will serve as an example.
modify the lists "s" and "v" and input your own substrate concentration (μM) and velocity (μM/s) values, respectively.
