import svgwrite


def draw_page_border(dwg):
    dwg.add(dwg.rect(insert=(150,150), size=(2250,3000), stroke='blue', stroke_width='5', fill='none'))


drawing = svgwrite.Drawing('template.svg', profile='tiny', size=(2550, 3300))
draw_page_border(drawing)

drawing.save()
