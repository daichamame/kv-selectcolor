from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
import sys

#--------------------------------------------------------------------------------------------------
# プログラム終了クラス
class PopupExitDialog(Popup):
    pass
    # プログラム終了
    def exec_exit(self):
       sys.exit()
#--------------------------------------------------------------------------------------------------
# メインウィジット
class MameWidget(Widget):
    # 初期処理
    def __init__(self, **kwargs):
        super(MameWidget, self).__init__(**kwargs)
        # ウィンドウサイズの指定
        Window.size = (640,480)  # Windowsで確認用
    # タッチアップしたタイミングで設定値を変更 
    def on_touch_up(self, touch):
        # 文字色
        self.ids.r_label.text = str(format(self.ids.r_slider.value,".1f"))
        self.ids.g_label.text = str(format(self.ids.g_slider.value,".1f"))
        self.ids.b_label.text = str(format(self.ids.b_slider.value,".1f"))
        self.ids.a_label.text = str(format(self.ids.a_slider.value,".1f"))
        # 背景色
        self.ids.r_bg_label.text = str(format(self.ids.r_bg_slider.value,".1f"))
        self.ids.g_bg_label.text = str(format(self.ids.g_bg_slider.value,".1f"))
        self.ids.b_bg_label.text = str(format(self.ids.b_bg_slider.value,".1f"))
        self.ids.a_bg_label.text = str(format(self.ids.a_bg_slider.value,".1f"))
        # グレースケールの計算
        gray_value = self.ids.r_slider.value*0.299 + self.ids.g_slider.value*0.587 + self.ids.b_slider.value*0.114
        gray_bg_value = self.ids.r_bg_slider.value*0.299 + self.ids.g_bg_slider.value*0.587 + self.ids.b_bg_slider.value*0.114

        # 文字色と背景色を設定
        self.ids.rgb_label.color=[self.ids.r_slider.value,self.ids.g_slider.value,self.ids.b_slider.value,self.ids.a_slider.value]
        self.ids.rgb_label.background_color=[self.ids.r_bg_slider.value,self.ids.g_bg_slider.value,self.ids.b_bg_slider.value,self.ids.a_bg_slider.value]  
        self.ids.gray_label.color=[gray_value,gray_value,gray_value,self.ids.a_slider.value]
        self.ids.gray_label.background_color=[gray_bg_value,gray_bg_value,gray_bg_value,self.ids.a_bg_slider.value]  
        return super().on_touch_up(touch)
    # 終了ダイアログ
    def exit_dialog(self):
        popup = PopupExitDialog()
        popup.open()
# アプリの定義
class SelectColorApp(App):  
    def __init__(self, **kwargs):
        super(SelectColorApp,self).__init__(**kwargs)
        self.title="カラー選択"                          # ウィンドウタイトル名
# メインの定義
if __name__ == '__main__':
    SelectColorApp().run()                          # クラスを指定
Builder.load_file('selectcolor.kv')                 # kvファイル名

