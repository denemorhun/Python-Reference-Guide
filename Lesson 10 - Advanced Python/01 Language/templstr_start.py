# demonstrate template string functions
from string import Template

def main():
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # TODO: create a template with placeholders

    s = Template ('$who likes $what')

    # TODO: use the substitute method with keyword arguments
    
    s1 = s.substitute(who='denem', what='jazz')
    print(s1)

    # TODO: use the substitute method with a dictionary
    d = dict(who='seda', what='rock')

    s2 = s.substitute(d)
    print(s2)
    
if __name__ == "__main__":
    main()
    