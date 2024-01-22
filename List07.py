def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    list1[0]=False
    return list1
print (main([0,1,1,1,1,1]))