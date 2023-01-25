def fitsInOneBox(boxes):
    def box_check(i):
        if i == len(boxes) - 1:
            return True
        c_box = boxes[i]
        n_box = boxes[i+1]
        if c_box['l'] < n_box['l'] and c_box['w'] < n_box['w'] and c_box['h'] < n_box['h']:
            return box_check(i+1) 
        return False
    boxes.sort(key=lambda box: max(box.values()))
    return box_check(0)

boxes = [
    {'l': 1, 'w': 1, 'h': 1},
    {'l': 2, 'w': 2, 'h': 2},
    {'l': 3, 'w': 1, 'h': 3}
]

print(fitsInOneBox(boxes))