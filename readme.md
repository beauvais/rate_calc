This is a very quick hack I created when waiting for a file-transfer job to complete.

I have a few variables, which are asked for as raw_input:

*gigs_done* is the number of gigabytes which have been transferred already (e.g. 216)
*hrs_so_far* is the number of hours—decimal for partial hrs is ok—(e.g.: 4.25)

The script will convert these into floats, and divide them to give you a gigabyte-per-hour rate.

It will then ask you how many gigs there are in the job, and will tell you how many gigs there are to go, and a rough idea of how long it will take.