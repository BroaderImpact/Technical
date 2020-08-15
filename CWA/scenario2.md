## C:\Users\Christine\Documents\GitHub\Technical\CWA\scenario2.md

### STEP 1: Generating values for a set of 100 CWA members in Excel

#### LANID
=RANDARRAY(100,1,100000,999999,TRUE)
#### Race
=CHOOSE(RANDBETWEEN(1,6),Strings!$B$2,Strings!$B$3,Strings!$B$4,Strings!$B$5,Strings!$B$6,Strings!$B$7)
#### Age
=RANDARRAY(100,1,18,99,TRUE)
#### Gender
=CHOOSE(RANDBETWEEN(1,3),Strings!$C$2,Strings!$C$3,Strings!$C$4)
#### District
=CHOOSE(RANDBETWEEN(1,7),Strings!$D$2,Strings!$D$3,Strings!$D$4,Strings!$D$5,Strings!$D$6,Strings!$D$7,Strings!$D$8)
#### Event Attendance and Event Type columns constructed together
=CHOOSE(RANDBETWEEN(1,7),Strings!$E$2:$F$2,Strings!$E$3:$F$3,Strings!$E$4:$F$4,Strings!$E$5:$F$5,Strings!$E$6:$F$6,Strings!$E$7:$F$7,Strings!$E$8:$F$8)
#### Groups of Skills and Skills columns constructed together
=CHOOSE(RANDBETWEEN(1,10),Strings!$G$2:$H$2,Strings!$G$3:$H$3,Strings!$G$4:$H$4,Strings!$G$5:$H$5,Strings!$G$6:$H$6,Strings!$G$7:$H$7,Strings!$G$8:$H$8,Strings!$G$9:$H$9,Strings!$G$10:$H$10,Strings!$G$11:$H$11)

### STEP 2: Data munging and cleaning

### STEP 3: Reviewing and visualizing data in Tableau

### STEP 4: Modeling

### STEP 5: Scaling

### STEP 6: Reporting