import csv
import pygame
pygame.init()

def read_csv(file_name):
	list_csv=[]
	with open(file_name,'r+',newline='') as csv_file:
		reader=csv.reader(csv_file)
		for i in reader:
			list_csv.append(i)
	return list_csv

print(read_csv("entities.csv"))