from dcache._utils import prefix_filename


def test_prefix_filename():
    new_name = prefix_filename(filename="name", prefix="dcache_")

    assert new_name == "dcache_name"
