def test_single_item(my_store):
    my_store.index_page.navbar.click_category_women()
    products_dict = my_store.index_page.product_content.get_products()
    product_id, product_properties = next(iter(products_dict.items()))
    my_store.index_page.product_content.add_product_to_cart(product_id=product_id)
    my_store.index_page.navbar.click_cart()
    cart_dict = my_store.cart_page.get_products()
    assert product_id in cart_dict, "selected product does not appear in cart"
    assert cart_dict[product_id]["price"] == product_properties["price"]
    assert cart_dict[product_id]["name"] == product_properties["name"]
    assert cart_dict[product_id]["quantity"] == 1
    assert cart_dict[product_id]["color"] in product_properties["colors"]


def test_multiple_items(my_store):
    my_store.index_page.navbar.click_category_women()
    products_dict = list(my_store.index_page.product_content.get_products().items())[:3]
    for product_id, product_properties in products_dict:
        my_store.index_page.product_content.add_product_to_cart(product_id=product_id)

    my_store.index_page.navbar.click_cart()
    cart_dict = my_store.cart_page.get_products()

    for product_id, product_properties in products_dict:
        assert product_id in cart_dict, "selected product does not appear in cart"
        assert cart_dict[product_id]["price"] == product_properties["price"]
        assert cart_dict[product_id]["name"] == product_properties["name"]
        assert cart_dict[product_id]["quantity"] == 1
        assert cart_dict[product_id]["color"] in product_properties["colors"]


def test_single_item_delete(my_store):
    my_store.index_page.navbar.click_category_women()
    products_dict = list(my_store.index_page.product_content.get_products().items())[:3]
    for product_id, product_properties in products_dict:
        my_store.index_page.product_content.add_product_to_cart(product_id=product_id)

    my_store.index_page.navbar.click_cart()
    product_id_to_delete = products_dict[-1][0]
    my_store.cart_page.delete_product(product_id=product_id_to_delete)
    cart_dict = my_store.cart_page.get_products()

    assert len(cart_dict) == 2
    assert product_id_to_delete not in cart_dict


def test_all_item_delete(my_store):
    my_store.index_page.navbar.click_category_women()
    products_dict = list(my_store.index_page.product_content.get_products().items())[:3]
    for product_id, product_properties in products_dict:
        my_store.index_page.product_content.add_product_to_cart(product_id=product_id)

    my_store.index_page.navbar.click_cart()
    for product_id, product_properties in products_dict:
        my_store.cart_page.delete_product(product_id=product_id)
    cart_dict = my_store.cart_page.get_products()

    assert len(cart_dict) == 0


def test_increase_item_quantity(my_store):
    pass
