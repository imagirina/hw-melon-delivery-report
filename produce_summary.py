def generate_report():
    reports = ['um-deliveries-day-1.txt', 'um-deliveries-day-2.txt', 'um-deliveries-day-3.txt']
    day = 1
    for report in reports:
        print(f"Day {day}")
        the_file = open(report)
        for line in the_file:
            line = line.rstrip()         
            melon, count, amount = line.split('|')

            print(f"\tDelivered {count} {melon}s for total of ${amount}")
        the_file.close()
        day += 1

generate_report()