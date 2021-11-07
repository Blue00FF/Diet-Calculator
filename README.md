# Diet-Calculator
This is a program that I wrote to help my mother to calculate the portions of her keto diet, as specified by a professional nutritionist.

The way this diet works is that you're allocated a certain number of blocks each meal, divided between fat blocks, protein blocks and carbs blocks according to the
fat to protein to carbs ratio that the nutritionist has calculated and the number of calories each day a person of her age, weight and height requires. Each meal of 
the day has its own number of blocks and sources to take them from (for example, dinner requires that the carbs be all vegetables while a snack only wants fruit). 
Each kind of meat/fruit/vegetable/etc. has a certain value in grams corresponding to 1 block. The user then has to tell the script which meal they want to calculate 
the portions of, if they want to mix and match different kinds of carbs, fats or proteins and (if there is a choice) choose which family their protein/carb/fat has 
to come from (proteins for example can be either meat or fish). Once the user has chosen the families, a list of all the meals in the family is displayed and the 
actual meal is chosen for each of the three classes and for each of the mix and match choices. Once each meal is chosen, the program prints to console how much of 
that meal the user is assigned to eat.

On the technical side, I have used some functions for the pyinputplus module to restrict the kinds of input that are accepted from the user in order to ensure that 
the program runs as expected. I have also made use of the match/case structure introduced in python 3.10 and thus a version of python >= 3.10 will be required for 
the script to run.
