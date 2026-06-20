def build_report(count, b_avg, c_avg, s_avg, g_avg):
    return (
        "============ STUDENT PERFORMANCE REPORT ============\n"
        f"Total Students Processed: {count}\n\n"
        f"Average BIO101 Score: {b_avg:.2f}\n"
        f"Average COS101 Score: {c_avg:.2f}\n"
        f"Average STA111 Score: {s_avg:.2f}\n"
        f"Average GST112 Score: {g_avg:.2f}\n"
        "====================================================\n"
    )
