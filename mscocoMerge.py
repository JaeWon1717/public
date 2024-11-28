import json
from collections import defaultdict

def merge_coco_files(file_list, output_file):
    merged_data = {
        "images": [],
        "annotations": [],
        "categories": []
    }
    image_id_offset = 0
    annotation_id_offset = 0
    
    category_mapping = {}  # To handle consistent category IDs
    category_id_offset = 0

    for file_path in file_list:
        with open(file_path, 'r') as f:
            coco_data = json.load(f)
        
        # Handle categories (ensure unique category mapping)
        if not merged_data["categories"]:
            merged_data["categories"] = coco_data["categories"]
            category_mapping = {cat["id"]: cat["id"] for cat in coco_data["categories"]}
        else:
            for cat in coco_data["categories"]:
                if cat["id"] not in category_mapping:
                    category_id_offset += 1
                    new_category_id = category_id_offset
                    category_mapping[cat["id"]] = new_category_id
                    cat["id"] = new_category_id
                    merged_data["categories"].append(cat)
        
        # Adjust image IDs and annotations
        for image in coco_data["images"]:
            image["id"] += image_id_offset
            merged_data["images"].append(image)

        for annotation in coco_data["annotations"]:
            annotation["id"] += annotation_id_offset
            annotation["image_id"] += image_id_offset
            annotation["category_id"] = category_mapping[annotation["category_id"]]
            merged_data["annotations"].append(annotation)
        
        # Update offsets
        image_id_offset = max(img["id"] for img in merged_data["images"]) + 1
        annotation_id_offset = max(ann["id"] for ann in merged_data["annotations"]) + 1

    # Save merged data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(merged_data, f, indent=4)

# Example usage:
file_list = ["/Users/jaewon/Desktop/NAS_job/job133/133.json", "/Users/jaewon/Desktop/NAS_job/job134/134.json", "/Users/jaewon/Desktop/NAS_job/job135/135.json"]
output_file = "merged_coco.json"
merge_coco_files(file_list, output_file)
