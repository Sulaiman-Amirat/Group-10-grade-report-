def calculate_averages(bio_tot, cos_tot, sta_tot, gst_tot, count):
    b_avg = bio_tot / count
    c_avg = cos_tot / count
    s_avg = sta_tot / count
    g_avg = gst_tot / count

    return b_avg, c_avg, s_avg, g_avg
