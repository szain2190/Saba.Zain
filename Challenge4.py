

def calcPopulationUK(years): 
# function to calculate the population in the UK in a certain number of years
 Today_Population = 66650000 
 # stores the total population of the UK in a variable
 Births_per_day = 8.51 
 # stores the births per day in the variable
 Deaths_per_day = 6.48 
 # stores the deaths per day in a variable
 Emigration_per_year = 403000 
 # stores the emigration per year in a variable
 Migration_per_year = 715000 
 # stores the migration per year in the variable
 bdChange_per_day = Births_per_day - Deaths_per_day
 # calculates the change per day in birth and death rates by subtracting them 
 bdChange_per_year = bdChange_per_day * 365 
 # calculates the change per year in birth and death rates by multiplying the change per day by how many days there are in a year
 bdOverall_change = bdChange_per_year * years 
 # calculates the overall change by multiplying it by the number of years to figure out the population that many years into the future
 emChange_per_year = Migration_per_year - Emigration_per_year 
 # change per year by subtracting the migration and emigration
 emOverall_change = emChange_per_year * years 
 # calculates overall change by multiplying by years 
 Future_population = Today_Population + bdOverall_change + emOverall_change 
 # calculates future population of the UK by adding both the overall changes to todays population
 print(f"\nIn the UK in {years:,} years there will be {int(Future_population):,} people.") 
 # outputs the number of people that many years into the future


def calcPopulationWorld(years): # function for calculating population of the world in a certain number of years
    population = 79000000000 # stores the population of the world in the variable
    births_per_second = 4.17 # stores births per second in the variable
    deaths_per_second = 1.8 # stores deaths per second in the variable 
    change_per_second = births_per_second - deaths_per_second # change per second per subtracting the births and deaths per second
    change_per_year = change_per_second * 60 * 60 * 24 * 365 # calculates change per year to have the number in years instead of seconds
    WFuture_population = change_per_year * years + population 
    # calculates the future population by multiplying the number of years and adding it to the population
    print(f"\nIn {years:,} years the world population will be {int(WFuture_population):,}.\n") # outputs the future population in that number of years


years = int(input("\nEnter a number of years to get an estimate for the population: \n")) # allows the user to enter the number of years
calcPopulationUK(years) # calls the function
calcPopulationWorld(years) # calls the function

