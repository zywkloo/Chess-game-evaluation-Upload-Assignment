# ============================================================  
# 
# Student Name (as it appears on cuLearn): Yiwei Zhang          
# Student ID (9 digits in angle brackets): <101071022>               
# Course Code (for this current semester): COMP1405A                
#                                                                   
# ============================================================


'''
This function will ask the user to input legal rows of the chessboard repectively as string format.
@params		none
@return		gameboard 	a list of lists of strings, which is a 8x8 size,containing the chessboard data for each location.
		    []			an empty list,if all location are '-',then return [] 
'''
def inputboard():
	Ord=["1st","2nd","3rd","4th","5th","6th","7th","8th"]
	white="kqrnbp"
	black="KQRNBP"
	gameboard=[]
	nonpiece=True
	'''
	[K]ing    0
	[Q]ueen   10
	[R]ook    5
	k[N]ignt  3.5
	[B]ibshop 3
	[P]awn    1
	''' 
	for x in range(1,9):
		rowinput=True
		while rowinput==True:
			print("Please input the %s row string of the chessboard.\nwhite='k,q,r,n,b,p';black='K,Q,R,N,B,P';empty='-':\n"% (Ord[x-1])) #
			rstring=input("12345678\n────────\n")# a graph helping user to input as correctly as possible
			legal=True
			for piece in rstring:
				if piece not in white+black+'-':  #input letter legal or not 
					legal=False
			if (not len(rstring)==8): #if user input a string whose length is not 8,try again
				print ("The length should be 8,please try AGAIN.")
			elif legal==False :  #if user input letters not in "kqrnbpKQRNBP",try again
				print ("String contains illegal letter,please try AGAIN.")
			else :
				rlist=[]
				for letter in rstring:
					if not letter=="-":
						nonpiece=False #if the board is all made up of "-", denote the gameboard as empty label
					rlist.append(letter)   #append each location string of this row 1 by 1
				gameboard.append(rlist)		#append the list of this row into the gameboard list
				print("The %s row input susceeds.\n"% (Ord[x-1]))
				break
	if nonpiece==True:
		return []		#An empty gameboard consisted by all "-" returns []
	else:
		return gameboard


'''
This function will print a chessboard using an argument of a list of lists of strings, which is a 8x8 size,containing the chessboard data for each location.
It has no return value, and only print the chess board labels row by row .Each row has a length of 8 label.
@params		gameboard   a list of lists of strings, which is a 8x8 size,containing the chessboard data for each location.
@return		none
'''
def drawboard(gameboard):
	row="ABCDEFGH"    # Row coordinate string
	col="12345678"    #	Col coordinate string
	if gameboard==[]:  #if it is an empty chess board without any piece,simply fill the 8x8 board with '-'
		print("  "+col)
		print(" ┌────────┐")
		for i in range (8):
			print (row[i]+"│--------│")   #Display each empty place in this row together	
		print(" └────────┘")
	else:				#if it is not empty ,print the chess board labels row by row .Each row has a length of 8 label
		print("  "+col)	#Display column coordinate
		print(" ┌────────┐")	
		j=0		
		for r in gameboard:
			print (row[j]+"│",end='') #Display the row coordinate or the present row
			for c in r:
				print (c,end='')  #Display each piece in this row one by one 	
			print ("│")
			j+=1
		print(" └────────┘")
'''
This function will take one 2D-list of stings and two strings as three argument.
It mainly tries to use the user-input strings as coordinates to find out the piece of this location.
@params		gameboard 	a list of lists of strings, which is a 8x8 size,containing the chessboard data for each location. 
			prex		a string,the letter representing the column of the position
			prey 		a string,the number representing the row of the position
@return		gameboard[rindex][cindex]
						an uppercase string,containing the data(Piece) read from the file
						if the coordinate in not on the board return boolean value False,
			
'''
def locate(gameboard,prex,prey):
	row="ABCDEFGH"
	col="12345678"
	if (str(prex) not in row) or (str(prey) not in col):
		return False				#if the coordinate in not on the board return boolean value False,
	else:
		rindex= ord(prex)-ord('A') 			#find the index of row
		cindex= int(prey)-1					#find the index of col
		return gameboard[rindex][cindex]		#an uppercase string,containing the data(Piece) read from the file

'''
This function will move a piece from a location to another.If the piece is moved to the same location,warn the user "nothing happens".
Otherwise, the value of expected location will equal to the value of former location.The value of former location will be "-".
It must receive 5 agruments with one 8x8 list of lists of strings and four strings as coordinates of the present position and the expected position to move.
@params		gameboard	a list of lists of strings, which is a 8x8 size,containing the chessboard data for each location.
		prex	a string,the letter representing the column of the 'present' position
		prey	a string,the number representing the row of the 'present' position
		posx	a string,the letter representing the column of the 'expected' position
		posy	a string,the number representing the row of the 'expected' position
@return		gameboard	a list of lists of strings, which is a 8x8 size,containing the chessboard data for each location.
'''
def move(gameboard,prex,prey,posx,posy):
	row="ABCDEFGH"
	col="12345678"
	rind1= ord(prex)-ord('A') 	#find the index of previous row
	cind1= int(prey)-1			#find the index of previous col
	rind2= ord(posx)-ord('A') 	#find the index of expected row
	cind2= int(posy)-1			#find the index of expected col
	if rind1==rind2 and cind1==cind2:  #if location doesnot change warn the user
		print("You didn't do anything!")
	else:
		gameboard[rind2][cind2]=gameboard[rind1][cind1] # overwrite the expected location
		gameboard[rind1][cind1]="-"						# overwrite the previous location with "-"
	#print("I'm %s. I'm %d year old" % ('Hom', 30))`
		print("Move from (%s,%s) to (%s,%s) successfully!" % (str(prex),str(prey),str(posx),str(posy)))
	return gameboard									# return modified gameboard

'''
This function will campare the sum of values of white lowercase letter and the sum of values of black uppercase letter.
It must receive a list of lists of strings as an argument and produce one string return value.
@params		list  a list of lists of strings, which is a 8x8 size,containing the chessboard data for each location.
@return		none
'''
def rating(gameboard):
	'''
	[K]ing    0
	[Q]ueen   10
	[R]ook    5
	k[N]ignt  3.5
	[B]ibshop 3
	[P]awn    1

	''' 
	rate=[0,10,5,3.5,3,1]
	white=['k','q','r','n','b','p']
	black=['K','Q','R','N','B','P']  #initialize all the elements this function needs to use
	wsum=0
	bsum=0
	for row in gameboard:
		for x in row:
			for i in range(0,6):
				if x==white[i]:		#if this letter in the list of strings representing white pieces,plus the corresponding value to white sum.
					wsum+=rate[i]
				elif x==black[i]:	#if this letter in the list of strings representing black pieces,plus the corresponding value to black sum.
					bsum+=rate[i]
				else:
					pass
	print ("White pieces are: ",wsum)
	print ("Black pieces are: ",bsum)
	if wsum>bsum:					#if white value > black display white wins. 
		print ("┌──────────────┐")
		print ("│  White wins! │") 
		print ("└──────────────┘")
	elif wsum<bsum:					#if white value < black display black wins. 
		print ("┌──────────────┐")
		print ("│  Black wins! │")
		print ("└──────────────┘")
	else:							#Otherwise its a tie
		print ("┌──────────────┐")
		print ("│  Draw Game ! │")
		print ("└──────────────┘")
	
'''
 This is the main function,responsible for the user interface.
 @params none
 @return none
'''

def main():#much of your code will go here
	print ("Would you like to see the INSTRUCTION?")
	intr=str(input("Please input 'I' to see the [I]NSTRUCTION.\nOr input any other letters to process the chessboard.(I/other input):"))
	Flag=True
	gameboard=[]
	if intr=="i" or intr=="I" :
		print ("  ┌─[INSTRUCTION]──────────────────────────────────────────────────────┐     ")
		print ("  │     Please input any corresponding letter of the menu,but note you │     ")  # ask the user if instructions needed firstly
		print ("  │ should use H to initial a game board first.                        │     ")
		print ("  │     This is an evaluation system of a chess game,so you can move   │     ")
		print ("  │ piece wherever is on the board.                                    │     ")
		print ("  └────────────────────────────────────────────────────────────────────┘     ")
		input("Press any button to continue....")
	while Flag==True:
		print ("     ┌─[Yiwei's Chessboard Analysis System]───────┐")
		print ("     │ 	H:[H]AND input the gameboard.             │")
		print ("     │	M:[M]OVE exsisting gameboard.             │")		#main menu
		print ("     │ 	I:[I]NSTRUCTION.                          │")
		print ("     │ 	Q:[Q]uit the system.                      │")
		print ("     └────────────────────────────────────────────┘")
		opt1=input("Please input any initial letters shown above:")
		if opt1=="H" or opt1=="h":		# input H/h to hand input the gameboard .
			gameboard=inputboard()	
			drawboard(gameboard)		#If input successfully, draw the gameboard and rate it at once.
			rating(gameboard)
		elif opt1=="M" or opt1=="m":	# input M/m to move the pieces on gameboard .
			if gameboard==[]:
				print("Gamebroad has not been initialized yet.Return to main menu...") #force the user to input gameboard first
			else:
				Flag_move=True
				while Flag_move==True:
					prec=input("Previous Column:please input a number from 1 to 8 as the column of an exsisting piece. \nInput a number in [1-8],or input Q to quit.\n")
					if prec=="Q" or prec=="q":  # user can quit at any time
						print("\nReturn to main menu....") 
						break
					prer=input("Previous Row:please input a letter from A to H as the row of an exsisting piece.\nInput UPPERCASE letter in [A-H],or input Q to quit. \n")
					if prer=="Q"or prer== "q":	 # user can quit at any time
						print("\nReturn to main menu....") 
						break
					if locate(gameboard,prer,prec)==False or len(prer)!=1 or len(prec)!=1: # if the coordinate string longer doesn't have len of 1 or withou a valid piece here,warn the user
						input("\nInput illegally or out of bound, please input any value to try AGAIN.")
					elif locate(gameboard,prer,prec)=="-":				#if the location is empty ,warn
						input ("\nThis position is an empty '-',please input any value to try AGAIN.") 
					else:			
						posc=input("\nExpected Column:please input a number from 1 to 8 as the column for the location you want to move to. \n Input a number in [1-8],or input Q to quit.:\n")
						if prec=="Q"or prec=="q":	 # user can quit at any time
							print("\nReturn to main menu....") 
							break
						posr=input("Expected Row:Please input a letter from A to H as the row for the location you want to move to.\nInput a UPPERCASE letter in [A-H],or input Q to Quit:\n")
						if prer=="Q"or prer== "q":	 # user can quit at any time
							print("\nReturn to main menu....") 
							break
						if locate(gameboard,posr,posc)==False or len(posr)!=1 or len(posc)!=1:  #same len and piece validaty test as above
							input("Input illegally or out of bound, please input any value to try AGAIN.")
						else:
							move(gameboard,prer[0],prec[0],posr[0],posc[0])	#if input valid move the piece
							drawboard(gameboard)		#then draw and rate the board at once
							rating(gameboard)
							Flag_move=False
		elif opt1=="I" or opt1=="i":
			print ("  ┌─[INSTRUCTION]──────────────────────────────────────────────────────┐     ")
			print ("  │     Please input any corresponding letter of the menu,but note you │     ")
			print ("  │ should use H to initial a game board first.                        │     ")
			print ("  │     This is an evaluation system of a chess game,so you can move   │     ")
			print ("  │ piece wherever is on the board.                                    │     ")
			print ("  └────────────────────────────────────────────────────────────────────┘     ")
			input("Press any button to return to main menu....")
		elif opt1=="Q" or opt1=="q":
			exit()						#exit to command line mode
			Flag=False
		else:
			input("Input error.Press any button to return to main menu....\n")  # if user input character not shown on the menu, warn
#this is the only line in your code that isn't inside a function definition
main()
