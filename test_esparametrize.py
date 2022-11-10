import pytest

@pytest.mark.parametrize("username,password",
                         [
                            ("user1","mobile1"),
                            ("user2","mobile2"),
                            ("user3","mobile3"),
                         ]
                         )
def test_parametrize(username,password):
    print(username)
    print(password)
