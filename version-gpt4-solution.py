import traceback

def get_latest_version_index(versions):
    # Define the order of precedence for release types
    release_order = {'': 3, 'beta': 2, 'alpha': 1}

    def version_key(version):
        # Extract the version number and release type
        if 'alpha' in version or 'beta' in version:
            version_num, release_type, release_num = version.split('v')[1].split('alpha') if 'alpha' in version else version.split('v')[1].split('beta')
        else:
            version_num = version.split('v')[1]
            release_type = ''
            release_num = 0

        return (int(version_num), release_order[release_type], int(release_num) if release_num else 0)

    # Find the index of the latest version
    latest_index = max(range(len(versions)), key=lambda i: version_key(versions[i]))

    return latest_index

def test_alphas():
    assert get_latest_version_index(
        ['v1alpha1', 'v2alpha2', 'v2alpha1']
    ) == 1, "Should be 1"
    print('passed test_alphas()')

def test_alpha_beta():
    assert get_latest_version_index(
        ['v1alpha3', 'v1alpha2', 'v1beta1']
    ) == 2, "Should be 2"
    print('passed test_alpha_beta()')

def test_general_alpha_beta():
    assert get_latest_version_index(
        ['v1', 'v1beta2', 'v1alpha3', 'v1beta4']
    ) == 0, "Should be 0"
    print('passed test_general_alpha_beta()')

def test_multiple():
    assert get_latest_version_index(
        ['v103beta2', 'v3alpha6', 'v2beta2', 'v1alpha7', 'v3beta4', 'v2alpha1', 'v3', 'v3beta5','v4', 'v2', 'v1', 'v102']
    ) == 0, "Should be 0"
    print('passed test_multiple()')


if __name__ == "__main__":

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
    
    try:
        test_multiple()
    except:
        print(traceback.format_exc())
    