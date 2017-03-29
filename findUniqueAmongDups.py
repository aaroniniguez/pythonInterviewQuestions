def find_unique_delivery_id(delivery_ids):
    unique_delivery_id = 0
    for delivery_id in  delivery_ids:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id
mylist = [1,2,3,4,4,3,2,1,5,6,6]
print find_unique_delivery_id(mylist)
