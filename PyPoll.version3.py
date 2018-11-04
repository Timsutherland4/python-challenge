import os
import csv

# Declare your variables
candidates = []
number_votes = 0
vote_counts = []

election_data = ['1', '2']

# Start For Loop through file
for files in election_data:
    #find csv file
    election_dataCSV = csvpath = os.path.join("election_data.csv")
       
    with open(election_dataCSV) as csvfile:
        
        csvreader = csv.reader(csvfile, delimiter=',')
        
        line = next(csvreader,None)
        
        # Nested For Loop
        for line in csvreader:
            
            #Establish vote count
            number_votes = number_votes +1
            
            # Establish Candidate
            candidate = line[2]
            
            # add subsequent votes to candidate total
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1
                
                # Make new spot for candidate in list
            else:
                candidates.append(candidate)
                vote_counts.append(1)
                
    #Declare more variables:
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0
    
    #Work out percentages and winner (loop)
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/number_votes*100
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]
    
    percentages = [round(i,2) for i in percentages]
    
    # Summary
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {number_votes}")
    print("--------------------------")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("--------------------------")
    print(f"Winner:  {winner}")
    print("--------------------------")
    
    #Export file name and open
    output_file = election_dataCSV[0:-4]
    
    write_election_dataCSV = f"{output_file}pypoll_results.txt"
    
    filewriter = open(write_election_dataCSV, mode = 'w')
    
    # Write results to export file
    filewriter.write("Election Results\n")
    filewriter.write("-----------------------------\n")
    filewriter.write(f"Total Votes:  {number_votes}\n")
    filewriter.write("-----------------------------\n")
    for count in range(len(candidates)):
        filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
    filewriter.write("-----------------------------\n")
    filewriter.write(f"Winner:  {winner}\n")
    filewriter.write("-----------------------------\n")
    
    
    # Close File
    filewriter.close()
    
    
                
                
                 
            
            
    
    