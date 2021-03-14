
import random as rd
import matplotlib.pyplot as plt
import numpy as np

size_siml = 1000000
initial_ages = [14, 17, 15, 14, 21, 17, 19, 20, 16, 18, 20, 17, 16, 19, 20]
# Assigning values 0, 1, 2, 3, 4, 5, 6, 7 for the case of selecting a 14, 15, 16, 17, 18, 19, 20, 21 year old respectively.
ages_data = [0, 0, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 7]
unique_ages = [14, 15, 16, 17, 18, 19, 20, 21]
numb_14 = numb_15 = numb_16 = numb_17 = numb_18 = numb_19 = numb_20 = numb_21 = 0

for i in range(size_siml):
  sim_itr = rd.randint(0, 14)
  if(ages_data[sim_itr] == 0):
    numb_14 += 1
  elif(ages_data[sim_itr] == 1):
    numb_15 += 1
  elif(ages_data[sim_itr] == 2):
    numb_16 += 1
  elif(ages_data[sim_itr] == 3):
    numb_17 += 1
  elif(ages_data[sim_itr] == 4):
    numb_18 += 1
  elif(ages_data[sim_itr] == 5):
    numb_19 += 1
  elif(ages_data[sim_itr] == 6):
    numb_20 += 1
  else:
    numb_21 += 1
  
    
prob_14 = numb_14 / size_siml
prob_15 = numb_15 / size_siml
prob_16 = numb_16 / size_siml
prob_17 = numb_17 / size_siml
prob_18 = numb_18 / size_siml
prob_19 = numb_19 / size_siml
prob_20 = numb_20 / size_siml
prob_21 = numb_21 / size_siml
probabilities_simu = [prob_14, prob_15, prob_16, prob_17, prob_18, prob_19, prob_20, prob_21]

print(" The following results are obtained from simulations")
print(f"(a) Choosing a person of age 14 has a probability of : {probabilities_simu[0]}")
print(f"(b) Choosing a person of age 15 has a probability of : {probabilities_simu[1]}")
print(f"(c) Choosing a person of age 16 has a probability of : {probabilities_simu[2]}")
print(f"(d) Choosing a person of age 17 has a probability of : {probabilities_simu[3]}")
print(f"(e) Choosing a person of age 18 has a probability of : {probabilities_simu[4]}")
print(f"(f) Choosing a person of age 19 has a probability of : {probabilities_simu[5]}")
print(f"(g) Choosing a person of age 20 has a probability of : {probabilities_simu[6]}")
print(f"(h) Choosing a person of age 21 has a probability of : {probabilities_simu[7]}")

print()
print("The following results are obtained theoretically")
print("(a) Choosing a person of age 14 has a probability of : 0.1333334")
print("(b) Choosing a person of age 15 has a probability of : 0.0666667")
print("(c) Choosing a person of age 16 has a probability of : 0.1333334")
print("(d) Choosing a person of age 17 has a probability of : 0.2")
print("(e) Choosing a person of age 18 has a probability of : 0.0666667")
print("(f) Choosing a person of age 19 has a probability of : 0.1333334")
print("(g) Choosing a person of age 20 has a probability of : 0.2")
print("(h) Choosing a person of age 21 has a probability of : 0.0666667")

#Calculating the mean, variance and standard deviation of the given data 
sim_mean = np.average(initial_ages)
sim_var = np.var(initial_ages)
sim_stddev = np.std(initial_ages)
print(f"The simulated values of mean, variance and standard deviation are {sim_mean}, {sim_var} and {sim_stddev} respectively")
print(f"The theoretical values of mean, variance and standard deviation are 17.53, 4.78 and 2.18 respectively")
print("Drawing the comparison graphs with ages on x-axis, probabilities on y-axis, blue bar representing simulations and orane bar representing theoretical value")
probabilities_theor = [0.1333334, 0.0666667, 0.1333334, 0.2, 0.0666667, 0.1333334, 0.2, 0.0666667]
x_axis = list(set(unique_ages))
N = 8
blue_bar = probabilities_simu
orange_bar = probabilities_theor
ind = np.arange(N)
width = 0.3
plt.bar(ind, blue_bar , width, label="Simulations' data")
plt.bar(ind + width, orange_bar, width, label='Theoretical data')
plt.xlabel('Ages of students')
plt.ylabel('Probabilities')
plt.title('Comparison plot between simulated and theoretical estimations.')

plt.xticks(ind + width / 2, x_axis)
plt.legend(loc='best')
plt.show()

