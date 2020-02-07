import list_tool


def test_create_list():
    assert list_tool.create_list() == [1, 2, 3, 4, 50]


def test_append_value_to_list():
    l = list_tool.create_list()
    list_tool.append(l, 5)
    list_tool.append(l, 6)

    assert l == [1, 2, 3, 4, 50, 5, 6]


def test_contain_element():
    l = list_tool.create_list()
    assert list_tool.contain(l, 3)
    assert list_tool.contain(l, 50)
    assert not list_tool.contain(l, 100)
    assert not list_tool.contain(l, 45)


def test_delete_element():
    l = list_tool.create_list()
    assert list_tool.contain(l, 50)
    list_tool.delete(l, 4) # on supprime l'élément à l'index 4, càd la valeur 50
    assert not list_tool.contain(l, 50)


def test_insert_element():
    l = list_tool.create_list()
    assert l == [1, 2, 3, 4, 50]
    list_tool.insert(l, 3, 25)
    assert l == [1, 2, 3, 25, 4, 50]


def test_pop_list():
    l = list_tool.create_list()
    assert l == [1, 2, 3, 4, 50]
    popped_element = list_tool.pop(l, 2)
    assert popped_element == 3
    assert l == [1, 2, 4, 50]


def test_extend():
    l1 = list_tool.create_list()
    l2 = ["a", "b", "c"]
    l_extended = list_tool.extend(l1, l2)
    assert l_extended == [1, 2, 3, 4, 50, "a", "b", "c"]
    l_extended = list_tool.extend(l2, l1)
    assert l_extended == ["a", "b", "c", 1, 2, 3, 4, 50]

