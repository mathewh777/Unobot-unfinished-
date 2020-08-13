
# -*- coding: utf-8 -*-
#import socket
#Many lazy parts 

def move(card_in_play, wild, wild_f, colors, matches):
	#a few var that havent been used 
	B, Y, R, G = colors
	count_skip = 0
	count_rev = 0
	count_dr = 0
	count_norm = 0
	count_col = 0
	count_colors = 0
	#Low = min(colors)
        #Max = max(colors)
        #move = 0
	#          0   1   2   3   4   5   6   7
	colors = [B, Y, R, G]
	matches = matches.split(":End:")

	#counts the amout of skips and etc in total
	for i in range(len(matches)):
		if matches[i][16:18] == "s":
			count_skip += 1
		if matches[i][16:18] == "r":
			count_rev += 1
		if matches[i][16:18] == "dt":
			count_dr += 1
		else:
			count_norm += 1
 
	#colors[3*2] = "G"
	#colors[2*2] = "R"
	#colors[1*2] = "Y"
	#colors[0*2] = "B"

	return colors.index(B) #matches[0], len(matches), colors[::-1]
#Lazy 
def get_color_count(deck):
	colors = ["B","Y","R","G"]
	Y = 0
	B = 0
	R = 0
	G = 0
	deck = deck.split(":End:")
	for i in range(len(deck)):
		if colors[0].lower() in deck[i][7:8]:
			B += 1
		if colors[1].lower() in deck[i][7:8]:
			Y += 1
		if colors[2].lower() in deck[i][7:8]:
			R += 1
		if colors[3].lower() in deck[i][7:8]:
                	G += 1
		else:
			pass

	return B, Y, R, G

def Get_wild(deck):
	count = 0
	wild_f = 0
	wild = 0
	if "," in deck:
		a = deck.split(",")
		for i in range(len(deck)):
			try:
				if a[i] == "12r  1":
					wild_f += 1
					wild -= 1
				if a[i] == "8 W0":
					wild += 1
				else:
					pass
			except:
				pass
	return wild_f, wild


def Matches(card_in_play, deck):
	#matches cards in play against your deck to find ones u can use
	#for your turn 
	#Color card[i][7:8]:
        #Object card[i][16:17]: = 0 doesnt get the additonal chars like dt and dr 
	matches = []
	card = card_in_play.split(":Object:")
	Color = card[0][7:8]
	Object = card[1][0]
	card = deck.split(":End:")
	for i in range(len(deck)):
		try:
			# matches draw two cards
			if card[i][16:18] == "dt":
				matches += ":Color:"+card[i][7:8] +":Object:"+ card[i][16:18] +":End:"
			#matches color
			if card[i][7:8] == Color:
				if card[i][7:8] == "":
					pass
				else:
					matches += ":Color:"+card[i][7:8]+":Object:" + card[i][16:18] +":End:"
			#Matches Object
			elif card[i][16:18] == Object:
                                if card[i][16:18] == "":
                                        pass
                                else:
                                        matches += ":Color:"+card[i][7:8] +":Object:"+ card[i][16:18]+":End:"
			else:
				pass
		except:
			pass

	matches = ''.join(matches)
	return str(matches)


#sort func to the cards given
def get_card_value(array_cards):
	deck = []
	color_check = ["G", "R", "Y", "B"]
	i = 0
	#array_cards = "12 Blue Skip  0,03 Green 1  0,03 Green Reverse  0"Not  #Got Em
	#array_cards = "Blue 9 Red 1 Red 3 Yellow 5 Red 2 Green Skip Blue 2" NOt Got Em

	#Sorts theses Values "12 Blue Skip  0,03 Green 1  0,03 Green Reverse  0"
	#Sorts Theses "Blue 9 Red 1 Red 3 Yellow 5 Red 2 Green Skip Blue 2"
	array_cards = array_cards.split(" ", len(array_cards))
	for check_col in range(len(color_check)):
		for i in range(len(array_cards)):
			try:
				if array_cards[i][0:1] == color_check[check_col]:
					if array_cards[i+1][0:1].lower() == "d":
						deck += ":Color:" + array_cards[i][0:1].lower() + ":Object:"+array_cards[i+1][0:1].lower()+array_cards[i+2][0:1].lower()+":End:"
					else:
						if array_cards[i+1][0:1].lower() == "":
							pass
						else:
							deck += ":Color:" + array_cards[i][0:1].lower() + ":Object:"+array_cards[i+1][0:1].lower()+":End:"
			except:
				pass
	return ''.join(deck)


test = "0,04 Blue Draw Two  0,03 Green 1  0,03 Green Draw Two  0,03 Green 1  0,03 Green Reverse  0"
deck = get_card_value(test)
print "Your cards -> " + deck 

card_in_play = get_card_value("0 04 Yellow Draw Two 1 0")
print "Card in Play -> "+ card_in_play

wild_f, wild = Get_wild(deck)

print "Wildcards -> "+str(wild) +"\nSpecial Wildscards -> " + str(wild_f)
print "Your Colors: ", get_color_count(deck)

colors = get_color_count(deck)

print "Play: ", move(card_in_play, wild, wild_f, colors, Matches(card_in_play, deck))
#single: w 
#draw two: rdt
#pl wdr wd4 wdf
print "Move: ", Matches(card_in_play, deck)


