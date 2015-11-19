import numpy
 
def get_cosine(v1, v2):
    """ calculate cosine and returns cosine """
    n1 = numpy.linalg.norm(v1)
    n2 = numpy.linalg.norm(v2)
    ip = numpy.dot(v1, v2)
    return ip / (n1 * n2)
  
def get_radian_from_cosine(cos):
    return numpy.arccos(cos)
 
def get_degrees_from_radian(cos):
    return numpy.degrees(cos)
 
def main():
    v1 = numpy.array([1, 0])
    v2 = numpy.array([1, numpy.sqrt(3)])
    cosine = get_cosine(v1, v2)
    print v1,v2,cosine
    radian = get_radian_from_cosine(cosine)
    print get_degrees_from_radian(radian)
 
if __name__ == "__main__":
    main()