import svgwrite


dpi = 300
spacer = .1 * dpi

def to_dpi(x, y):
	return (x*dpi, y*dpi)

def draw_rect(dwg, x, y, width, height):
    dwg.add(dwg.rect(insert=to_dpi(x, y), size=to_dpi(width, height), stroke='black', stroke_width='5', fill='none'))

def full_span_top(dwg):
	draw_rect(dwg, .5, .5, 7.5, 2.425)

def full_span_bottom(dwg):
	draw_rect(dwg, .5, 8.075, 7.5, 2.425)

def row2_left(dwg):
	draw_rect(dwg, .5, 3.025, 4.4, 2.425)

def row2_right(dwg):
	draw_rect(dwg, 5, 3.025, 3, 2.425)

def row3_left(dwg):
	draw_rect(dwg, .5, 5.55, 3, 2.425)

def row3_right(dwg):
	draw_rect(dwg, 3.6, 5.55, 4.4, 2.425)

drawing = svgwrite.Drawing('template.svg', profile='tiny', size=to_dpi(8.5, 11))
full_span_top(drawing)
row2_left(drawing)
row2_right(drawing)
row3_left(drawing)
row3_right(drawing)
full_span_bottom(drawing)
drawing.save()
