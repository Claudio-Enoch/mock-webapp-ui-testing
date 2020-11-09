import pytest


@pytest.mark.parametrize("product_view", ["list", "grid"])
def test_modal(my_store, product_view):
    my_store.index_page.navbar.click_category_women()
    grid_products = my_store.index_page.product_content.get_products(product_view=product_view)
    product_id, product_properties = next(iter(grid_products.items()))
    modal_properties = my_store.index_page.product_content.preview_product(product_id=product_id)
    assert modal_properties == product_properties, f"modal does not match product for: {product_properties.get('name')}"


def test_list_and_grid_data_integrity(my_store):
    my_store.index_page.navbar.click_category_women()
    list_view_products = my_store.index_page.product_content.get_products("list")
    grid_view_products = my_store.index_page.product_content.get_products("grid")
    assert list_view_products, "no items found to compare"
    assert list_view_products == grid_view_products, "product data from list view does not match grid view"
