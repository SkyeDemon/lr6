import unittest
import os
from app import app, db, User, Owner, Rep, House, Event
class TestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join('test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_main(self):
        result = self.app.get('/')

    def test_User(self):
        z = User(login='login', password_hash='password', name='name', dateb='03.02.2021', Number_Doc='1555 064088')
        db.session.add(z)
        db.session.commit()
        assert z.login == 'login'
        assert z.password_hash == 'password'
        assert z.name == 'name'
        assert z.dateb == '03.02.2021'
        assert z.Number_Doc == '1555 064088'

    def test_Owner(self):
        z = Owner(Nickname='OOO', Name='Nick', Type='Type', Number='+ 79969213225')
        db.session.add(z)
        db.session.commit()
        assert z.Nickname == 'OOO'
        assert z.Name == 'Nick'
        assert z.Type == 'Type'
        assert z.Number == '+ 79969213225'

    def test_Rep(self):
        p = Rep(Name_house='Name', Mark='Оценка 5', When='03.02.2021', Comment='Normal')
        db.session.add(p)
        db.session.commit()
        assert p.Name_house == 'Name'
        assert p.Mark == 'Оценка 5'
        assert p.When == '03.02.2021'
        assert p.Comment == 'Normal'

    def test_House(self):
        p = House(Name='Name', Name_owner='Name owner', Type='Type', Index='address', Slots='5 slots', Status='Open',
                  Data_open='03.02.2021')
        db.session.add(p)
        db.session.commit()
        assert p.Name == 'Name'
        assert p.Name_owner == 'Name owner'
        assert p.Type == 'Type'
        assert p.Index == 'address'
        assert p.Slots == '5 slots'
        assert p.Status == 'Open'
        assert p.Data_open == '03.02.2021'

    def test_Event(self):
        p = Event(Name='Name', Name_house='Name owner', Type='Type', Data='03.02.2021')
        db.session.add(p)
        db.session.commit()
        assert p.Name == 'Name'
        assert p.Name_house == 'Name owner'
        assert p.Type == 'Type'
        assert p.Data == '03.02.2021'


if __name__ == '__main__':
    unittest.main()