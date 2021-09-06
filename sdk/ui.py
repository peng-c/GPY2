#导入tkinter的库文件
import io
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import main
import time
# pip install pillow

#创建根窗口
root = Tk()
#设置窗口标题
root.title('体温打卡系统')
#设置窗口大小和位置
root.geometry("900x600")

#标题
L1 = Label(root, text="基于AI800的非接触测温和人脸识别的体温打卡系统",font=("华文行楷", 20))
L1.pack(padx=5, pady=5,side="top")

# 对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例

def resize(w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片
    w, h = pil_image.size  # 获取图像的原始大小
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)

w_box = 200  # 期望图像显示的大小（窗口大小）
h_box = 200

pil_image = Image.open(r'img.jpg')  # 以一个PIL图像对象打开  【调整待转图片格式】

pil_image_resized = resize(w_box, h_box, pil_image)  # 缩放图像让它保持比例，同时限制在一个矩形框范围内  【调用函数，返回整改后的图片】

tk_image = ImageTk.PhotoImage(pil_image_resized)  # 把PIL图像对象转变为Tkinter的PhotoImage对象  【转换格式，方便在窗口展示】
# ====================================================================
# Label: 这个小工具，就是个显示框，小窗口，把图像大小显示到指定的显示框
label = Label(root, image=tk_image, width=w_box, height=h_box)
# padx,pady是图像与窗口边缘的距离
label.pack(padx=5, pady=5)


# canvas = Canvas(root, width=200, height=200)
# image_file = ImageTk.PhotoImage(file='faceimage.jpg')
# #image_file = PhotoImage(file='img.gif')
# image = canvas.create_image(200, 0, anchor='n', image=image_file)
# canvas.pack(side='top')
# Label(root, text='welcome',font=('Arial', 16)).pack()


#添加各种组件(按钮)
btn1 = Button(root,text="开始打卡",bg="pink",width=15,height=5)
btn2 = Button(root,text="打卡详情",bg="yellow",width=15,height=5)


# list1=[12,3,4,5,6,7,8]
#list2=["1","jhaj","fjd","fjdsk"]#全体学生信息
#设置几何布局
btn1.pack(side="top")
btn2.pack(side="top")
#创建事件方法
def main_daka(e):
	# 1.试试能不能检测相机，显示实时图像
	# 2.调用主函数
# 	3. 如果打卡成功，（主函数调用成功）
# 	4.返回测量的温度，姓名，进入时间
    canshu4=main.woshimain()
    if(canshu4.flag==1):
        messagebox.showinfo("打卡成功", "name: "+str(canshu4.name)+"  curren_time  "+str(canshu4.curren_time)+"  Temperature  "+str(canshu4.Temperature))
        
        
# 打卡的情况 这里初步定为 输出为txt文件
def xiangqing(e):
  # 	1.打开文件并写入文件
    f = open('daka.txt','a')
    f.write("--------------------")
    f.write("\n已打卡: " +'\n'+str(main.list_yi))
    f.write("\n"+"总计  "+str(len(main.list_yi))+"  已打卡\n")
    f.write("\nweidaka: "+"\n"+str(main.list_wei))
    f.write("\n"+"总计  "+str(len(main.list_wei))+"  未打卡\n")
    f.write("\n------"+time.asctime(time.localtime(time.time()))+"------")
    f.close()
    messagebox.showinfo("详情", "已打卡和未打卡详情已经输入到本地，请到daka.txt中查看")

def shanchu(list2,list2_wei,list2_yi):
	def hanshu_shanchu(list2,list2_wei,list2_yi):
		ox=old_xinxi.get()
		if ox in list2:
			list2.remove(ox)
			messagebox.showinfo('成功', '成功删除!')
		else:
			messagebox.showerror('失败', '该元素不存在!')
		# 定义长在窗口上的窗口
		if ox in list2_wei:
			list2_wei.remove(ox)
		if ox in list2_yi:
			list2_yi.remove(ox)
	root_shanchu = Toplevel(root)
	root_shanchu.geometry('300x200')
	root_shanchu.title('delete')

	old_xinxi = StringVar()  # 输入要删除的人
	Label(root_shanchu, text='name').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
	entry_new_name = Entry(root_shanchu, textvariable=old_xinxi)  # 创建一个注册名的`entry`，变量为`new_name`
	entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

	# 下面的 sign_to_Hongwei_Website
	btn_comfirm_shanchu = Button(root_shanchu, text='确定删除', command=lambda :hanshu_shanchu(list2,list2_wei,list2_yi))
	btn_comfirm_shanchu.place(x=180, y=120)

def zengjia(list2,list2_wei):
	def hanshu_zengjia(list2,list2_wei):
		nx = new_xinxi.get()
		if nx not in list2_wei:list2_wei.append(nx)
		if nx in list2:
			messagebox.showerror('失败', '该元素已存在!')
		else:
			list2.append(nx)
			messagebox.showinfo('成功', '成功增加!')

	# 定义长在窗口上的窗口
	root_zengjia = Toplevel(root)
	root_zengjia.geometry('300x200')
	root_zengjia.title('add')

	new_xinxi = StringVar()  # 输入要增加
	Label(root_zengjia, text='name').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
	entry_new_name = Entry(root_zengjia, textvariable=new_xinxi)  # 创建一个注册名的`entry`，变量为`new_name`
	entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

	# 下面的 sign_to_Hongwei_Website
	btn_comfirm_zengjia = Button(root_zengjia, text='确定增加', command=lambda :hanshu_zengjia(list2,list2_wei))
	btn_comfirm_zengjia.place(x=180, y=120)

def chakan(list2):
    messagebox.showinfo('信息',str(list2))

# 组件绑定绑定事件
btn1.bind("<Button-1>",main_daka)
btn2.bind("<Button-1>",xiangqing)

btn_shanchu = Button(root, text='删除', command=lambda :shanchu(main.list2,main.list_wei,main.list_yi))
btn_shanchu.place(x=120, y=240)
btn_zengjia = Button(root, text='增加', command=lambda :zengjia(main.list2,main.list_wei))
btn_zengjia.place(x=200, y=240)
btn_chakan = Button(root, text='查看', command=lambda :chakan(main.list2))
btn_chakan.place(x=120, y=280)

#使窗口持续运行
root.mainloop()
#print(list2)











# 树莓派摄像头预览
# from picamera import PiCameras
#
# from time import sleep
#
# camera = PiCamera()
#
# camera.start_preview()
#
# sleep(5)
#
# camera.stop_preview()