import requests
import json
import csv
import sys
import time

def sleep(i):
    if i ==40:
        i =0
        time.sleep(10)
    return i

api = str(sys.argv[1])

with open('movie_ID_name.csv', mode='w') as csv_file, open('movie_ID_sim_movie_ID.csv', mode='w') as csv_sfile:
    
    counter = 0
    #for page in range(1,16):
    movie_ID = []
    for page in range(1,16):
 #       print(page)
        url  = "https://api.themoviedb.org/3/discover/movie?api_key="+ api +"&sort_by=popularity.desc&page=" + str(page) + "&primary_release_date.gte=2000-01-01&with_genres=35"
        counter += 1
        counter = sleep(counter)

        payload = "{}"
        response = requests.request("GET", url, data=payload)
        t = response.json()
        #t=json.loads(response.text)
        # Parse 20 pages and add to the array
        writer = csv.writer(csv_file, delimiter=',', lineterminator="\n")
        
        for i in range(len(t['results'])):
            #There is state is field of database
            movie_ID.append(t['results'][i]['id'])
            writer.writerow([ t['results'][i]['id'] , str(t['results'][i]['original_title']) ])

    movie_sim = {}

    for i in range(len(movie_ID)):
        similar_url = "https://api.themoviedb.org/3/movie/"+str(movie_ID[i])+"/similar?api_key=" + api +"&page=1"
        counter += 1
        counter = sleep(counter)
        y ="{}"
        response_s = requests.request("GET", similar_url, data=y)
        result_similar = response_s.json()

        sim_count = 0


        for j in result_similar['results']:
            # sim_data.append(j['id'])
            if movie_ID[i] in movie_sim:
                if j['id'] in movie_sim:
                    if not movie_ID[i] in movie_sim[j['id']]:
                        movie_sim[movie_ID[i]].append(j['id'])
                      #  print("x")
                else:
                    movie_sim[movie_ID[i]].append(j['id'])
            else:
                if j['id'] in movie_sim:
                    if not movie_ID[i] in movie_sim[j['id']]:
                        movie_sim[movie_ID[i]] = [j['id']]
                     #   print("y")
                else:
                        movie_sim[movie_ID[i]] = [j['id']]
            sim_count += 1
            if (sim_count == 5):
                break
    writer_s = csv.writer(csv_sfile, delimiter=',', lineterminator="\n" )

    for key, value in movie_sim.items():
        for i in range(len(value)):
            #print (key)
            #print(value[i])
            writer_s.writerow([key , value[i] ])






