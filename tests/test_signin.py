def test_sign_in(my_store):
    my_store.index_page.navbar.click_sign_in()
    my_store.login_page.log_in()
    assert "controller=my-account" in my_store.url, "failed to rout to account home page, after log in"


def test_sign_in_bad_credentials(my_store):
    my_store.index_page.navbar.click_sign_in()
    my_store.login_page.log_in(password="bad_password")
    assert my_store.login_page.alert_message == "There is 1 error\nAuthentication failed."


def test_sign_out(my_store):
    my_store.index_page.navbar.click_sign_in()
    my_store.login_page.log_in()
    my_store.index_page.navbar.click_sign_out()
    assert "controller=authentication" in my_store.url, "did not return to login page after sign out"


def test_cookie_deletion(my_store):
    my_store.index_page.navbar.click_sign_in()
    my_store.login_page.log_in()
    my_store._driver.delete_all_cookies()
    my_store._driver.refresh()
    assert "controller=authentication" in my_store.url, "did not return to login page after deleting cookies"
