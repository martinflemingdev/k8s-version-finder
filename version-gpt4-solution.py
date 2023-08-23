import traceback

def get_newest_version_index(versions):
    # Define the order of stability levels
    stability_order = {'alpha': 1, 'beta': 2, '': 3}  # '' represents general release

    def version_key(version):
        # Extract major version, stability level, and minor version
        major_version = int(''.join(filter(str.isdigit, version.split('alpha')[0].split('beta')[0])))
        stability = ''.join(filter(str.isalpha, version[len(str(major_version)):]))
        minor_version = int(version.split(stability)[1]) if stability and version.split(stability)[1] else 0
        return (major_version, stability_order[stability], minor_version)

    # Find the index of the newest version
    newest_index = max(enumerate(versions), key=lambda x: version_key(x[1]))[0]
    return newest_index

# Test functions
def test_alphas():
    assert get_newest_version_index(
        ['v1alpha1', 'v2alpha2', 'v2alpha1']
    ) == 1, "Should be 1"
    print('passed test_alphas()')

def test_alpha_beta():
    assert get_newest_version_index(
        ['v1alpha3', 'v1alpha2', 'v1beta1']
    ) == 2, "Should be 2"
    print('passed test_alpha_beta()')

def test_general_alpha_beta():
    assert get_newest_version_index(
        ['v1', 'v1beta2', 'v1alpha3', 'v1beta4']
    ) == 0, "Should be 0"
    print('passed test_general_alpha_beta()')

def test_multiple():
    assert get_newest_version_index(
        ['v103beta2', 'v3alpha6', 'v2beta2', 'v1alpha7', 'v3beta4', 'v2alpha1', 'v3', 'v3beta5','v4', 'v2', 'v1', 'v102']
    ) == 0, "Should be 0"
    print('passed test_multiple()')

# Run tests
test_alphas()
test_alpha_beta()
test_general_alpha_beta()
test_multiple()


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
    