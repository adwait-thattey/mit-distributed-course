import requests
import json

class Material:
    def __init__(self):
        self.class_name = ""
        self.type = ""
        self.notes = []
        self.papers = []
        self.ytvideos = []
        self.faq = []
        self.others = []

    def serialize(self):
        return {
            "class_name": self.class_name,
            "type": self.type,
            "notes": self.notes,
            "papers": self.papers,
            "ytvideos": self.ytvideos,
            "faq": self.faq,
            "others": self.others
        }

ALL_MATERIALS = []

if __name__ == "__main__":
    infile = open("list.tsv", mode="r")
    for line in infile:
        cells = line.split('\t')
        if len(cells) < 2: continue

        material = Material()
        ALL_MATERIALS.append(material)
        material.class_name = cells[1]
        
        if "lab" in cells[1].lower():
            material.type = "lab"
        elif "lec" in cells[1].lower():
            material.type = "lec"
        else:
            material.type = "unknown"
        
        if material.type == "lab":
            material.others.extend(cells[2:])
            continue

        for cell in cells[2:]:
            if "notes" in cell.lower():
                material.notes.append(cell)
                continue
            elif "papers" in cell.lower():
                material.papers.append(cell)
                continue
            elif "faq" in cell.lower():
                material.faq.append(cell)
                continue
            elif "youtu.be" in cell.lower():
                material.ytvideos.append(cell)
                continue
            else:
                material.others.append(cell)

    
    all_materials = [i.serialize() for i in ALL_MATERIALS]
    all_materials_json = json.dumps(all_materials)

    outfile = open("course_material.json", mode="w")
    outfile.write(all_materials_json)
