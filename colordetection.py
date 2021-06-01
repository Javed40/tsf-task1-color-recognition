
import cv2
import pandas as pd

#image path
img_path = 'colorimg.jpg'
img=cv2.imread(img_path)

#csv file reading
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
CSV = pd.read_csv('colors.csv', names=index, header=None)

#reading image
img = cv2.imread(img_path)
img = cv2.resize(img, (1280,720))

#false status unless clicked by Left Mouse Button
clicked = False

#getting R, G & B data from clicking, position on X-Y Plane
r = g = b = x_pos = y_pos = 0

#Defining function to get color name
def get_color_name(R,G,B):
	minimum = 10000                 # minimum threshold of intensity
	for i in range(len(CSV)):
		Dis = abs(R - int(CSV.loc[i,'R'])) + abs(G - int(CSV.loc[i,'G'])) + abs(B - int(CSV.loc[i,'B'])) # getting intensity value from image
		if Dis <= minimum:
			minimum = Dis
			cname = CSV.loc[i, 'color_name']                       # getting color name if intensity is less than threshold
	return cname

# Function to draw mouse cursor
def draw_function(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global b, g, r, x_pos, y_pos, clicked
		clicked = True
		x_pos = x
		y_pos = y
		b,g,r = img[y,x]
		b = int(b)
		g = int(g)
		r = int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

# Function to display color name
while True:
	cv2.imshow('image', img)
	if clicked:
		cv2.rectangle(img, (20,20), (700,60), (b,g,r), -1)
		text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
		cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)
		if r+g+b >=600:
			cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)

			# press ESC to exit
	if cv2.waitKey(20) & 0xFF == 27:
		break
cv2.destroyAllWindows()