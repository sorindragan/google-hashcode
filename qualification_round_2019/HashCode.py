from pprint import pprint
from random import randint, choice
from itertools import chain

def compute_score(current_tags, photo2, ids, next_dir, current_dir):
    ph1_tags = set(current_tags)
    ph2_tags = set(ids[next_dir][photo2])

    score1 = len(ph1_tags.intersection(ph2_tags))
    score2 = len(ph2_tags.difference(ph1_tags))
    score3 = len(ph1_tags.difference(ph2_tags))

    return (photo2, min(score1, min(score2, score3)), next_dir)

def compute_vertical_score(photo1, photo2, ids, next_dir, current_dir):
    ph1_tags = set(ids[current_dir][photo1])
    ph2_tags = set(ids[next_dir][photo2])

    score1 = len(ph1_tags.intersection(ph2_tags))

    return (photo2, score1)

def main():
    with open("a_example.txt") as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]

        no_photos = int(content[0])
        ids_dict = {'H': {}, 'V':{}}
        tags_dict = {}

        for i in range(1, len(content)):
            v = content[i].split(" ")

            ids_dict[v[0]][i - 1] = list(v[2:])

            for tag in list(v[2:]):
                if tag in tags_dict:
                    tags_dict[tag].append(i - 1)
                else:
                    tags_dict[tag] = [i - 1]

        slideshow = []

        chosen_photo = randint(0, len(ids_dict['H']) + len(ids_dict['V']) - 1)
        if chosen_photo in ids_dict["H"]:
            chosen_dir = 'H'
        else:
            chosen_dir = 'V'

        current_tags = ids_dict[chosen_dir][chosen_photo]

        slideshow_size = len(list(ids_dict['H'])) + len(list(ids_dict['V'])) / 2

        while True:
            if len(slideshow) >= slideshow_size:
                break

            if chosen_dir == 'V':
                candidates = []
                for tag in current_tags:
                    tags_dict[tag].remove(chosen_photo)
                    candidates += [id for id in tags_dict[tag] if id in ids_dict['V'] and id != chosen_photo]

                if candidates == []:
                    candidates.append(choice(list(ids_dict['V'])))

                vertical_scores = []
                for photo in candidates:
                    vertical_scores.append(compute_vertical_score(chosen_photo, photo, ids_dict, 'V', 'V'))

                best_vertical = max(vertical_scores, key=lambda item: item[1])

                if chosen_photo != best_vertical[0]:
                    slideshow.append((chosen_photo, best_vertical[0]))

                current_tags = list(set(ids_dict['V'][chosen_photo] + ids_dict['V'][best_vertical[0]]))

                del ids_dict['V'][chosen_photo]
                
                if best_vertical[0] in ids_dict['V']:
                    del ids_dict['V'][best_vertical[0]]

                chosen_photo = best_vertical[0]

            candidates = []
            for tag in current_tags:
                if chosen_photo in tags_dict[tag]:
                    tags_dict[tag].remove(chosen_photo)
                candidates += tags_dict[tag]

            if candidates == []:
                candidates.append(choice(list(ids_dict['V']) + list(ids_dict['H'])))

            scores = []
            for photo in candidates:
                if photo in ids_dict['H']:
                    next_dir = 'H'
                else:
                    next_dir = 'V'
                scores.append(compute_score(current_tags, photo, ids_dict, next_dir, chosen_dir))

            best = max(scores, key=lambda item: item[1])
            best_id = best[0]

            current_tags = ids_dict[best[2]][best_id]
            chosen_dir = best[2]
            chosen_photo = best_id

            if chosen_dir == 'H':
                slideshow.append(chosen_photo)
                del ids_dict['H'][chosen_photo]

        print(slideshow)

        with open('c_out.txt', 'a') as the_file:
            the_file.write(str(len(slideshow)),)
            the_file.write("\n")
            for el in slideshow:
                if isinstance(el, tuple):
                    the_file.write(str(str(el[0]) + " " + str(el[1])),)
                    the_file.write("\n")
                else:
                    the_file.write(str(el),)
                    the_file.write("\n")






if __name__ == '__main__':
    main()
