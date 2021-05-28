# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io, os, sys
from collections import Counter
import random


# %%
def read_file(filename):
    data = io.open(filename, "r")
    duration_of_sim, num_intersections, num_streets, num_cars, points = [
        int(we_dont_care) for we_dont_care in data.readline().split()
    ]
    input_data = [line.split() for line in data]
    streets = {
        line[2]: {
            "beginning_intersection": int(line[0]),
            "end_intersection": int(line[1]),
            "duration": int(line[3])
        }
        for idx, line in enumerate(input_data[:num_streets])
    }
    cars = ({"num_streets": int(line[0]), "streets": line[1:]} for line in input_data[num_streets:])
    return duration_of_sim, num_intersections, num_streets, num_cars, points, list(cars), streets


# %%


filename = "a"
duration_of_sim, num_intersections, num_streets, num_cars, points, cars, streets = read_file(f"../{filename}.txt")
cnt = Counter([street for car in cars for street in car["streets"][:-1]])


# cnt_first_street = Counter([car["streets"][0] for car in cars])
cnt_first_street = Counter({key: 0 for key in streets.keys()})
cnt_first_street.update([car["streets"][0] for car in cars])

# mapping = {i: [] for i in range(num_intersections)}
# for key, street in streets.items():
#     mapping[street["end_intersection"]].append(key)

street2id = {key: idx for idx, key in enumerate(streets.keys())}
id2street = {val: key for key, val in street2id.items()}

route_matrix = np.zeros((num_cars, num_streets, num_streets))
current_pos = np.zeros((num_cars, num_streets))
for idx, car in enumerate(cars):
    route = car["streets"]
    for i in range(0, len(route)):
        from_to_destination = route[i:i + 2]
        current_pos[idx, street2id[route[0]]] = 1
        if len(from_to_destination) > 1:
            street_from, street_to = from_to_destination
            street_from_id = street2id[street_from]
            street_to_id = street2id[street_to]
            route_matrix[idx, street_from_id, street_to_id] = streets[street_to]["duration"]
            car["route"] = route_matrix[idx]
            car["init"] = current_pos[idx]
            car["next"] = car["init"] @ car["route"]   


mapping = {i: [] for i in range(num_intersections)}
for key, street in streets.items():
    mapping[street["end_intersection"]].append(key)
new_num_intersections = 0
schedule = {i: [] for i in range(num_intersections)}
for key, intersections in mapping.items():
    if len(intersections) == 1:
        new_num_intersections += 1
        schedule[key].append((intersections[0], 1))
    if len(intersections) > 1:
        sum_of_appearances = 0
        for street in intersections:
            sum_of_appearances += cnt[street]
        if sum_of_appearances > 0:
            new_num_intersections += 1
            for street in intersections:
                schedule[key].append((street, (cnt[street] // sum_of_appearances) + 1 + random.randint(0, 1)))
    schedule[key].sort(key=lambda t: cnt_first_street[t[0]], reverse=True)


shedule_matrix = np.zeros((duration_of_sim, num_streets, num_streets))
for key, plan in schedule.items():
    for offset, intersection_shedule in enumerate(plan):
        from_street, pattern = intersection_shedule
        shedule_matrix[offset::pattern, street2id[from_street], key] = 1

next_to_go = np.zeros((1, num_cars))
for idx, car in enumerate(cars):
    # print(idx)
    # print(car["next"])
    # print(car["next"].sum())
    if car["next"].sum() == 1:
        next_to_go[0, idx] = 1


example_car = cars[1]
# car_path_over_route = 


# with io.open(f"../out/{filename}.out", "w") as f:
#     f.write(f"{new_num_intersections}\n")
#     for key, plan in schedule.items():
#         len_plan = len(plan)
#         if not len_plan:
#             continue
#         f.write(f"{key}\n{len_plan}\n")
#         for intersection_shedule in plan:
#             f.write(f"{intersection_shedule[0]} {intersection_shedule[1]}\n")

# run_one("a")
# run_one("b")
# run_one("c")
# run_one("d")
# run_one("e")
# run_one("f")
# %%
