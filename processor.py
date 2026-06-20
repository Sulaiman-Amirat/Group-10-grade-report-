def process_records(records, bio_tot, cos_tot, sta_tot, gst_tot, count):
    for record in records:
        if not record:
            continue

        bio_tot += int(record[1])
        cos_tot += int(record[2])
        sta_tot += int(record[3])
        gst_tot += int(record[4])
        count += 1

    return bio_tot, cos_tot, sta_tot, gst_tot, count
