#Andy chen������python����������Ԥ��ϵͳ
from tkinter import *
import urllib.request
import gzip
import json
from tkinter import messagebox

root = Tk()


def main():
    # ���봰��
    root.title('������ѯ')  # ���ڱ���
    Label(root, text='���������').grid(row=0, column=0)  # ���ñ�ǩ������λ��
    enter = Entry(root)  # �����
    enter.grid(row=0, column=1, padx=20, pady=20)  # ����λ��
    enter.delete(0, END)  # ��������
    enter.insert(0, '��ɽ')  # ����Ĭ���ı�
    # enter_text = enter.get()#��ȡ����������

    running = 1

    def get_weather_data():  # ��ȡ��վ����
        city_name = enter.get()  # ��ȡ����������
        url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city_name)
        url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
        # ��ַ1ֻ��Ҫ�������������ַ2��Ҫ������д���
        # print(url1)
        weather_data = urllib.request.urlopen(url1).read()
        # ��ȡ��ҳ����
        weather_data = gzip.decompress(weather_data).decode('utf-8')
        # ��ѹ��ҳ����
        weather_dict = json.loads(weather_data)
        # ��json����ת��Ϊdict����
        if weather_dict.get('desc') == 'invilad-citykey':
            print(messagebox.askokcancel("xing", "������ĳ��������󣬻�����������δ��¼�����ڳ���"))
        else:
            # print(messagebox.askokcancel('xing','bingguo'))
            show_data(weather_dict, city_name)

    def show_data(weather_dict, city_name):  # ��ʾ����
        forecast = weather_dict.get('data').get('forecast')  # ��ȡ���ݿ�
        root1 = Tk()  # ������
        root1.geometry('650x280')  # �޸Ĵ��ڴ�С
        root1.title(city_name + '����״��')  # �����ڱ���

        # ���������б�
        for i in range(5):  # ��ÿһ������ݷ����б���
            LANGS = [(forecast[i].get('date'), '����'),
                     (forecast[i].get('fengxiang'), '����'),
                     (str(forecast[i].get('fengji')), '�缶'),
                     (forecast[i].get('high'), '�����'),
                     (forecast[i].get('low'), '�����'),
                     (forecast[i].get('type'), '����')]
            group = LabelFrame(root1, text='����״��', padx=0, pady=0)  # ���
            group.pack(padx=11, pady=0, side=LEFT)  # ���ÿ��
            for lang, value in LANGS:  # �����ݷ�������
                c = Label(group, text=value + ': ' + lang)
                c.pack(anchor=W)
        Label(root1, text='����' + weather_dict.get('data').get('ganmao'),
              fg='green').place(x=40, y=20, height=40)  # ��ܰ��ʾ
        Label(root1, text="www.andyccr.com", fg="green", bg="yellow").place(x=10, y=255, width=125,
                                                                                height=20)  # Andy����վ
        Button(root1, text='ȷ�ϲ��˳�', width=10, command=root1.quit).place(x=500, y=230, width=80, height=40)  # �˳���ť
        root1.mainloop()

    # ���ð���
    Button(root, text="ȷ��", width=10, command=get_weather_data) \
        .grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Button(root, text='�˳�', width=10, command=root.quit) \
        .grid(row=3, column=1, sticky=E, padx=10, pady=5)
    if running == 1:
        root.mainloop()


if __name__ == '__main__':
    main()
