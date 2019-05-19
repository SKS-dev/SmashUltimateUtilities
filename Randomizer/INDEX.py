import tkinter as tk
import time
from tkinter import *
import random
global data1
import os 

data = """Attacks	Hitbox Active	FAF	Base Dmg.	Angle	BKB/FKB	KBG
Jab 1	8-9	30	4	361	40/40/38	20
Jab 2	4-5	34	5	75	60	100
Dash Attack	5-8	49	11/5	50	60	97
Dash Attack (Late)	9-23	-	5	70	60	97
Ftilt (All Angles)	12-15	40	13/11	361	20	102
Utilt	8-10	28	6	92/95	28	130
Utilt (Late)	11-19	-	5	90	20	120
Dtilt	5	18	4	46/69	20	50
Fsmash	18-19	66	20	361	20	93
Usmash	11-12	58	17	95	35	85
Usmash (Late)	13	-	13	95	35	85
Dsmash		62				
Grabs	Hitbox Active	FAF				
Standing Grab	8-10	36				
Dash Grab	11-13	44				
Pivot Grab	12-14	39				
Throws	Base Dmg.	Angle	BKB	KBG	Throw Release/FAF	Notes
Fthrow	4, 8	45	60	70	21, 55	
Bthrow	7	45	80	60	48, 70	
Uthrow	4, 4	89	60	105	26, 45	
Dthrow	4, 7	130	80	18	30, 55	
Miscellaneous	Intangibility	FAF	Notes			
Spotdodge						
Forward Roll						
Back Roll						
Airdodge						
Directional Airdodge (F/B)						
Directional Airdodge (U)						
Directional Airdodge (D)						
1.2 Aerial Moves

Attacks	Hitbox Active	FAF	Base Dmg.	Angle	BKB/FKB	KBG	Landing Lag	Autocancel
Nair (Hit 1)	4-17	46	6	40	30	100	7	1-3, 43>
Nair (Hit 2)	20-42	-	4	70	65	100	-	-
Fair	5-6	38	7	361	30	97	10	1-4, 27>
Fair (Late)	7-17	-	4.5	361	15	80	-	-
Bair	9-11	50	12	361	21	106	16	1-4, 34>
Uair	8-9	47	13	88	30	78	7	1-3, 37>
Dair (Hits 1-6)	9, 11, 13, 12, 17, 19	48	1.3	250/110/110	F: 60	100	18	1-2, 42>
Dair (Hit 7)	21	-					-	-
1.3 Special Moves

Attacks	Hitbox Active	FAF	Base Dmg.	Angle	BKB/FKB	KBG
Chomp (Shortest)	8-16	42	-	-	-	-
Chomp (Longest)	8-64	90	-	-	-	-
Chomp (Eating Explosive)	17	72	-	-	-	-
Chomp ("Food")	1.5x Recovery	51	-	-	-	-
Chomp (Large Objects)	-	56	-	-	-	-
Chomp (Throw)	-	-	5			
Wario Bike (Bike)	KB Based Armor: 20, HP: 18%	-	-	-	-	-
Wario Bike (zoom)	20-		7/5	361	60	70
Wario Bike (Turn)	-	-	7	45	60	120
Wario Bike (Turn, Late)	-	-	3	25	40	80
Wario Bike (Wheelie)	-	-	5	80	70	50
Wario Bike (Wheelie Slam)	-	-	13	70	70	105
Wah Twist (Hit 1)	6-7	-	5	127	F: 110/110/90/90	100/110/100/100
Wah Twist (Hits 2-5)	8-11, 12-15, 16-19, 20-23	-	1/1.2/1.3/1.4/1.5	80/105/115/105/105	F: 100/110/110/110/110	92/88/88/88/88
Wah Twist (Hit 6)	29-30	-				
Wario Waft (No Charge)	16-18	80	0	361	0	1
Wario Waft (15 Seconds)	10-11	65	12/10			
Wario Waft (55 Seconds)	5-8	50	20			
Wario Waft (110 Seconds)	9-10	60	27	35	50	75
Wario Waft (110 Seconds, Late)	11-26	-	20	80	0	100 """
print(data)