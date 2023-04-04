- 自用,修改自:  https://github.com/Greetlist/wow_fishing_script
- 下一步: 增加钓鱼失败提醒 
- [OverView](#overview)
- [How To Build It](#how-to-build-it)
  - [python version](#python-version)
    - [Build From Source](#build-from-source)
    
  
- [How To Use It](#how-to-use-it)
- [Core Config](#core-config)
- [TODO List](#todo-list)
- [Report Bug And Advice](#report-bug-and-advice)
- [Relate Tools And Repo](#relate-tools-and-repo)
- [Useful WebSite](#useful-website)

# OverView
Auto Fising Script with GUI.
Rate of success catching fishing is over **90%**.


# How To Use It
[ForeGround Example GIF](https://1drv.ms/u/s!ArufjyMgeESVgc9x5MZkED7NZo_KGQ?e=cW1eAh)

[BackGround Example GIF](https://1drv.ms/u/s!ArufjyMgeESVgc9zOjW1tHBFcisxEA?e=Zh2iTy)

> Notice: BackGround Mode need 3 prepare works before fishing
1. Turn Interact On

![Turn On](https://img.ppcn.net/uploadfile/2022/1028/20221028153852683.png)

2. execute these two macro

```
/console SoftTargetInteractArc 2      # allowed you to interact without facing things
/console SoftTargetInteractRange 50   # increase your interact range to 50
```

3. Bind interact key to **'9'**

![Interact Key Setting](https://olimg.3dmgame.com/uploads/images/raiders/2022/0830/1661822926765.png)

# Core Config
1. Fishing area. (Coordinate of screen is auto-complete, support multi-screen, **not support cross-screen**)
2. Game Window Name. (Adjust different language)
3. Fishing Idle Time.
4. Cast Some Skill Periodically [keyboard '6']. (toy or bait)
5. Switch To TestMode. (Take some screenshot for testing)
6. Switch To FG/BG Mode. (BG Mode allow you to do something else while WOW window is inactive)
7. Use Coordinate judgement or Area Judgement. (Coordinate Judgement is more stable while testing in real game)
8. Max Fishing Count, :warning: **0 is not infinity, Please Increase this value manually**
9. Probability Of Jumping before every fishing (default: 10%).

# TODO List
- [x] Add Max-Fishing-Count config.
- [x] Add Random Jump and Jump probability config.
- [ ] Support invoke some WOW's Macro before fishing.
- [ ] Auto Online/Offline.
- [ ] Key Binding configurable.
- [ ] Auto change coordinate threshold. (Reinforcement)
- [ ] Auto change Fish-Float hsv color range to fit different environment. (Reinforcement)

# Report Bug And Advice
If you trapped with some unknown bugs or want to give some advice, Please [new issue](https://github.com/Greetlist/wow_fishing_script/issues/new/choose) to me.

# Relate Tools And Repo
[PySide6](https://doc.qt.io/qtforpython/#)

[pywin32](https://github.com/mhammond/pywin32)

[pyautogui](https://github.com/asweigart/pyautogui)

[pyinstaller](https://github.com/pyinstaller/pyinstaller)

[python-mss](https://github.com/BoboTiG/python-mss)

[opencv-python](https://github.com/opencv/opencv-python)

# Useful WebSite
[MicroSoft Win32 API](https://learn.microsoft.com/en-us/windows/win32/)

[PySide6 Tutorials](https://www.pythonguis.com/tutorials/)

[pywin32 Online API](http://timgolden.me.uk/pywin32-docs/)

[How-To-Send-Key-To-Inactive-Window](https://stackoverflow.com/questions/12996985/send-some-keys-to-inactive-window-with-python)

[MicroSoft Win32 Virtual Key Binding](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

[HSV Color Range Switcher](https://stackoverflow.com/a/59906154/13747065)
