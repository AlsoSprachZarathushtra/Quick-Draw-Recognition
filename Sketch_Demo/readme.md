# 草图识别的简单演示Demo

用tkinter实现GUI
预测模型为densenet121

环境：python3.6    tensorflow1.13     PIL    numpy     tkinter    heapq
执行Canvas.py
绘图界面鼠标左键按下开始画图，每画完一笔，自动识别给出结果，单击鼠标右键重置画布。

note：模型加载时间过长，约1分钟。
      此demo中所使用的模型仅采用了最终图像信息，未采用笔画序列信息。
      后序会加入更复杂的模型，并考虑压缩模型的规模。