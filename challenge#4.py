def fitsInOneBox(boxes):
    def check_boxes(i):
        if i == len(boxes) - 1:
            return True
        current_box = boxes[i]
        next_box = boxes[i+1]
        if current_box['l'] < next_box['l'] and current_box['w'] < next_box['w'] and current_box['h'] < next_box['h']:
            return check_boxes(i+1) 
        return False
    boxes.sort(key=lambda box: max(box.values()))
    return check_boxes(0)

boxes = [
    {'l': 1, 'w': 1, 'h': 1},
    {'l': 2, 'w': 2, 'h': 2},
    {'l': 3, 'w': 1, 'h': 3}
]

print(fitsInOneBox(boxes))