def convert_grade(grade, name) :
  if grade >= 94.5 :
    print "%(name)s got an A!" % locals()
  elif grade >= 90 :
    print "%(name)s got an A-. pretty good I guess." % locals()
  elif grade >= 80 :
    print "%(name)s got somewhere in the B range." % locals()
  elif grade >= 70 :
    print "%(name)s got a C. Shape up if you want to live." % locals()
  elif grade >= 0 :
    print "%(name)s got less than a C. %(name)s is no longer welcome here." % locals()
  elif grade < 0 :
    print "%(name)s is a liar. You can't get less than zero!" % locals()

def user_input():
  name = str(raw_input("Name:"))
  grade = float(raw_input("Grade:"))
  convert_grade(grade, name)

user_input()