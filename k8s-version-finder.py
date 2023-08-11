import traceback

# in k8s, there are 3 possible version types:
alpha = ['v1alpha1', 'v2alpha1', 'v2alpha2', 'etc']
beta = ['v1beta1', 'v1beta3', 'v2beta2', 'etc']
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

def return_newest_version_index(versions: list) -> int:
    latest_version_index = 0
    version_check = max(versions)
    for i in range(len(versions)):
        if len(versions[i]) == 2 and versions[i][1] >= version_check[1]:
            version_check = versions[i]
            latest_version_index = i
        elif versions[i] == version_check:
           latest_version_index = i
    return latest_version_index
    



#########################################################
# Tests : Run this python file to see if the tests pass #             
#########################################################

def test_alphas():
    assert return_newest_version_index(
        ['v1alpha1', 'v2alpha2', 'v2alpha1']
    ) == 1, "Should be 1"
    print('passed test_alphas()')

def test_alpha_beta():
    assert return_newest_version_index(
        ['v1alpha3', 'v1alpha2', 'v1beta1']
    ) == 2, "Should be 2"
    print('passed test_alpha_beta()')

def test_general_alpha_beta():
    assert return_newest_version_index(
        ['v1', 'v1beta2', 'v1alpha3', 'v1beta4']
    ) == 0, "Should be 0"
    print('passed test_general_alpha_beta()')


def test_multiple():
    assert return_newest_version_index(
        ['v3alpha6', 'v2beta2', 'v1alpha7', 'v3beta4', 'v2alpha1', 'v3', 'v3beta5', 'v2', 'v1']
    ) == 5, "Should be 5"
    print('passed test_multiple()')


if __name__ == "__main__":

    try:
        test_multiple()
    except:
        print(traceback.format_exc())
    
    try:
        test_alphas()
    except:
        print(traceback.format_exc())
    
    try:
        test_alpha_beta()
    except:
        print(traceback.format_exc())
    
    try:
        test_general_alpha_beta()
    except:
        print(traceback.format_exc())