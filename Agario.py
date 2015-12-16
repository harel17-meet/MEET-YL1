import meet
import turtle

user_cell = {'radius':20,'x':8, 'y':8, 'dx':1, 'dy':1, 'color':'black', 'shape':'circle'}
cell1 = {'radius':18,'x':5, 'y':150, 'dx':0.8, 'dy':0.8, 'color':'blue', 'shape':'square'}
cell2 = {'radius':10,'x':10, 'y':10, 'dx':-0.8, 'dy':0.8, 'color':'green', 'shape':'square'}
cell3 = {'radius':25,'x':7, 'y':-150, 'dx':0.8, 'dy':0.8, 'color':'red', 'shape':'square'}
cell4 = {'radius':14,'x':100, 'y':-200, 'dx':-0.8, 'dy':0.8, 'color':'purple', 'shape':'square'}
cell5 = {'radius':25,'x':-100, 'y':200, 'dx':0.8, 'dy':0.8, 'color':'green', 'shape':'square'}
cell6 = {'radius':10,'x':150, 'y':150, 'dx':0.8, 'dy':0.8, 'color':'yellow', 'shape':'square'}
cell7 = {'radius':10,'x':125, 'y':-100, 'dx':-0.8, 'dy':0.8, 'color':'orange', 'shape':'square'}
cell8 = {'radius':25,'x':150, 'y':100, 'dx':0.8, 'dy':-0.8, 'color':'yellow', 'shape':'square'}
cell9 = {'radius':16,'x':-125, 'y':50, 'dx':0.8, 'dy':-0.8, 'color':'green', 'shape':'square'}
cell10 = {'radius':14,'x':-45, 'y':300, 'dx':0.8, 'dy':0.8, 'color':'blue', 'shape':'square'}
cell11 = {'radius':14,'x':-250, 'y':50, 'dx':-0.8, 'dy':-0.8, 'color':'pink', 'shape':'square'}
cell12 = {'radius':16,'x':-200, 'y':120, 'dx':-0.8, 'dy':0.8, 'color':'pink', 'shape':'square'}


cells=[]
user_cell = meet.create_cell(user_cell)
cells.append(user_cell)

cell = meet.create_cell(cell1)
cells.append(cell)
cell = meet.create_cell(cell2)
cells.append(cell)
cell = meet.create_cell(cell3)
cells.append(cell)
cell = meet.create_cell(cell4)
cells.append(cell)
cell = meet.create_cell(cell5)
cells.append(cell)
cell = meet.create_cell(cell6)
cells.append(cell)
cell = meet.create_cell(cell7)
cells.append(cell)
cell = meet.create_cell(cell8)
cells.append(cell)
cell = meet.create_cell(cell9)
cells.append(cell)
cell = meet.create_cell(cell10)
cells.append(cell)
cell = meet.create_cell(cell11)
cells.append(cell)
cell = meet.create_cell(cell12)
cells.append(cell)


def check_x_border(cells):
	width = meet.get_screen_width()
	for cell in cells:
		if cell.xcor() > width or cell.xcor() < -width:
			h1 = cell.get_dx()
			cell.set_dx(-h1)


def check_y_border(cells):
	height = meet.get_screen_height()
	for cell in cells:
		if cell.ycor() > height or cell.ycor() < -height:
			h2 = cell.get_dy()
			cell.set_dy(-h2)


exit = True

def eat_cells(cell):
	global exit
	for cell in cells:
		for cell2 in cells:
			x1 = cell.xcor()
			x2 = cell2.xcor()
			y1 = cell.ycor()
			y2 = cell2.ycor()
			distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
			r1 = cell.get_radius()
			r2 = cell2.get_radius()
			min_d = r1 + r2
			if distance < min_d:
				if (r1 > r2):
					cell2.goto(meet.get_random_x(),meet.get_random_y())
					r1 = r1 + r2/10
					cell.set_radius(r1)
					if cell2 == user_cell:
						exit = False
						print("game over")
						turtle.write('Game Over' , align='center', font=('ariel',50,'bold'))
					if user_cell.radius > 75:
						exit = False
						print("You Win")
						turtle.write('You Win' , align='center', font=('ariel',50,'bold'))


while exit:
	x,y = meet.get_user_direction(user_cell)
	user_cell.set_dx(x)
	user_cell.set_dy(y)
	meet.move_cells(cells)

	check_x_border(cells)	
	check_y_border(cells)
	
	eat_cells(cells)

meet.mainloop()