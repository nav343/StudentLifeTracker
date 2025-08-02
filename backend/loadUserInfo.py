import pickle


def loadUserInfo() -> dict:
    setup = open("tests/user_data.dat", "rb")
    userData = pickle.load(setup)
    setup.close()
    return userData
