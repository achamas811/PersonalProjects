import pandas as pd
import matplotlib.pyplot as plt

#Turn csv into a data frame
lwd = pd.read_csv("C:/Users/alexa/Downloads/livwell135.csv")

#Setting: The countries and the events that occurred during the time period of 2000-2015
print("The Setting \n")
print("The setting of the data takes place in Colombia and Peru between the years of 2000 and 2015.")
input("Press enter to continue...")
print("\nColombia\n")
print("In Colombia, there was a recession that occurred in the late 1990s into the early 2000s.")
input("Press enter to continue...\n")
print(f"In 1999, Colombia’s economy fell by 4% and in 2000, Colombia’s unemployment level reached 20.4%.")
input("Press enter to continue...")
print("\nPeru\n")
print("In the 2000s, Peru suffered from a major natural disaster and violence.")
input("Press enter to continue...\n")
print("In 2002, a car bomb exploded in Lima, Peru killing nine people, injuring thirty-two, and caused heavy damage to the surrounding buildings and cars in the process of the event.\n")
print("In 2007, a magnitude 8 earthquake occurred on the coast of south Peru that killed 519 people, injuring 1,300 people, and causing damage to tens of thousands of  homes, churches, schools, and hospitals. The infrastructure damage was worth up to $300 million.\n")

#Prints the information of the characters
print("The Characters\n")
print("The characters in the data are young women, school aged, and each of these women are from either Colombia or Peru.")
input("Press enter to continue...")

#Context 
print("\nThe Context\n")
print("In both regions, the women represented in the data have at least four members in their household and most likely have a lot of responsibilities to take care of younger siblings. However, there are some possibly different reasons for the data showing that as the number of members in a household increases, the female average year of schooling decreases.")
input("Press enter to continue...")
print("\nColombia\n")
print("In Colombia, there was an economic recession in the early 2000s that may have made some families unstable financially, causing some women to leave school and work to support their families.")
input("Press enter to continue...")
print("\nPeru\n")
print("In Peru, people are impacted by violent events and natural disasters that could have possibly killed their family members and destroyed their homes and schools, making them feel strong negative emotions.\n")

#List of all unique countries in the csv file
country_list = lwd["country_name"].unique()

#Filters the date included in the list by country name and year, saves results
colombia_conditional_list = (lwd["country_name"] == "Colombia") & (lwd["year"].between(2000,2015))
colombia_data = lwd.loc[colombia_conditional_list]

peru_conditional_list = (lwd["country_name"] == "Peru") & (lwd["year"].between(2000,2015))
peru_data = lwd.loc[peru_conditional_list]

#Creates the scatter plots 
plt.scatter(data=colombia_data, x="HD_women_size_mean", y="ED_educ_years_mean",color = "black")
plt.scatter(data=peru_data, x="HD_women_size_mean", y="ED_educ_years_mean",color = "red")

plt.legend(["Colombia", "Peru"])
plt.grid(True)

plt.title("Household Size Versus Female Average/Median Years Of Schooling")
plt.xlabel("Household Size (number of people)")
plt.xlim(4,7)
plt.ylabel("Female Average/Median Years Of Schooling (years)")
plt.ylim(6,10.5)

#Research Question
print("\nResearch Question\n")
print("Based on the data and the knowledge obtained about Peru and Colombia, my research question is:\nHow do geographical, social, and economical events impact a young woman’s ability to continue in school?")

#Display Graph
plt.show(block = True)



