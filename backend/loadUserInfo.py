import pickle


def loadUserInfo() -> dict:
    setup = open(".exoro_data/user_data.dat", "rb")
    userData = pickle.load(setup)
    setup.close()
    return userData
