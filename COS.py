import csv

def generate_report():
    # Initialize totals for the 4 courses
    bio_tot, cos_tot, sta_tot, gst_tot, count = 0, 0, 0, 0, 0
    
    with open("Amirat.csv", "r") as f:
        data_reader = csv.reader(f)
        header = next(data_reader) # Skip the headers row
        
        for record in data_reader:
            if not record: 
                continue
            # Read columns by index: Name=0, BIO101=1, COS101=2, STA111=3, GST112=4
            bio_tot += int(record[1])
            cos_tot += int(record[2])
            sta_tot += int(record[3])
            gst_tot += int(record[4])
            count += 1

    # Calculate the 4 averages
    b_avg = bio_tot / count
    c_avg = cos_tot / count
    s_avg = sta_tot / count
    g_avg = gst_tot / count

    # Write summaries to the report file
    with open("report.txt", "w") as out:
        out.write("============ STUDENT PERFORMANCE REPORT ============\n")
        out.write(f"Total Students Processed: {count}\n\n")
        out.write(f"Average BIO101 Score: {b_avg:.2f}\n")
        out.write(f"Average COS101 Score: {c_avg:.2f}\n")
        out.write(f"Average STA111 Score: {s_avg:.2f}\n")
        out.write(f"Average GST112 Score: {g_avg:.2f}\n")
        out.write("====================================================\n")

generate_report()
print("Report successfully generated as 'report.txt'!")

print("\n--- Displaying Generated Report ---")
print(open("report.txt").read())
