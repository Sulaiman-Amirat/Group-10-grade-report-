# COS-Project-OVS-group-10-
from file_loader import load_file
from header import get_header
from records import get_records
from init import initialize
from processor import process_records
from calculator import calculate_averages
from report_builder import build_report
from display import display_report

# Step 1: Load CSV
data = load_file()

# Step 2: Get header and records
header = get_header(data)
records = get_records(data)

# Step 3: Initialize counters
bio_tot, cos_tot, sta_tot, gst_tot, count = initialize()

# Step 4: Process records
bio_tot, cos_tot, sta_tot, gst_tot, count = process_records(
    records, bio_tot, cos_tot, sta_tot, gst_tot, count
)

# Step 5: Calculate averages
b_avg, c_avg, s_avg, g_avg = calculate_averages(
    bio_tot, cos_tot, sta_tot, gst_tot, count
)

# Step 6: Build report
report = build_report(count, b_avg, c_avg, s_avg, g_avg)

# Step 7: Save report
with open("report.txt", "w") as f:
    f.write(report)

# Step 8: Display report
display_report()
