fucks = 2
null = ""

while fucks != null:
    fucks = int(raw_input("How many fucks do you give? "))

    if fucks == 0:
        print "Good for you!"
        break
    elif fucks > 2:
        print "I count a total of %s fucks" % fucks
        print "You give way too many fucks"
    elif fucks < 2:
        print "I count a total of %s fuck" % fucks
        print "You're so close"
    else:
        print "I count a total of %s fucks" % fucks
