import wx
import random


def passwordGenerate(lenght, chars):
    password = ""
    for j in range(lenght):
        password += random.choice(chars)
    return password


CharArray = "1234567890-=qwertyuiopasdfghjklzxcvbnm,./;'[]\* ZAQWSXEDCRFVTGBYHNUJMIKOLP<>?:{}+_)(*&^%$#@!`~"


def p_fun(event):
    global CharArray
    textC_1.AppendText(passwordGenerate(int(spin_C.Value), CharArray) + "\n")


def p1_fun(event):
    frame.SetLabel("Programa")
    text.SetLabel("Program for generating passwords")
    button_1.SetLabel("Generate")
    checkBox.SetLabel("With concrete\nsymbols")
    button_2.SetLabel("Accept\nsymbols")


def p2_fun(event):
    frame.SetLabel("Програма")
    text.SetLabel("Программа для генераций паролей")
    button_1.SetLabel("Сгенерировать")
    checkBox.SetLabel("С конкретнимы\nсымволамы")
    button_2.SetLabel("Принять\nсимволы")


def p3_fun(event):
    global CharArray
    if checkBox.Value:
        frame.SetSize(350, 300)
        rad_b_1.SetPosition((10, 240))
        rad_b_2.SetPosition((80, 240))
        checkBox.SetPosition((220, 230))
        textC_2.SetSize((170, 40))
        button_2.SetSize((60, 40))
    else:
        frame.SetSize(350, 260)
        rad_b_1.SetPosition((10, 200))
        rad_b_2.SetPosition((80, 200))
        checkBox.SetPosition((220, 190))
        textC_2.SetSize(170, 0)
        button_2.SetSize(60, 0)
        CharArray = "1234567890-=qwertyuiopasdfghjklzxcvbnm,./;'[]\* ZAQWSXEDCRFVTGBYHNUJMIKOLP<>?:{}+_)(*&^%$#@!`~"


def p4_fun(event):
    global CharArray
    CharArray = "".join(list(set(textC_2.GetValue())))


app = wx.App()
frame = wx.Frame(None, title="Програма", pos=(500, 300), size=(350, 260),
                 style=wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION)
box = wx.BoxSizer(wx.VERTICAL)
frame.SetBackgroundColour("#FFF8F5")
panel_1 = wx.Panel(frame)

panel_2 = wx.Panel(panel_1)
box1 = wx.BoxSizer(wx.HORIZONTAL)

text = wx.StaticText(panel_2, label="Программа для генераций паролей", style=wx.ALIGN_CENTRE)
textC_1 = wx.TextCtrl(panel_1, -1, style=wx.TE_MULTILINE | wx.TE_NOHIDESEL | wx.TE_READONLY | wx.EXPAND, size=(0, 100))
button_1 = wx.Button(panel_1, label="Сгенерировать", size=(120, 30))
rad_b_1 = wx.RadioButton(panel_1, label="Русский", pos=(10, 200), style=wx.RB_GROUP)
rad_b_2 = wx.RadioButton(panel_1, label="English", pos=(80, 200))

checkBox = wx.CheckBox(panel_1, label="С конкретнимы \nсымволамы", pos=(220, 190))
textC_2 = wx.TextCtrl(panel_1, -1, style=wx.TE_MULTILINE | wx.TE_NOHIDESEL, pos=(10, 180), size=(100, 0))
button_2 = wx.Button(panel_1, label="Принять\nсимволы", pos=(190, 180), size=(60, 0))
spin_C = wx.SpinCtrl(panel_1, value="8", min=5, max=30, pos=(150, 138), size=(50, 30))
spin_C.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

textC_1.SetFont(wx.Font(11, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_HEAVY))
text.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
box1.Add(text, 0, flag=wx.TEXT_ALIGNMENT_CENTER | wx.TOP | wx.DOWN, border=20)

panel_1.SetSizer(box1)
box.Add(panel_2, flag=wx.EXPAND | wx.ALL, border=5)
box.Add(textC_1, 0, flag=wx.EXPAND | wx.ALL, border=0)
box.Add(button_1, flag=wx.ALL, border=10)

panel_1.SetSizer(box)
frame.Bind(wx.EVT_BUTTON, p_fun, button_1)
frame.Bind(wx.EVT_RADIOBUTTON, p1_fun, rad_b_2)
frame.Bind(wx.EVT_RADIOBUTTON, p2_fun, rad_b_1)
frame.Bind(wx.EVT_CHECKBOX, p3_fun, checkBox)
frame.Bind(wx.EVT_BUTTON, p4_fun, button_2)

frame.Show()
app.MainLoop()
