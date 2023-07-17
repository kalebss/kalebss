import random


reps = [f"rep_{i}" for i in range(10)]  # Five reps named 'rep_0', 'rep_1', etc.
rep_now_max_opps = [
    random.randint(20, 30) for _ in range(10)
]  # Each rep can handle 20 to 30 leads
total_opps = 100  # There are 100 opportunities to distribute
distribution_group = "Test_Group"  # The name of the distribution group


# prod
def distribute_opps(reps, rep_now_max_opps, total_opps, distribution_group):
    min_opps = 0
    output_array = []
    total_bandwidth = sum(rep_now_max_opps)

    # set up the dictionary_output
    for i in reps:
        output_array.append({"user_id": i, "opps": min_opps})

    # Distribute the opps to the reps with the lowest number of leads
    while total_opps > 0:
        for r in range(len(reps)):
            if output_array[r]["opps"] < rep_now_max_opps[r]:
                output_array[r]["opps"] += 1
                total_opps -= 1
            elif (rep_now_max_opps[r] == 0) & (total_bandwidth == 0):
                error_msg = f"There are no reps with bandwidth for opportunity_distribution for distribution group {distribution_group}"
                print(reps)
                print(output_array)
                raise ValueError(error_msg)
            else:
                continue

    return output_array


# dev
def distribute_opps(reps, rep_now_max_opps, total_opps, distribution_group):
    min_opps = 0
    output_array = []

    # Set up the dictionary_output
    for i in reps:
        output_array.append({"user_id": i, "opps": min_opps})

    # Distribute the opps to the reps with the lowest number of leads
    while total_opps > 0:
        # Sort the output array based on the number of leads each rep has already received
        output_array.sort(key=lambda x: x["opps"])
        for r in range(len(reps)):
            if (
                output_array[r]["opps"]
                < rep_now_max_opps[reps.index(output_array[r]["user_id"])]
            ):
                output_array[r]["opps"] += 1
                total_opps -= 1
            elif (rep_now_max_opps[reps.index(output_array[r]["user_id"])] == 0) & (
                sum(rep_now_max_opps) == 0
            ):
                error_msg = f"There are no reps with bandwidth for opportunity_distribution for distribution group {distribution_group}"
                print(reps)
                print(output_array)
                raise ValueError(error_msg)
            else:
                continue

    return output_array


output = distribute_opps(reps, rep_now_max_opps, total_opps, distribution_group)
for rep in output:
    print(f"User {rep['user_id']} received {rep['opps']} opportunities.")
