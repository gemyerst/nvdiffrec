import json
from os import listdir
from os.path import isfile, join

pose_location = "C:/Users/G/GitHub/datasets/gina_test3/item2/pose"
onlyfiles = [f for f in listdir(pose_location) if isfile(join(pose_location, f))]


def create_frame(file: str) -> dict: #get frame, return dictionary
    with open(pose_location + "/" + file) as f:
        filecontent = f.read()
        lines = filecontent.split(" ")
        transform_matrix = [
            [float(x) for x in lines[i:i + 4]]
            for i in range(0, len(lines), 4)
        ]
        return {
            "file_path": "./images/" + file.split(".")[0],
            "rotation": 0.031415926535897934,
            "transform_matrix": transform_matrix
        }
    

fnal_result = {
    "camera_angle_x": 0.6911112070083618,
    "frames": [
        create_frame(file)
        for file in onlyfiles
    ]
}


with open("C:/Users/G/GitHub/nvdiffrec/data/vision_nerf_outputs/car_buildings/transforms.json", "w") as fout:
    json.dump(fnal_result, fout, indent=4)