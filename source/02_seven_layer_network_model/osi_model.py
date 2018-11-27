output_file = open("osi_model.svg", "w")

out = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="500"
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

# Make boxes
top_margin = 10
box_left_margin = 5
text_left_margin = 20
height = 35
space_between_boxes = 30
text_y_offset = 25
box_width = 200
interval = height + space_between_boxes
labels = ["Application Layer", "Presentation Layer", "Session Layer", "Transport Layer", "Networking Layer", "Data Link Layer", "Physical Layer"]

for box in range(7):
    y = box * interval + top_margin
    out = f'<rect x="{box_left_margin}" y="{y}" rx="20" ry="20" width="{box_width}" height="{height}" style="fill:None;stroke:black;stroke-width:5;" />\n'
    output_file.write(out)
    text = labels[box]

    # <text x="30" y="110" class="my_style">Presentation Layer</text>
    out = f'<text x="{text_left_margin}" y="{y+text_y_offset}" class="my_style">{text}</text>\n'
    output_file.write(out)


# Box labels

output_file.write("</svg>")
output_file.close()
