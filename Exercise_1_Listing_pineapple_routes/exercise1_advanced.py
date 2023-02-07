portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def permutations(route, ports):
    # Write your recursive code here
    if len(ports) <= 0:  
    # Print the port names in route when the recursion terminates
        print(' '.join([portnames[i] for i in route]))
        return
    for port in ports:
        subroute = route.copy()
        subroute.append(port)
        subports = ports.copy()
        subports.remove(port)
        permutations(subroute, subports)


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))
