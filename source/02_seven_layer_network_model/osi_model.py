# Make boxes
top_margin = 10
box_left_margin = 5
text_left_margin = 20
height = 35
space_between_boxes = 50
text_y_offset = 25
box_width = 200
line_width = 3
interval = height + space_between_boxes
middle_of_box = box_width / 2 + box_left_margin
left_right_arrow_separation = 20

arrow_height = 4
arrow_width = 4

output_file = open("osi_model.svg", "w")

out = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="{box_width+text_left_margin}"
   height="600"
   id="svg2"
   version="1.1"
>
"""
output_file.write(out)

out = """<style>
.my_style { font: 20px "Arial", Serif; }
</style>
"""
output_file.write(out)


out = f"""<defs>
<marker id="arrow" markerWidth="{arrow_height}" markerHeight="{arrow_width}" refX="0" refY="{arrow_width/2}" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 V{arrow_width} L{arrow_height},{arrow_width/2} z" fill="black" />
</marker>
</defs>
"""
output_file.write(out)


labels = ["Application Layer", "Presentation Layer", "Session Layer", "Transport Layer", "Networking Layer", "Data Link Layer", "Physical Layer"]

for box in range(7):
    # Make box
    y = box * interval + top_margin
    out = f'<rect x="{box_left_margin}" y="{y}" rx="20" ry="20" width="{box_width}" height="{height}" style="fill:None;stroke:black;stroke-width:{line_width};" />\n'
    output_file.write(out)

    # Make label
    text = labels[box]
    out = f'<text x="{text_left_margin}" y="{y+text_y_offset}" class="my_style">{text}</text>\n'
    output_file.write(out)

    # Make arrow
    if box != 0:
        y1 = y
        y2 = y - (space_between_boxes - (line_width / 2) - arrow_height * 3)
        x = middle_of_box + left_right_arrow_separation
        out = f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" style="stroke:black;stroke-width:{line_width}" marker-end="url(#arrow)" />\n'
        output_file.write(out)

        y1 = y - space_between_boxes
        y2 = y + ( - (line_width / 2) - arrow_height * 3)
        x = middle_of_box - left_right_arrow_separation
        out = f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" style="stroke:black;stroke-width:{line_width}" marker-end="url(#arrow)" />\n'
        output_file.write(out)


# Box labels

output_file.write("</svg>")
output_file.close()
