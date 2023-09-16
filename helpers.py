


def read_text_quiz(foldername, filename):
    f = open("data/" + foldername + "/" + filename)
    out = f.readlines()

    way_one = {}
    way_two = {}

    for qa in out:
        pair_list = qa.split("  ")
        q = pair_list[0].strip()
        a = pair_list[1].strip()
        way_one[q] = a
        way_two[a] = q

    return way_one, way_two



def read_image_quiz(foldername, filename):
    f = open("data/" + foldername + "/" + filename)
    out = f.readlines()

    q_image_mapping = {}

    for qa in out:
        pair_list = qa.split("  ")
        q = pair_list[0].strip()
        a = pair_list[1].strip()
        q_image_mapping[q] = a

    return q_image_mapping

