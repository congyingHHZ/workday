# workday
计算工作日的小工具
一、前言
略

二、介绍
实现功能：
 - 功能1：输入一个日期X，天数Y，计算日期X后Y个工作日后的日期是几号
 - 功能2：输入一个日期X，日期Z，计算日期X与日期Z之间的工作日天数

三、代码
https://github.com/congyingHHZ/workday

四、使用方法
  
1. 日历文件夹下需手动添加当年的日历文件，格式见【2018年日历】
2. 执行 
   - 直接运行脚本 `python -m run`
   - 使用pyinstaller打包 
       1. 生成exe `pyinstaller -F run.py`
       2. 把生成的exe放到与日历文件同级文件夹下双击运行
3. 弹出窗口，按提示选择功能，并输入日期
