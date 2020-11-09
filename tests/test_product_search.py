import pytest


@pytest.mark.parametrize("category", ["Tops", "Dresses"])
def test_search_by_category(my_store, category):
    my_store.index_page.navbar.click_category_women()
    category_dict = my_store.index_page.filter_navbar.get_categories()
    my_store.index_page.navbar.search(category)
    search_result_count = my_store.index_page.product_content.get_search_count()
    assert category_dict[category] == search_result_count, "search results do not match category filter results"


def test_search_non_existent_item(my_store):
    my_store.index_page.navbar.search("NOT_A_REAL_CATEGORY")
    search_result_count = my_store.index_page.product_content.get_search_count()
    assert search_result_count is 0, "search returned result for non-item query"
