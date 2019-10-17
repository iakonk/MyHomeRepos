import multiprocessing as mp

#~~~~~~~~~~~ Parse in parallel ~~~~~~~~

def find_substr(line):
    print line

#init objects
pool = mp.Pool(2)
jobs = []

#create jobs
with open("json") as f:
    for line in f:
        jobs.append(pool.apply_async(find_substr, (line,)) )


#wait for all jobs to finish
for job in jobs:
    job.get()

#clean up
pool.close()
#~~~~~~~~~~~ end of Parse in parallel ~~~~~~~~
