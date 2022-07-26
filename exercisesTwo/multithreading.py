# The CPU is regarded as the computer's brain. The CPU is responsible for all data processing operations.
# It saves information such as data, intermediate results, and instructions (program). It directs the operation of all computer components.


from multiprocessing import Process
import os

processes = []
num_processes = os.cpu_count()

print(num_processes)

