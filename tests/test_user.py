import pytest

@pytest.mark.run(order=2)
def test_add_new_user(normal_session):
    _ugid = 1
    _name = 'test user'
    _id = 'testuserID'
    _pw = '!@09qwer1234'
    _phone = '000-0000-0000'
    _email = 'test@example.com'
    _profileImg = 'https://example.com/test.jpg'
    # https://stackoverflow.com/a/3564604/7270469
    normal_session.execute('CALL api_to_web_insert_user(:ugid, :name, :id, :pw, :phone, :email, :profileImg, @result, @msg)', 
        {'ugid': _ugid, 'name': _name, 'id': _id, 'pw': _pw, 'phone': _phone, 'email': _email, 'profileImg': _profileImg})
    spResult = normal_session.execute('SELECT @result, @msg').fetchone()
    assert spResult[0] == 1