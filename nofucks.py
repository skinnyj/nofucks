fucks = 2
null = ""

while fucks != null:
    fucks = int(raw_input("How many fucks do you give? "))
  
    if fucks == 0:
        print "Good for you!\n"
        break

    elif fucks > 5:
        print "I count a total of %s fucks" % fucks
        print "You give way too many fucks"
        print "Try....giving less of a fuck\n"

    elif fucks > 2:
        print "I count a total of %s fucks" % fucks
        print "That's still way too many"
        print "Let's try this again...\n"

    elif fucks < 2:
        print "I count a total of %s fuck" % fucks
        print "You're so close\n"

    else:
        print "I count a total of %s fucks" % fucks
        print "A baseline level of fuckery\n"
