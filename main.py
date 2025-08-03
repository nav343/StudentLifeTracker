"""
Art integrated project for Computer Science 2025-26

@Author: nav343 (Navaneeth K)
@Version: v1

**The Idea**
A system for analysing marks and suggesting strengths and weaknesses. Also has a todo's list for students
"""

from backend.dashboard import Dashboard
from backend.loadUserInfo import loadUserInfo
from backend.userSetup import CreateUser
from utils.window import Window

window = Window()

try:
    Dashboard(window, loadUserInfo())
except KeyboardInterrupt:
    window.quit()
except FileNotFoundError:
    try:
        userData = CreateUser()
        Dashboard(window, userData)
    except KeyboardInterrupt:
        window.quit()
