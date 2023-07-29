# in k8s, there are 3 possible version types:
alpha = ['v1alpha1', 'v2alpha1', 'v2alpha2', 'etc']
beta = ['v1beta1', 'v1beta2', 'v2beta3', 'etc']
general_release = ['v1', 'v2', 'v3', 'etc']
    
# each version (v#) can have a general release, alpha and beta version
# v1 is newer than v1beta1, but v1 is older than v2beta1 (because of the "v2")

###########################################################################################
# Given a list of versions, write a function that returns the index of the latest version #
###########################################################################################

# for example:
# given versions = ['v1alpha1','v2alpha1','v2beta1', v1]

# the function would return 2 
# because 'v2beta1' is the newest version and sits at index 2

# from newest to oldest, the above versions would be
# 'v2beta1', 'v2alpha1', v1, 'v1alpha1'

def return_newest_versions(versions):
    pass