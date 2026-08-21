from main import get_weather

def test_weather():
    assert get_weather(21) == "hot"
    assert get_weather(21) == "cold"


from main import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    
def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10,0)


from main import UserManager


@pytest.fixture
def user_manager():
    """Create a fresh instance of UserManager before each test"""
    return UserManager

def test_add_user(user_manager):
    assert user_manager.add_user("Joh_doe", "Joh@gmail.com") == True
    assert user_manager.get_user("Joh_doe") == "Joh@gmail.com"
    
def test_add_duplicate_user(user_manager):
    user_manager.add_user("Joh_doe", "Joh@gmail.com")
    with pytest.raises(ValueError):
        user_manager.add_user("Joh_doe", "another@gmail.com")
        
        
from main import Database

@pytest.fixture
def db():
    database = Database()
    yield database
    database.data.clear()
    
    
def test_add_user(db):
    db.add_user(1, "Masha")
    assert db.get_user(1) == "Masha"
    
    
def test_add_duplicate_user(db):
    db.add_user(1, "Masha")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "Bob")


def test_delete_user(db):
    db.add_user(2, "Bob")
    db.delete_user(2)
    assert db.get_user(2) is None

