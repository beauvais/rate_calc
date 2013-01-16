
gigs_done = float(raw_input("how many gigs have been copied? \n> "))
hrs_so_far = float(raw_input("how many hours have passed since it started? \n> "))


def gig_rate(gigs_done, hrs_so_far):
    return (gigs_done / hrs_so_far)

rate = int(gig_rate(gigs_done, hrs_so_far))

print "OK, the gigs per hour rate is %s" % rate

total_gigs = float(raw_input("How many gigs are there to copy in total? \n> "))


def gigs_to_go(total_gigs, gig_rate):
    remaining = (total_gigs - gigs_done)
    return remaining

to_go = int(gigs_to_go(total_gigs, gig_rate))

print "So, you have %s gigs to go. \n" % to_go


def hrs_remaining(to_go, rate):
    hrs = (to_go / rate)
    return hrs

hrs_to_go = int(hrs_remaining(to_go, rate))

print "At the rate of %s gigs per hour, you have %s hrs remaining." % (rate, hrs_to_go)
